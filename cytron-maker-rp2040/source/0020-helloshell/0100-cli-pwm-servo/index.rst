.. _hs-cli-pwm-servo:

Shell-Kommando ``pwm`` für Servomotor
#####################################

.. sidebar:: Ziel

   Ein Servomotor wird in Bewegung gesetzt.

.. topic:: Übersicht

   **Servomotoren** sind Elektromotoren mit einer selbständigen Regelung der
   Winkelposition ihrer Motorwelle oder Drehgeschwindigkeit und Beschleunigung.
   In dieser Übung wirst du lernen, wie mit Hilfe eines einzelnen PWM Kanals
   die Ansteuerung eines Servomotors realisiert wird. Auf deinem MCU-Board
   befindet sich standardisierte Anschlüsse aus dem Modellbau für insgesamt
   4 einzelne Servomotoren.

.. admonition:: Wissenswertes
   :class: worth-knowing note
   :collapsible:

   Werfen wir zunächst noch einmal einen Blick auf den Devicetree und die
   Zuordnung der PWM Kanäle im RP2040 bezogen auf die Servo Motoren:

   .. code-block:: DTS

      &pwm {
        status = "okay";
        pinctrl-0 = <&pwm_makerpi>;
        pinctrl-names = "default";
      };

      &pwm {
        divider-int-6 = <255>;
        divider-int-7 = <255>;
      };

   .. code-block:: DTS

      &pinctrl {
        pwm_makerpi: pwm_makerpi {
          group12131415_servo_motors {
            pinmux = <PWM_6A_P12>, /* GP12: PWM6CHA (12) */
                     <PWM_6B_P13>, /* GP13: PWM6CHB (13) */
                     <PWM_7A_P14>, /* GP14: PWM7CHA (14) */
                     <PWM_7B_P15>; /* GP15: PWM7CHB (15) */
          };
        };
      };

   Die Servomotoren sind also an **GP12** bis **GP15** angeschlossen,
   an den zugehörigen **PWM Kanälen 12 bis 15**:

   .. table::
      :align: center

      +-------------+-------------+--------+--------+-----------------------------------------------------+
      | PWM Kanal RP2040 / Zephyr | GPIO (GPx)      | Devicetree ``pinctrl``                              |
      +=============+=============+========+========+=====================================================+
      |    **6A**   |    **12**   | **12** |   28   | :bgn:`SERVO:` :devicetree:`pinmux = <PWM_6A_P12>;`  |
      +-------------+-------------+--------+--------+-----------------------------------------------------+
      |    **6B**   |    **13**   | **13** |   29   | :bgn:`SERVO:` :devicetree:`pinmux = <PWM_6B_P13>;`  |
      +-------------+-------------+--------+--------+-----------------------------------------------------+
      |    **7A**   |    **14**   | **14** |        | :bgn:`SERVO:` :devicetree:`pinmux = <PWM_7A_P14>;`  |
      +-------------+-------------+--------+--------+-----------------------------------------------------+
      |    **7B**   |    **15**   | **15** |        | :bgn:`SERVO:` :devicetree:`pinmux = <PWM_7B_P15>;`  |
      +-------------+-------------+--------+--------+-----------------------------------------------------+

   .. rubric:: Wie gelingt es nun, mit einer PWM einen Servomotor zu bewegen?

   Ähnlich wie in der :ref:`vorherigen Übung <hs-cli-pwm-led>` zur LED
   Helligkeit werden Servomotoren mit einer definierten **Impulsdauer**
   von **500µs bis 2,5ms** innerhalb einer **festen Periode von 20ms**
   (Grundfrequenz *fₚ = 50Hz*) gesteuert. Je nach Typ wird damit durch
   den Servomotor selbständig eine fest definierte Winkelposition oder
   eine Drehgeschwindigkeit mit (CW) oder gegen (CCW) den Uhrzeigersinn
   geregelt.

   Du hast an deinem MCU-Board je 2 Servomotoren beider Typen angeschlossen.
   Die folgenden beiden Impulsdiagramme stellen die Details dar.

   .. figure:: /_images/doing/servo-pulse-to-pos.*
      :align: center

      Impulsdiagramm für Winkelpositionierung mit Servomotor SG90

   .. figure:: /_images/doing/servo-pulse-to-rot.*
      :align: center

      Impulsdiagramm für Drehgeschwindigkeit mit Servomotor FS90R

.. include:: bom.rsti
.. include:: assembly.rsti
.. include:: doing.rsti

.. vi: ft=rst ai ts=3 et sw=3 sta
