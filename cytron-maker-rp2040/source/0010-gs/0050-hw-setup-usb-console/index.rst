.. _gs-setup-usb-console:

USB-CDC/ACM Console am PC
#########################

.. sidebar:: Ziel

   Host-PC kommuniziert über eine USB-CDC/ACM Console mit dem MCU-Board.

.. topic:: Übersicht

   Du bist nun in der Lage, aus deinem *West Workspace* heraus auf deinem
   Host-PC eine *Zephyr UF2 Firmware* zu **bauen**, diese in dein *MCU-Board*
   zu **laden** und auf deinem *Hardwareaufbau* unter Zuhilfenahme eines
   *Terminalemulators* von deinem Host-PC aus zu **untersuchen**.

   Schauen wir uns aber den Hardwareaufbau etwas genauer an. Der angeschlossene
   USB Debug-Adapter ist für echtes Debugging essentiell wichtig, dient dir aber
   gegenwärtig nur als ein USB zu UART/RS232 Konverter. Hier können wir Dank
   Zephyr noch einmal gut optimieren.

   Zephyr unterstützt von Haus aus eine umfangreiche Treiber-Bibliothek für
   USB Geräte Klassen, z.B. Tastatur und Maus (HID), Massenspeicher (MSC), aber
   auch Kommunikation (CDC) für Netzwerk und serielle Schnittstellen. Letztere
   Klasse, genauer die **USB-CDC/ACM Klasse**, wollen wir nun mit einfachen
   Mitteln für die Zephyr Beispiele und dein MCU-Board aktivieren und nutzen.

   Damit entfällt der USB Debug-Adapter gänzlich aus deinem Hardwareaufbau. Über
   den **USB Anschluss, direkt am MCU-Board,** wird somit folgendes realisiert:

   - **Spannungsversorgung**
   - UF2 Firmware **laden** (über den on-chip UF2 Bootloader)
   - mit der Firmware **kommunizieren** (über USB Klasse)

   Erreichen werden wir das durch ein von Bridle bereitgestelltes **Zephyr
   Snippet** namens :file:`usb-console`. Dieser "Schnipsel" wird für dich alles
   Notwendige in deinem lokalen :file:`build`-Verzeichnis veranlassen, dass die
   Zephyr Console nicht mehr an die UART, sondern an die USB-CDC/ACM Klasse
   gebunden wird. Damit wird dann an deinem Host-PC eine andere (neue) ``COM``
   Schnittstelle auftauchen, mit der du nun aus deinem Terminalemulator heraus
   arbeiten wirst, dann aber **nicht mehr über die UART am USB Debug-Adapter**
   sondern **jetzt über die aktivierte USB-CDC/ACM Klasse am MCU-Board selbst**.

   .. seealso::

      - Zephyr :ref:`zephyr:snippets`
      - :ref:`bridle:snippet-usb-console`

.. rubric:: Wissenswertes

Mittlerweile besitzen fast alle Mikrocontroller eine on-chip Funktion für USB
Geräte. In aller Regel sind auch in Zephyr die Treiber für diese Funktion voll
integriert und durch die Hardwarebeschreibungen (Devicetree) der betreffenden
MCU-Boards für eine finale Aktivierung durch den Benutzer definiert. Das Zephyr
Treiber- und Hardware-Modell bietet also genügend Flexibilität, auf deklarativer
Ebene das Subsystem der Console an eine definierte serielle Schnittstelle zu
binden. Dabei spielt es keine Rolle, ob eine serielle Schnittstelle durch einen
Hardwaretreiber, wie im Fall der UART, oder durch den Endpunkt eines anderen
Subsystems oder :spelling:ignore:`Kommunikations-Stack`, wie im Fall der
USB-CDC/ACM Klasse, bereitgestellt wird.

Ohne an dieser Stelle zu tief in die Konzepte von Zephyr gehen zu können, ist es
wichtig zu verstehen, dass die finale Aktivierung durch den Benutzer nur durch
die richtig gesetzten Werte und Strukturen auf Kconfig und Devicetree Ebene
erwirkt wird. **Im dir vorliegenden West Workspace von Bridle** wird diese
Möglichkeit des Umschaltens, weg von der Console an einer UART hin zu einer
USB-CDC/ACM Klasse, durch ein sogenanntes **Zephyr Snippet** namens
:file:`usb-console` ermöglicht. Die folgende Tabelle stellt dir das Endergebnis
beider Möglichkeiten auf Kconfig und Devicetree Ebene gegenüber. Wie diese in
deinem :file:`build`-Verzeichnis aber zustande kommen, würde die Erklärung
jetzt und hier an dieser Stelle sprengen.

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
          # CONFIG_UART_LINE_CTRL is not set
          CONFIG_UART_INTERRUPT_DRIVEN=y

     - .. rubric:: Kconfig

       .. code-block:: Kconfig

          CONFIG_SERIAL=y
          CONFIG_CONSOLE=y

          CONFIG_UART_CONSOLE=y
          CONFIG_UART_LINE_CTRL=y
          CONFIG_UART_INTERRUPT_DRIVEN=y

          CONFIG_USB_DEVICE_STACK=y
          CONFIG_USB_DEVICE_VID=0x2e8a
          CONFIG_USB_DEVICE_PID=0x000a
          CONFIG_USB_DEVICE_INITIALIZE_AT_BOOT=y

   * - .. rubric:: Devicetree

       .. code-block:: DTS

          / { /* bind to UART */
            zephyr,console = &uart0;
          };

          /*
           * no comminication stack
           * involved, doesn't need
           * further setups
           */

          &uart0 {
            status = "okay"; /* ena. driver */
            pinctrl-0 = <&uart0_default>;
            pinctrl-names = "default";
          };

          uart0: uart@40034000 {
            compatible = /* UART on SoC */
                "raspberrypi,pico-uart";
          };

     - .. rubric:: Devicetree

       .. code-block:: DTS

          / { /* bind to USB-CDC/ACM */
            zephyr,console = &cdc_acm_uart;
          };

          &zephyr_udc0 {
            cdc_acm_uart: cdc_acm_uart {
              compatible = /* USB dev. class */
                 "zephyr,cdc-acm-uart";
            };

          zephyr_udc0: &usbd {
            status = "okay"; /* ena. driver */
            /* USB device doesn't need
             * a specific pin setup */
          };

          usbd: usbd@50100000 {
            compatible = /* USB dev. on SoC */
                 "raspberrypi,pico-usbd";
          };

.. include:: bom.rsti
.. include:: assembly.rsti
.. include:: doing.rsti

.. toctree::
   :caption: Zephyr Beispiele
   :maxdepth: 1
   :glob:

   samples/button
   samples/led_ws2812

.. vi: ft=rst ai ts=3 et sw=3 sta
