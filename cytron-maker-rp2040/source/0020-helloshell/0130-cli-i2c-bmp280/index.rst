.. _hs-cli-i2c-bmp280:

Shell-Kommando ``i2c`` für BMP280
#################################

.. sidebar:: Ziel

   Registerzugriff auf den Drucksensor BMP280 laut Datenblatt.

.. topic:: Übersicht

   In dieser Übung wirst du mit Hilfe des Zephyr Shell Kommandos :bcy:`i2c` und
   dessen Unterkommandos gezielt I²C Nachrichten zusammenstellen. Du wirst dabei
   auf Ebene der Chip-Register des *Barometric Pressure Sensor* **BMP280**
   von Bosch operieren. Dabei wirst du die notwendigen Informationen aus dem
   Datenblatt des Sensors entnehmen und die Anweisungen für einen Messvorgang
   manuell durch eine Folge von Kommandos durchlaufen.

.. rst-class:: page-break

.. include:: bom.rsti
.. include:: assembly.rsti
.. include:: doing.rsti

.. target-notes::

.. vi: ft=rst ai ts=3 et sw=3 sta
