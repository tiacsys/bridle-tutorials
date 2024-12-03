.. _demo-zephyr-sensor-bme280:

BME280 Sensor Werte auslesen und anzeigen
#########################################

.. sidebar:: Ziel

   Übersetzen, programmieren und spielen mit dem Zephyr Sensor Beispiel
   :doc:`zephyr:samples/sensor/bme280/README`

.. topic:: Übersicht

   In der :ref:`zurückliegende Übung <hs-cli-sensor-bmp280>` hattest du dir ein
   erstes eigenes Devicetree Overlay für die Deklaration des **Drucksensors
   BMP280** am I²C Bus deines MCU-Boards geschrieben. Das liegt in deinem West
   Workspace als Datei :file:`grove_i2c-bmp280@77.overlay`. Du wirst nun in
   dieser Übung erkennen, dass ein **Devicetree Overlay nicht an eine einzige
   Zephyr Applikation gebunden** ist. Diese können immer benutzt werden, wenn
   sie zu den restlichen Deklarationen passen. Da du ja nicht vor hast, jetzt
   dein MCU-Board auszutauschen, ist das immer noch garantiert. Du wirst nun
   ein Zephyr Standard Beispiel zusammen mit deinem eigenen Devicetree Overlay
   benutzen, um permanent aus dem angeschlossenen Drucksensor BMP280 Werte
   auszulesen und an der Zephyr Console ausgeben zu lassen.

.. rubric:: Wissenswertes

Du hast bereits gelernt, dass der **Drucksensor BMP280** identisch zu seinem
größeren und teureren Bruder, dem **Umweltsensor BME280**, ist. Selbst der in
Zephyr existierende Sensor-Treiber ist für beide Bauelement exakt der selbe.
Dieser ignoriert nur im Falle eines BM\ **P**\ 280 den Kanal für die nicht
vorhandene Feuchtigkeitsmessung.

Aber: Das von Zephyr bereitgestellte Standard Beispiel, welches du in dieser
Übung benutzen wirst, achtet nicht auf diesen Unterschied und geht strikt von
einem angeschlossenen Umweltsensor BM\ **E**\ 280 aus. Wundere dich also nicht,
dass du nun einen *"komischen"* Wert für die relative Luftfeuchtigkeit angezeigt
bekommst. Dieser bleibt immer gleich und entspricht dem Wert der C-Speicher-\
Initialisierung.

**Es ist aber ein weiteres Beispiel für die Robustheit der Zephyr API
Architektur.** Wenn *"unmögliche"* API Aufrufe zum Einsatz kommen, führt das
nicht zwangsläufig zum Scheitern. Weder stürzt Software im Zielsystem ohne
Kontrolle ab, noch wird ein Entwickler daran gehindert, eine Applikation zu
übersetzen. **Eine Zephyr API ist ein Stück weit "selbstsicher".**

.. include:: bom.rsti
.. include:: assembly.rsti
.. include:: doing.rsti

.. vi: ft=rst ai ts=3 et sw=3 sta
