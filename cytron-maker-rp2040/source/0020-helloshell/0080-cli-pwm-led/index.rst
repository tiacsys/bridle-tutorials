.. _hs-cli-pwm-led:

Shell-Kommando ``pwm`` für LED
##############################

.. sidebar:: Ziel

   Beliebige LED verändert ihre Helligkeit.

.. topic:: Übersicht

   **Pulse Width Modulation** – oder kurz nur **PWM** – ist eine Modulationsart,
   bei der eine elektrische Spannung zwischen zwei Werten wechselt. Dabei wird
   bei konstanter Frequenz die Dauer eines Rechteck-Impulses moduliert. Das
   zugehörige Kommando :bcy:`pwm` mit seinen Unterkommandos ist eine direkte
   Abbildung auf die zugrundeliegende Zephyr API, siehe dazu auch
   :ref:`zephyr:pwm_api` in der Zephyr Dokumentation.

   In dieser Übung finden wir zum Teil Antworten auf offene Fragen aus der
   :ref:`zurückliegenden Übung <hs-cli-led>`, als es um die Zephyr LED API
   ging. Du hattest dort bereits gelernt, dass es unterhalb der Zephyr LED
   API noch eine Abhängigkeit zu speziellen APIs oder Treibern in die Hardware
   gibt. In dieser Übung werden wir uns genau auf diese Ebene begeben, direkt
   auf die Ebene der Signalmodulation und können uns über die abstrakten Zwänge
   der LED API hinweg setzten.

   Somit wird es dir möglich, nicht nur die eine einzige *Dignose-LED an GP7*
   zu steuern, sondern eine beliebig andere. So zum Beispiel die zusätzlich
   angeschlossenen **externe LED** am Steckverbinder **GROVE 3**.

.. admonition:: Wissenswertes
   :class: worth-knowing note
   :collapsible:

   Die :ref:`Zephyr PWM API <zephyr:pwm_api>` unterstützt die wichtigsten
   funktionalen Eigenschaften einer PWM. Das sind: *Period* in Zyklen, Mikro-
   oder Nanosekunden und *Pulse* in Zyklen, Mikro- oder Nanosekunden. Alle
   diese Eigenschaften sind für jeden einzelnen PWM Kanal in einem System
   durch das Shell Kommando :bcy:`pwm` zugänglich. **Hardware spezifische
   Einstellungen**, wie Vorteiler oder Pin-Zuordnungen, **können
   ausschließlich im Devicetree definiert werden.**

   Das von dir benutzte MCU-Board ist mit dem Mikrocontroller **RP2040**
   ausgestattet und bietet dir insgesamt 16 PWM Kanäle. Deren Ausgänge
   teilen sich jeweils identische Pins mit einfachen GPIO Ausgängen. In
   unseren Übungen wirst du damit nicht in Konflikt geraten, jedoch sind
   auch nur die notwendigsten Einstellungen im Devicetree definiert.

   Hier ein Auszug mit Bezug auf LEDs:

   .. code-block:: DTS

      &pwm {
        status = "okay";
        pinctrl-0 = <&pwm_makerpi>;
        pinctrl-names = "default";
      };

      &pwm {
        divider-frac-3 = <15>;
        divider-int-3 = <255>;
      };

   .. code-block:: DTS

      &pinctrl {
        pwm_makerpi: pwm_makerpi {
          group7_led {
            pinmux = <PWM_3B_P7>; /* GP7: PWM3CHB (7) */
          };
        };
      };

   Alle 30 Pins des RP2040 können für PWM verwendet werden:

   .. table::
      :align: center

      +-------------+-------------+--------+--------+-----------------------------------------------------+
      | PWM Kanal RP2040 / Zephyr | GPIO (GPx)      | Devicetree ``pinctrl``                              |
      +=============+=============+========+========+=====================================================+
      |      0A     |       0     |    0   |   16   |                                                     |
      +-------------+-------------+--------+--------+-----------------------------------------------------+
      |      0B     |       1     |    1   |   17   |                                                     |
      +-------------+-------------+--------+--------+-----------------------------------------------------+
      |      1A     |       2     |    2   |   18   |                                                     |
      +-------------+-------------+--------+--------+-----------------------------------------------------+
      |      1B     |       3     |    3   |   19   |                                                     |
      +-------------+-------------+--------+--------+-----------------------------------------------------+
      |      2A     |       4     |    4   |   20   |                                                     |
      +-------------+-------------+--------+--------+-----------------------------------------------------+
      |      2B     |       5     |    5   |   21   | :brd:`externe LED:` :ird:`nicht konfiguriert`       |
      +-------------+-------------+--------+--------+-----------------------------------------------------+
      |    **3A**   |     **6**   |    6   | **22** | **BUZZER:** :devicetree:`pinmux = <PWM_3A_P22>;`    |
      +-------------+-------------+--------+--------+-----------------------------------------------------+
      |    **3B**   |     **7**   |  **7** |   23   | :bgn:`LED:` :devicetree:`pinmux = <PWM_3B_P7>;`     |
      +-------------+-------------+--------+--------+-----------------------------------------------------+
      |    **4A**   |     **8**   |  **8** |   24   | **MOTOR:** :devicetree:`pinmux = <PWM_4A_P8>;`      |
      +-------------+-------------+--------+--------+-----------------------------------------------------+
      |    **4B**   |     **9**   |  **9** |   25   | **MOTOR:** :devicetree:`pinmux = <PWM_4B_P9>;`      |
      +-------------+-------------+--------+--------+-----------------------------------------------------+
      |    **5A**   |    **10**   | **10** |   26   | **MOTOR:** :devicetree:`pinmux = <PWM_5A_P10>;`     |
      +-------------+-------------+--------+--------+-----------------------------------------------------+
      |    **5B**   |    **11**   | **11** |   27   | **MOTOR:** :devicetree:`pinmux = <PWM_5B_P11>;`     |
      +-------------+-------------+--------+--------+-----------------------------------------------------+
      |    **6A**   |    **12**   | **12** |   28   | **SERVO:** :devicetree:`pinmux = <PWM_6A_P12>;`     |
      +-------------+-------------+--------+--------+-----------------------------------------------------+
      |    **6B**   |    **13**   | **13** |   29   | **SERVO:** :devicetree:`pinmux = <PWM_6B_P13>;`     |
      +-------------+-------------+--------+--------+-----------------------------------------------------+
      |    **7A**   |    **14**   | **14** |        | **SERVO:** :devicetree:`pinmux = <PWM_7A_P14>;`     |
      +-------------+-------------+--------+--------+-----------------------------------------------------+
      |    **7B**   |    **15**   | **15** |        | **SERVO:** :devicetree:`pinmux = <PWM_7B_P15>;`     |
      +-------------+-------------+--------+--------+-----------------------------------------------------+

   .. rubric:: Wie gelingt es nun, mit einer PWM die LED Helligkeit einzustellen?

   Der Strom durch eine LED darf seine Stärke variieren. Nur negativ sollte
   er nie werden. Das kann eine LED zerstören. Eine PWM kann nun dazu dienen,
   je nach eingestellter Pulsweite den Energieanteil in einem Rechtecksignal
   zwischen 0 und 100 Prozent in Bezug auf eine feste Periode (Grundfrequenz)
   zu variieren. Wie bei den meisten elektrischen Verbrauchern ist auch an
   einer LED der Verbrauch von Energie proportional zum elektrischen Strom.
   Die Helligkeit einer LED lässt sich also über die effektive Spannung aus
   einer PWM variieren.

   Hierzu ein paar Beispiele:

   .. figure:: /_images/doing/led-pulse-to-ueff.*
      :align: center

      Spannungsausgabe mit einer Pulse Width Modulation (PWM)

.. include:: bom.rsti
.. include:: assembly.rsti
.. include:: doing.rsti

.. vi: ft=rst ai ts=3 et sw=3 sta
