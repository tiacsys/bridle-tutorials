.. _hs-cli-sensor-bmp280:

Shell-Kommando ``sensor`` für BMP280
####################################

.. sidebar:: Ziel

   Werte aus dem Drucksensor BMP280 holen.

.. topic:: Übersicht

   In dieser Übung lernst du den allgemeinen Umgang mit Sensoren unter Zephyr
   kennen. Helfen wird dir hierbei das Kommando :bcy:`sensor` mit seinen
   Unterkommandos. Dieses ist eine direkte Abbildung auf die zugrundeliegende
   Zephyr API, siehe dazu auch :ref:`zephyr:sensor` in der Zephyr Dokumentation.

   Du wirst dabei sehr schnell in die Zwänge von Zephyr geraten, deine Hardware
   genauer zu deklarieren. Das lösen wir gemeinsam auf und versuchen dich somit
   in kleinen Schritten näher an die neuen Konzepte von Zephyr heranzuführen.

   Du lernst das erste mal, einen :ref:`Devicetree Overlay <zephyr:use-dt-overlays>`
   zu schreiben und diesen über die Zephyr eigenen Mechaniken und Regeln bekannt
   zu machen. Da du in diesem einfachen Schritt nur eine *temporäre Veränderung*
   vornimmst, nutzt du die Umgebungsvariable :makevar:`EXTRA_DTC_OVERLAY_FILE`.
   Siehe dazu auch die folgenden Abschnitte in der Zephyr Dokumentation:

   - :ref:`Devicetree Overlay setzen <zephyr:set-devicetree-overlays>`
   - :ref:`Umgebungsvariablen beim Bauen <zephyr:important-build-vars>`

.. admonition:: Wissenswertes
   :class: worth-knowing note
   :collapsible:

   Die :ref:`Zephyr Sensor API <zephyr:sensor>` ist eine weitere abstrakte
   API und unterstützt die wichtigsten funktionalen Eigenschaften für die
   Beschaffung von Daten aus sensorischen Baugruppen. Das sind: *Channels*,
   *Values*, *Fetching*, *Async-Read*, *Triggers*,
   *Configuration-and-Attributes* und *Processing-Data*.

   Das von dir benutzte MCU-Board kennt für sich selbst keinerlei sensorische
   Bauelemente. Dennoch hattest du seit der Übung in :ref:`hs-cli-i2c-scan` mit
   zwei Sensoren für Umweltdaten gearbeitet, der **BMP280** und der **AHT20**.
   Dir wird aber noch in Erinnerung sein, dass du diese **beiden Bauelemente
   zusätzlich** an das MCU-Board **angeschlossen** hast. Das nennt man **eine
   Systemerweiterung** und es wäre naiv anzunehmen, dass deine aktuell
   vorliegende Firmware diese Systemerweiterung ohne weiteres dazutun
   irgendwie funktional unterstützt.

   Du wirst also **beim Erstellen deiner Zephyr UF2 Firmware** dafür sorgen
   müssen, dass **deine eigene und spezifische Systemumgebung mit Sensor**
   dem Build-Prozess mit :program:`west build …` **bekanntgegeben wird**.

.. include:: bom.rsti
.. include:: assembly.rsti
.. include:: doing.rsti

.. target-notes::

.. vi: ft=rst ai ts=3 et sw=3 sta
