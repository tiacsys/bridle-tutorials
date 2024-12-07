.. _hs-cli-led:

Shell-Kommando ``led``
######################

.. sidebar:: Ziel

   Beliebige LED über dedizierten Index schalten.

.. topic:: Übersicht

   **Light Emitting Diode** – oder kurz nur **LED** – ist ein
   Halbleiter-Bauelement, das Licht ausstrahlt, wenn elektrischer Strom in
   Durchlassrichtung fließt. Einzelne LEDs oder ganze LED-Verbünde (meist in
   Matrix- oder Streifen-Anordnung) müssen nicht zwangsläufig über *GPIO*
   Leitungen in ein System integriert sein. Das Ein- und Ausschalten kann
   mitunter mehrere Zephyr Treiber benötigen. Für den Benutzer führt Zephyr
   daher die separate Geräteklasse von LEDs ein und bildet den Zugang innerhalb
   der Shell mit dem Kommando :bcy:`led` und seinen Unterkommandos ab. Auch
   dieses ist eine direkte Abbildung auf die zugrundeliegende Zephyr API, siehe
   dazu auch :ref:`zephyr:led_api` in der Zephyr Dokumentation.

.. admonition:: Wissenswertes
   :class: worth-knowing note
   :collapsible:

   Die :ref:`Zephyr LED API <zephyr:led_api>` unterstützt so gut wie alle
   üblichen elektrischen Eigenschaften von LEDs. Das sind: *brightness*,
   *colors* (für RGB-LEDs) und *channels* (für LED-Streifen). Alle diese
   Eigenschaften sind für jede einzelne im System vorhandene LED individuell
   erreichbar, vorausgesetzt, die LEDs wurden auch im jeweiligen Devicetree
   für Zephyr definiert.

   In dem von dir benutzten MCU-Board, dem *Cytron – Maker Pi RP2040*, wurde
   das für nur genau eine einzige LED getan – die **Diagnose-LED an GP7**.
   Im Devicetree findet man folgende Definition dazu:

   .. code-block:: DTS

      / {
        pwm_leds: pwm_leds {
          compatible = "pwm-leds";
          status = "okay";

          pwm_led0: pwm_led_0 {
            pwms = <&pwm 7 PWM_MSEC(20) PWM_POLARITY_NORMAL>;
            label = "PWM_LED";
          };
        };
      };

   Demzufolge muss es in deiner Zephyr Laufzeitumgebung ein Gerät mit dem
   Namen ``pwm_leds`` geben. Dieses Gerät verwaltet nur eine einzelne LED,
   adressierbar über den Index '0'. Mit Hilfe einer PWM und des zugehörigen
   Treibers kann dann über die LED API die Helligkeit verändert werden. PWMs
   lernst du in :ref:`einer der folgenden Übungen <hs-cli-pwm-led>` kennen.

.. include:: bom.rsti
.. include:: assembly.rsti
.. include:: doing.rsti

.. vi: ft=rst ai ts=3 et sw=3 sta
