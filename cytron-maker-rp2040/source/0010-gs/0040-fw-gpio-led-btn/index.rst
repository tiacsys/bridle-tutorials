.. _gs-gpio-led-btn:

Testen der Benutzer-LED und Taste
=================================

.. sidebar:: Ziel

   Die Benutzer-LED blinkt, verändert ihre Helligkeit über die Zeit oder
   wird durch die Benutzer-Taste geschaltet.

.. topic:: Übersicht

   Herzlichen Glückwunsch! Dein Arbeitsplatz ist nun alltagstauglich, abgesehen
   von der fehlenden Möglichkeit zu debuggen. Das ist aber ein Kapitel für sich
   und füllt ein weiteres Tutorial.

   Gehe davon aus, dass dieser Aufbau für eine professionelle Arbeit mit Zephyr
   ausreicht und so auch millionenfach zum Einsatz kommt. Du kannst bereits:

   - UF2 Firmware in den Permanentspeicher (Flash) laden, und
   - und mit der Firmware über einen UART kommunizieren.

   In dieser Übung wollen wir den Arbeitsablauf für die Entwicklung von Zephyr
   Applikationen auf deinem Host-PC erlernen. Auch hier werden wir zunächst nur
   die absoluten Grundlagen kennenlernen sowie Begriffe, Verfahren und Vorgehen
   klären und nicht gleich die großen "Hacks" bewegen.

   Was liegt da näher, als sich des umfangreichen Fundus an Beispielen von
   Zephyr direkt zu bedienen? In dieser Übung wirst du deine ersten Erfahrungen
   mit den folgenden drei Beispielen sammeln:

   :Blinky:
      | *"… This sample blinks an LED forever using the GPIO API. …"*
      | Dokumentation: :doc:`zephyr:samples/basic/blinky/README`
        (:doc:`upstream <zephyr-us:samples/basic/blinky/README>`)

   :Fade:
      | *"… This sample “fades” a LED using the PWM API. …"*
      | Dokumentation: :doc:`zephyr:samples/basic/fade_led/README`
        (:doc:`upstream <zephyr-us:samples/basic/fade_led/README>`)

   :Button:
      | *"… This sample will light up an LED when pressing a button. …"*
      | Dokumentation: :doc:`zephyr:samples/basic/button/README`
        (:doc:`upstream <zephyr-us:samples/basic/button/README>`)

   .. attention::

      Wenn du die Übungen mit uns durchführst, bekommst du einen Zugang zu
      einer **virtuellen VS Code Entwicklungsumgebung** auf unserer Cloud
      Infrastruktur gestellt. Dieser ist **personalisiert**. Benutzen wirst
      du diese **in deinem WEB-Browser**!

      Alternativ, zum Beispiel für eigene Experimente, kannst du dir eine
      solche Umgebung auch auf deinem eigenen Host-PC einrichten.
      **Aber Achtung:** wir empfehlen dir eindringlich die Arbeit unter Linux.
      Anleitungen dazu findest du in der
      :ref:`Bridle Dokumentation <bridle:gs_installing>` und im
      :ref:`Zephyr Getting Started Guide <zephyr:getting_started>`

.. rubric:: Wissenswertes

Wenn du dich zunehmend mit Zephyr beschäftigst, wirst du lernen, dass hinter dem
:ref:`Zephyr Projekt <zephyr:zephyr-home>` weit mehr als nur ein RTOS für 32-bit
Mikrocontroller und Computer steckt. Vielmehr handelt es sich um ein ganzes
Ökosystem an Softwarequellen, Bibliotheken, Subsystemen, Werkzeugen, Regeln und
Projektstrukturen sowie der dazugehörigen Dokumentation.
Das :ref:`Zephyr Glossar <zephyr:glossary>` bietet dir zu den wichtigsten, auch
von uns hier benutzten, Begriffen einen ersten kompakten Überblick. Wir wollen
an dieser Stelle die wichtigsten Begriffe und damit verbundenen Methoden
:spelling:ignore:`bzw.` Funktionen kurz erläutern.

:Applikation :spelling:ignore:`vs.` Board:
   Zephyr unterscheidet strikt zwischen (1) den Softwarequellen für eine
   :term:`Applikation <zephyr:application>` und (2) den hardwarespezifischen
   Softwarequellen, die allgemein einem :term:`Board <zephyr:board>`
   zugeordnet sind. Diese hardwarespezifische Software kann nicht alleinstehend
   ausgeführt werden. Stattdessen wird immer ein applikativer Softwareteil
   benötigt, eine Applikation, auch wenn diese nur aus einer leeren ``main()``
   Funktion besteht. Eine **gewöhliche Zephyr Firmware** muss unter **Benennung
   eines Boards und einer Applikation** übersetzt werden. Die Dokumentation von
   Bridle und Zephyr pflegt Listen über unterstützte Boards und
   Beispielapplikationen:

   #. Beispiele und Demonstrationen:

      - von :ref:`Bridle unterstützt<bridle:examples>`
      - von :ref:`Bridle's Zephyr unterstützt<zephyr:samples-and-demos>`
      - von :ref:`Zephyr upstream unterstützt<zephyr-us:samples-and-demos>`

   #. Boards:

      - von :ref:`Bridle unterstützt<bridle:boards>`
      - von :ref:`Bridle's Zephyr unterstützt<zephyr:boards>`
      - von :ref:`Zephyr upstream unterstützt<zephyr-us:boards>`

:West Meta Tool:
   Softwareentwicklung wird immer durch Technologie getrieben. Ein Informatiker,
   also auch du, muss die folgenden Prozessschritte aus der Softwaretechnologie
   kennen und in seiner eigenen Produktentwicklung zuordnen können:

   - Software Configuration Management (SCM) – Baselines, Revisionen
   - Software Capability Management – Umfang und Variation (feature toggle)
   - Pre-processing – Vorbereitung von Quellcode, Konverter
   - Source Compilation – Assembler Mnemonic oder Bytecode generieren
   - Machine Code Assembly – nativ ausführbare Binär-Artefakte
   - Linker Stage – Binär-Artefakte zu finaler Firmware
   - Deployment, Provisioning – Auslieferung und Parametrisierung
   - Testing – Unit- oder Integrationstest
   - Life-Cycle-Management
   - Documentation

   Keine Angst, wir tauchen an dieser Stelle nicht in diesen technologischen
   Makrokosmos ein. Dir soll nur bewusst sein, dass sich hinter all diesen
   essentiell wichtigen und **notwendigen Schritten** eine Reihe
   **bewährter Verfahren (best practices)** dazu gehörende **Werkzeuge und
   Vorgehensmodelle** etabliert haben. Diese variieren gegebenenfalls je nach
   Art deiner Applikation und der Zielarchitektur (Hardware-Vorgaben).

   Jeder Punkt für sich stellt prinzipbedingt verschiedene Schnittstellen für
   die Bedienung bereit. Diese Schnittstellen müssen erlernt werden, was zum
   Teil eine längerfristige und mit unter frustrierende Angelegenheit sein
   kann (z.B. GNU C/C++ :spelling:ignore:`vs.` LLVM/Clang oder Doxygen
   :spelling:ignore:`vs.` Sphinx).

   Das Zephyr-Ökosystem umfasst unter anderem das **Meta-Werkzeug**
   :program:`west`, das die oben angesprochenen Prozessschritte unterstützt.
   Dir wird dieses Werkzeug im Folgenden begegnen, um:

   - eine Zephyr Firmware "zu bauen": :program:`west build …`
   - eine Zephyr Firmware "auszuliefern": :program:`west flash …`

   Darüber hinaus gibt es viele weitere *Standardeinstiege* über West, so
   z.B. :program:`west manifest` für das Thema SCM oder :program:`west twister`
   für Softwaretests, egal welchen Typs.

   Es sei an dieser Stelle nur kurz auf die entsprechende Passage in der Zephyr
   Dokumentation verwiesen: :ref:`zephyr:getting_started_run_sample`.

:West Workspace:
   Das ist **dein lokaler Arbeitsbereich in einem Verzeichnis auf** deinem
   Host-PC. Genau diesen wirst du mit **unserer virtuellen VS Code Instanz**
   automatisch erhalten – ohne Setup oder langwierigen Downloads. Wenn du
   die Übungen einmal alleine durchgehen möchtest und du dir eine eigene
   Entwicklungsumgebung für Zephyr und Bridle einrichten musst, wirst du
   dir mit Hilfe von :program:`west manifest` genau jenen Arbeitsbereich
   (West Workspace) selbst aufbauen und verwalten.

.. include:: bom.rsti
.. include:: assembly.rsti
.. include:: doing.rsti

.. toctree::
   :caption: Zephyr Beispiele
   :maxdepth: 1
   :glob:

   samples/blinky
   samples/fade
   samples/button

.. vi: ft=rst ai ts=3 et sw=3 sta
