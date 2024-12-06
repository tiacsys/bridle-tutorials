.. _hs-cli-pwm-buzzer:

Shell-Kommando ``pwm`` für Summer (Buzzer)
##########################################

.. sidebar:: Ziel

   Der Summer gibt einen Ton aus und wird wieder abgeschaltet.

.. topic:: Übersicht

   Widmen wir uns nun einer weiteren Möglichkeit für den Einsatz der Zephyr
   PWM API. Du hast in der :ref:`vorherigen Übung <hs-cli-pwm-led>` einen
   PWM Kanal für die Änderung der LED Helligkeit benutzt. Dabei sollte dir
   aufgefallen sein, dass eine PWM Impulse erzeugt, also Schwingungen. Nutzen
   wir diese Erkenntnis nun aus, um solche Schwingungen für die Ausgabe von
   Tönen einzusetzen. Auf deinem MCU-Board befindet sich idealerweise genau
   dafür ein Summer (englisch *Buzzer*).

.. admonition:: Wissenswertes
   :class: worth-knowing note
   :collapsible:

   Werfen wir zunächst noch einmal einen Blick auf den Devicetree und die
   Zuordnung der PWM Kanäle im RP2040 bezogen auf den Buzzer:

   .. code-block:: DTS

      &pwm {
        status = "okay";
        pinctrl-0 = <&pwm_makerpi>;
        pinctrl-names = "default";
      };

      &pwm {
        divider-int-3 = <255>;
      };

   .. code-block:: DTS

      &pinctrl {
        pwm_makerpi: pwm_makerpi {
          group22_buzzer {
            pinmux = <PWM_3A_P22>; /* GP22: PWM3CHA (6) */
          };
        };
      };

   Der Buzzer ist also an **GP22** angeschlossen,
   am zugehörige **PWM Kanal 6**:

   .. table::
      :align: center

      +-------------+-------------+--------+--------+-----------------------------------------------------+
      | PWM Kanal RP2040 / Zephyr | GPIO (GPx)      | Devicetree ``pinctrl``                              |
      +=============+=============+========+========+=====================================================+
      |    **3A**   |     **6**   |    6   | **22** | :bgn:`BUZZER:` :devicetree:`pinmux = <PWM_3A_P22>;` |
      +-------------+-------------+--------+--------+-----------------------------------------------------+

   .. rubric:: Wie gelingt es nun, mit einer PWM einen Ton zu erzeugen?

   Allgemein sollte bekannt sein, dass eine alternierende Spannung an einem
   Lautsprecher oder Summer einen Schalldruck und bei hörbaren Frequenzen
   einen für Menschen wahrnehmbaren Ton erzeugt. Idealerweise ist das eine
   einzelne Sinusschwingung – Alltagsgeräusche oder Musik sind jedoch die
   Mischung (Überlagerung) einer Vielzahl von einzelnen Sinusschwingungen
   mit unterschiedlicher Frequenz und Amplitude.

   Mit geeigneter Synthesesoftware, z.B. einer *Pulse Code Modulation (PCM)*,
   wäre die Erzeugung einer einzelnen Sinusschwingung theoretisch denkbar.
   Das ist aber deutlich aufwändiger, als nur ein statisches Paar an
   Parametern in einer PWM zu setzen. **Eine PWM ist jedoch die Grundlage
   für eine PCM und das nutzen wir aus.**

   Natürlich mit Abstrichen. Dazu schauen wir uns noch einmal kurz das
   Zeitdiagramm aus der :ref:`vorherigen Übung <hs-cli-pwm-led>` an und
   wandeln es gleich etwas um. Anstatt nun innerhalb einer festen Periode
   die Dauer des Impulses zu ändern um damit die Energie im Signal (die
   effektive Spannung am Ausgang) zu steuern, werden wir nun einfach die
   Periode (Grundfrequenz) ändern und dafür das Tastverhältnis zwischen
   Impulsdauer und der Periode exakt gleich halten. Das Tastverhältnis
   wird dabei auf 50 Prozent fest definiert.

   .. figure:: /_images/doing/buzzer-period-to-freq.*
      :align: center

      Frequenzausgabe mit einer Pulse Width Modulation (PWM)

   Somit entsteht immer ein Rechtecksignal mit exakt der Grundfrequenz
   (Periode). Damit lassen sich nun Töne mit bekannter Frequenz berechnen
   und erzeugen.

   Zugegeben, ein Rechtecksignal ist nicht wirklich ein "schönes" Signal für
   Töne, besitzt es doch mit Abstand die meisten Oberwellen und neigt extrem
   stark zu "quäken" und "krächzen" in einem Summer oder Lautsprecher. Wir
   wollen die Übung aber einfach halten. Eine Signalsynthese ist ohnehin nur
   mit viel mehr Software möglich. Wer genau hinschaut sieht auch, dass der
   Energieinhalt auf 50% abfällt. Du kannst aber davon ausgehen, dass der
   Summer auf deinem MCU-Board auch mit der halben Energie "laut genug" ist.

.. include:: bom.rsti
.. include:: assembly.rsti
.. include:: doing.rsti

.. target-notes::

.. vi: ft=rst ai ts=3 et sw=3 sta
