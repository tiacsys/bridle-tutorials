.. _hs-build-upload:

Shell-Zugriff einrichten
########################

.. sidebar:: Ziel

   Das Bridle Beispiel ``helloshell`` wird gebaut und hochgeladen.

.. topic:: Übersicht

   Nun werden wir deutlich schneller! Die Grundlagen sind gelegt und mit dem
   gelernten Handwerkszeug aus dem :ref:`vorherigen Kapitel <gettingstarted>`
   werden wir in dieser "kurzen" Übung:

   - deinen Hardwareaufbau mit der USB-CDC/ACM Console mit zusätzlichen
     Komponenten erweitern
   - das Bridle Beispiel ":ref:`bridle:helloshell`" (``helloshell``) bauen,
     hochladen und kennenlernen

   Dieses Beispiel basiert auf der Zephyr :ref:`zephyr:shell_api`, einem
   speziellen :ref:`Zephyr OS Service <zephyr:os_services>`. Es wird durch
   Bridle bereitgestellt und kann dir eine Vorlage für deine Erweiterung der
   Zephyr Shell mit eigenen Kommandos dienen, solltest du diese einmal in
   deinen eigenen Produkten einbauen wollen oder müssen.

   Wir werden ein sehr simples "Bridle Shell Kommando" gleich im Anschluss, in
   der nächsten Übung, kennenlernen. Sei gespannt, du wirst in den restlichen
   Übungen dieses Kapitels nur noch **mit der Zephyr Shell in deinem MCU-Board
   über deinen Terminalemulator auf deinem Host-PC arbeiten**.

.. admonition:: Wissenswertes
   :class: worth-knowing note
   :collapsible:

   Die Zephyr :ref:`zephyr:shell_api` ist nur einer von vielen sehr nützlichen
   Zephyr :ref:`zephyr:os_services`. Die wichtigsten und sehr oft benutzen
   Dienste wären zum Beispiel:

   - :ref:`zephyr:logging_api` und :ref:`zephyr:shell_api`
   - :ref:`zephyr:settings_api` und :ref:`zephyr:device_mgmt`
   - :ref:`zephyr:ipc_service_api` und :ref:`zephyr:zbus`
   - :ref:`zephyr:storage_reference` und :ref:`zephyr:file_system_api`
   - :ref:`zephyr:cryptography`
   - :ref:`zephyr:sensing` – *Sensor Fusion* (extrem neu und nicht final)
   - :ref:`zephyr:rtio` (extrem neu und nicht final)

   Die meisten davon basieren mehr oder weniger Vorlagen aus der Linux Kernel
   Entwicklung und folgen auch diesen Prinzipien.

   Nicht an dieser Stelle, aber in späteren Übungen werden wir tiefer in die API
   der Zephyr Shell eintauchen. Wir werden erst dann die Vorzüge dieses Dienstes
   wirklich schätzen lernen, bietet die Shell doch von Haus aus schon:

   - Hilfesystem
   - CLI-History
   - TAB-Completion
   - Unterkommandos (statisch oder dynamisch)
   - POSIX Argument Parsing (kurz oder lang oder beides)

   Noch ein Wort zu den Begriffen Console und Shell. Beide müssen deutlich
   voneinander unterschieden werde. **Die Console ist nicht die Shell** und
   braucht auch keine Shell. Die **Console** ist ein Begriff für eine
   Systemschnittstelle; wortwörtlich eine **"Schnittstelle für das System"**!
   Sie wird und darf nicht als Teil einer Applikation gesehen werden. Sollte
   die Console also durch reale Hardware, also eine u.U. nur einmalig
   vorhandene Ressource realisiert sein, dann darf eine Applikationsschicht
   diese Hardwareeinheit nicht mehr für ihre Zweck benutzen (z.B. ein
   proprietäres Protokoll mit einem Host-PC sprechen, weil ja gerade so schön
   über USB da eine Verbindung existiert). Andersherum gilt natürlich auch,
   **die Shell ist nicht die Console**, aber eine Shell kann von einer Console
   abhängen und diese aktiv nutzen. Dann ist die Shell aber nicht die einzige
   Instanz, welche mit der Console innerhalb der Zephyr Dienste interagiert.
   Das können auch gänzlich andere Teile einer Zephyr Firmware sein.

   .. rubric:: Dazu ein einfaches Beispiel.

   In deinem aktuellen Hardwareaufbau ist dir nun sicher in der letzten Übung
   bereits aufgefallen, dass der USB Treiber für den Raspberry Pi RP2040 ab
   und zu eine "Art Warn-Nachricht" auf die Console schreibt, also z.B.:

   .. parsed-literal::
      :class: code

      [00:00:00.288,000] :yl:`<wrn> udc_rpi: BUS RESET`

   Technisch ist das richtig und erwartet, es ist ein *USB Bus Reset* den der
   USB-Host (also dein Host-PC) auslösen muss, wenn ein neues Gerät am Bus
   auftaucht. Aber wie kommt das nun aus dem Treiber auf deine Console? Schuld
   daran ist der aktivierte Zephyr :ref:`zephyr:logging_api` Dienst.

   Warum erwähnen wir nun hier, wo es doch um die Shell gehen soll, auch noch
   den Logging Dienst? Es gibt die vorhin beschriebene Abhängigkeit der Shell
   mit dem Logging über die Console. Konkret ist das auf den Strukturen von
   :ref:`Kconfig <zephyr:kconfig>` und :ref:`Devicetree <zephyr:devicetree>`
   folgendermaßen abgebildet:

   .. list-table::
      :align: center
      :width: 100%
      :widths: 50, 50
      :header-rows: 1

      * - UART Treiber (:spelling:ignore:`Rx/Tx`)
        - USB-CDC/ACM Klasse (Modem)

      * - .. rubric:: Kconfig

          .. code-block:: Kconfig

             CONFIG_SERIAL=y
             CONFIG_CONSOLE=y

             CONFIG_UART_CONSOLE=y

        - .. rubric:: Kconfig

          .. code-block:: Kconfig

             CONFIG_SERIAL=y
             CONFIG_CONSOLE=y
             CONFIG_USB_DEVICE_STACK=y
             CONFIG_UART_CONSOLE=y

      * - .. rubric:: Devicetree

          .. code-block:: DTS

             / { /* bind to UART */
               zephyr,console = &uart0;
               zephyr,shell-uart = &uart0;
             };

        - .. rubric:: Devicetree

          .. code-block:: DTS

             / { /* bind to USB-CDC/ACM */
               zephyr,console = &cdc_acm_uart;
               zephyr,shell-uart = &cdc_acm_uart;
             };

   Damit ist es also ebenso **denkbar**, dass die Zephyr *Shell*
   **nicht zusammen** mit dem *Logging* **an derselben Console**
   benutzt werden kann.

   Behandeln wollen wir den Logging Dienst auch erst in späteren Übungen.

.. include:: bom.rsti
.. include:: assembly.rsti
.. include:: doing.rsti

.. vi: ft=rst ai ts=3 et sw=3 sta
