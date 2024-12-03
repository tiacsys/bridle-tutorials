.. _gs-uf2-upload:

Programmierung über UF2 Bootloader
##################################

.. sidebar:: Ziel

   Dein MCU-Board mit der :spelling:ignore:`"Out-of-the-box"` (OOTB) Demo
   programmieren.

.. topic:: Übersicht

   Nun kannst du einen ersten Erfolg verbuchen, nach dem dein Arbeitsplatz dir
   einen Zugriff an das Innerste einer umfangreichen Firmware bietet. Wir wollen
   nun gemeinsam erkunden, wie man eine eigene Firmware in dein MCU-Board laden
   kann. Was liegt da näher, als die originale Demo-Firmware des Herstellers
   wieder aufzuspielen?

   Diese auch gerne *Out-of-the-box* oder kurz **OOTB** genannte Software ist
   im Falle des *Cytron – Maker Pi RP2040* auch ein Python-Derivat für kleine
   eingebettete Systeme namens **CircuitPython**. Dieses Derivat zeichnet sich
   im Gegensatz zu *MicroPython* durch ein verbessertes Benutzererlebnis aus
   und bietet auch das **dauerhafte Speichern von Python Scrips** in deinem
   MCU-Board.

   Die Schritte in dieser Übung versetzen dich also nicht nur in die Lage,
   **eigene Software in den Permanentspeicher (Flash) deines MCU-Boards zu
   laden**, sondern auch eine komplette *Werksrückstellung* zu erreichen. Das
   wird von Nerds auch gerne als *unbricking* bezeichnet.

   Wir werden sehen, wie elegant und einfach eine Programmierung des Flash ohne
   Spezialhilfsmittel wie *JTAG oder SWD In-Cirgut-Debuggern*, sondern durch
   einfaches *Drag and Drop* oder *Datei kopieren* ist. Dieser Vorgang ist
   Alltagsarbeit von Embedded Software Entwicklern (nicht nur Makern und
   Hobbyisten), wenn eigene in C/C++ oder Rust geschriebene Programme in den
   Flash am RP2040 geladen werden.

   .. attention::

      Im Folgenden wirst du eine auf *CircuitPython* basierende Anwendung
      auf deinem MCU-Board speichern. *CircuitPython* ist zwar eine Variante
      von *Micropython*, die aber den Flash-Speicher des RP2040 anders benutzt
      als *Micropython*. Es kann daher passieren, dass eine zuvor im Flash
      gespeicherte Micropython-Anwendung *unerwünschte Auswirkungen* auf
      eine CircuitPython-Anwendung, aber auch auf eine *Zephyr*-Anwendung
      haben kann.

      Aus diesem Grund werden wir zu Beginn und am Ende dieser Übung mit der
      speziellen **Flash Resetting UF2 Firmware** :file:`flash_nuke.uf2`
      sämtliche Inhalte im **Permanentspeicher (Flash) auf dem MCU-Board
      rückstandslos löschen**.

      Das ist nicht immer notwendig. Gut eingearbeitete Entwickler und Experten
      werden die Notwendigkeit und den exakten Zeitpunkt dieses Schrittes genau
      vorhersagen können. Wir wollen dir aber die Durchführung deiner
      Experimente uneingeschränkt garantieren und mit diesem Vorgehen die am
      häufigsten anzutreffenden systematischen Fehler vermeiden.

.. rubric:: Wissenswertes

Die **OOTB Demo Software** setzt sich nun aus **zwei Teilen** zusammen.

Zum Ersten muss das Python-Derivat *CircuitPython* als nativ programmierte
Firmware in das MCU-Board, genauer gesagt in den Flash am RP2040, geladen
werden. Hierfür besitzt der RP2040, so wie alle modernen Mikrocontroller,
einen unveränderlichen (maskenprogrammierten) **First Stage Bootloader** in
seinem On-chip ROM. Dessen Funktionalität wird aktiv, wenn zum Zeitpunkt
eines Systemresets (Strom einschalten oder ``RESET`` Leitung aktiviert)
entweder der am RP2040 angeschlossene Flash Speicher leer, also keine
Firmware auf dem MCU-Board ist, oder die dafür vorgesehene ``BOOT`` Taste
auf deinem MCU-Board während des Einschaltens gedrückt ist. Der Bootloader
selbst folgt dann dem **UF2 Standardprotokoll**, wie es von Microsoft
ursprünglich für die Online-Lernplattform *Make & Code* spezifiziert und
entwickelt wurde.

Der zweite Teil der OOTB Demo Software besteht aus ein paar wenigen Kilobyte
reiner Python Dateien und müssen "nachinstalliert" werden. Hier bietet
*CircuitPython*, so wie zuvor der On-chip UF2 (First Stage) Bootloader,
ebenfalls die Möglichkeit, Dateien per ``Drag-and-Drop`` von deinem Host-PC in
den Flash-Speicher des RP2040 zu kopieren.

.. include:: bom.rsti
.. include:: assembly.rsti
.. include:: doing.rsti

.. include:: yourspace.rsti

.. vi: ft=rst ai ts=3 et sw=3 sta
