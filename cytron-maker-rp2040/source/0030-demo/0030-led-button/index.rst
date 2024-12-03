.. _demo-zephyr-basic-led-button:

Externe LED und Taste mit Standard Demos
########################################

.. sidebar:: Ziel

   Übersetzen, programmieren und spielen mit den Zephyr Basic Beispielen:

   - :doc:`zephyr:samples/basic/blinky/README`
   - :doc:`zephyr:samples/basic/blinky_pwm/README`
   - :doc:`zephyr:samples/basic/fade_led/README`
   - :doc:`zephyr:samples/basic/button/README`

.. topic:: Übersicht

   In dieser Übung nehmen wir noch einmal kurz das Ergebnis aus der
   :ref:`zurückliegenden Übung <hs-cli-pwm-led>` mit den PWM Zugriffen auf LEDs
   auf. Du hattest gelernt, dass die **externe LED** am Steckverbinder
   **GROVE 3** nur durch einen erweiterten Devicetree über den **PWM Kanal 5**
   erreicht werden kann. Du hattest auch gelernt, dass dies nur mit der
   Einführung der zusätzlichen Abstraktion von :ref:`Shields <zephyr:shields>`
   sinnvoll ist – das ist auch weiterhin so. Mit einer solchen Abstraktion
   würden aber auch :ref:`Devicetree Overlays <zephyr:use-dt-overlays>`
   entstehen und genau dieses Konzept hast du nun schon mehrmals angewandt.

   Wollen wir der Einführung von Shields für die externe LED und Taste in dieser
   Übung ein wenig vorweg greifen und schauen uns an, wie die damit entstehenden
   Devicetree Fragmente aussehen könnten.

.. include:: bom.rsti
.. include:: assembly.rsti
.. include:: doing.rsti

.. vi: ft=rst ai ts=3 et sw=3 sta
