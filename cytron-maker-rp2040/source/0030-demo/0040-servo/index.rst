.. _demo-zephyr-basic-servo:

Servomotor hin und her bewegen
##############################

.. sidebar:: Ziel

   Übersetzen, programmieren und spielen mit dem Zephyr Basic Beispiel
   :doc:`zephyr:samples/basic/servo_motor/README`

.. topic:: Übersicht

   Erinnere dich bitte an die :ref:`zurückliegende Übung <hs-cli-pwm-servo>`,
   als du mit dem Zephyr Shell Kommando :bcy:`pwm` die Servomotoren manuell
   in Bewegung versetzt hast. Nun werden wir ein Zephyr Standard Beispiel für
   einen Servomotor dazu benutzen. Dieses nutzt ebenso den Devicetree als Basis
   für die Deklaration konkreter Hardware. Im Gegensatz zu den vorangegangenen
   Beispielen wirst du nun aber keinen eigenen Devicetree Overlay schreiben.

.. rubric:: Wissenswertes

**Zephyr** kennt **seit Version 3.5** das Konzept der :ref:`zephyr:snippets`.
Ganz kurz beschrieben, bieten dir diese die Möglichkeit, aus einem Projekt
heraus **allgemeingültige** (das ist wichtig) **Devicetree Overlays** und
**Kconfig Artefakte** als Dateien fertig vorzugeben, also mit dem Projekt
zu pflegen und zu revisionieren. Zephyr bietet dir dann einen Zugriff auf
diese Dateien zum Build-Zeitpunkt und sorgt für die Anwendung dieser
*"Schnipsel"* im richtigen Moment an allerletzter Stelle.

.. only:: rinoh

   |nbsp|

   |nbsp|

.. admonition:: Gut zu wissen
   :class: info

   **Snippets übernehmen also das umständliche setzen der Umgebungsvariable**
   :makevar:`EXTRA_DTC_OVERLAY_FILE` und / oder :makevar:`EXTRA_CONF_FILE`
   **beim Aufruf von** :program:`west build …` **wenn ein Shield (noch) fehlt.**

.. only:: rinoh

   |nbsp|

   |nbsp|

Auf Ebene deines MCU-Boards *Cytron – Maker Pi RP2040* werden bereits die für
alle 4 Servomotoren benutzten PWM Kanäle deklariert – du erinnerst dich an die
:ref:`zurückliegende Übung <hs-cli-pwm-servo>`? Was dort noch nicht gesagt
wurde, auch die 4 Servomotoren selbst werden deklarativ vorbereitet, um diese
gezielt in einer Zephyr Applikation, wie dieser hier, benutzen zu können.

Das sieht im Devicetree deines MCU-Boards folgendermaßen aus:

.. rst-class:: page-break

   .. only:: rinoh

      |nbsp|
.. QUIRKS: Only with this dummy paragraph, the special rinohtype class
   'page-break-paragraph' react as expected. But the '.. code-block::' directive
   should also be handled as a 'ParagraphStyle' and trigger that class, But
   it doesn't work as expected. Fix this later!

.. code-block:: DTS

   / {
     pwm_servo_motors {
       compatible = "pwm-servos";
       status = "okay";

       pwm_servo0: pwm_servo_0 {
         pwms = <&pwm 12 PWM_MSEC(20) PWM_POLARITY_NORMAL>;
         label = "PWM_SERVO_0";
       };
       pwm_servo1: pwm_servo_1 {
         pwms = <&pwm 13 PWM_MSEC(20) PWM_POLARITY_NORMAL>;
         label = "PWM_SERVO_1";
       };
       pwm_servo2: pwm_servo_2 {
         pwms = <&pwm 14 PWM_MSEC(20) PWM_POLARITY_NORMAL>;
         label = "PWM_SERVO_2";
       };
       pwm_servo3: pwm_servo_3 {
         pwms = <&pwm 15 PWM_MSEC(20) PWM_POLARITY_NORMAL>;
         label = "PWM_SERVO_3";
       };
     };
   };

Einem Systemarchitekt ist sicher schon in der zurückliegenden PWM Übung
aufgefallen, dass Servomotoren *"Geräteeigenschaften"* besitzen – die Impulse
für die jeweiligen Winkelpositionen oder Drehrichtungen werden in Realität
Bauform abhängig sein und je nach Typ und Größe der Motoren und Hersteller
andere Bedingungen an die PWM stellen. Kurz gesagt: **Der Devicetree deines
MCU-Boards darf keine spezifischen Parameter der tatsächlich benutzen
Servomotoren vorgeben.**

Für das nun benutzte Zephyr Standard Beispiel fehlen also die Parameter für die
maximal und minimal erlaubten Impulsdauern im Devicetree. Genau dafür stellt
dir Bridle einen fertigen *"Schnipsel"* zur Verfügung, abgelegt innerhalb deines
West Workspace unter :file:`bridle/snippets/pwm-servo` und das sortiert nach
jeweils unterstützen Boards, also:

   :file:`bridle/snippets/pwm-servo/boards/cytron_maker_pi_rp2040.overlay`.

Der Inhalt lautet:

.. code-block:: DTS

   servo: &pwm_servo0 {
     compatible = "pwm-servo";
     min-pulse = <PWM_USEC(500)>;
     max-pulse = <PWM_USEC(2500)>;
   };

Die Verwaltung von Zephyr Snippets erfolgt wiederum rein deklarativ über
semantisch geschützte YAML Dateien. Hierdurch bereitet dir Bridle also den
rein symbolischen Snippet-Namen ``pwm-servo`` auf, den du mit dem Aufruf
von :program:`west build … -S pwm-servo …` nur noch benutzen musst.

.. admonition:: Gut zu wissen
   :class: info

   Das ist übrigens dasselbe Prinzip, das du ständig mit der Angabe von
   :program:`west build … -S usb-console …` für die USB-CDC/ACM Console
   benutzt.

.. include:: bom.rsti
.. include:: assembly.rsti
.. include:: doing.rsti

.. vi: ft=rst ai ts=3 et sw=3 sta
