.. _demo-zephyr-driver-adc:

ADC Werte auslesen und anzeigen
###############################

.. sidebar:: Ziel

   Übersetzen, programmieren und spielen mit dem Zephyr Treiber Beispiel
   :doc:`zephyr:samples/drivers/adc/README`

.. topic:: Übersicht

   Erinnere dich bitte an die :ref:`zurückliegende Übung <hs-cli-adc>`, als du
   mit dem Zephyr Shell Kommando :bcy:`adc` am ADC Kanal 2 (**ADC2**) die über
   dem Potentiometer am Steckverbinder **GROVE 7** abfallende **Spannung Uₐ₂**
   manuell gemessen hattest. Nun werden wir ein Zephyr Standard Beispiel für
   ADC Treiber dazu benutzen. Dieses liest permanent die aktuellen numerischen
   Werte aus *"deklarierten"* ADC Kanälen und gibt sie zusammen mit der
   errechneten Spannung an der Zephyr Console aus. Du wirst nun auch hier einen
   (weiteren, neuen) **speziellen Devicetree Overlay** mit den notwendigen
   HW-Deklarationen schreiben.

.. include:: bom.rsti
.. include:: assembly.rsti
.. include:: doing.rsti

.. vi: ft=rst ai ts=3 et sw=3 sta
