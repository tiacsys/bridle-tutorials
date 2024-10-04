Positionen
##########

.. figure:: /_images/refcards/cytron-maker-pi-rp2040-positions.*
   :name: cytron-maker-pi-rp2040-positions
   :align: center

   Funktionen und Komponenten am *Cytron – Maker Pi RP2040*

.. list-table:: Funktionen und Komponenten am *Cytron – Maker Pi RP2040*
   :class: longtable
   :align: center
   :width: 100%
   :widths: 50, 50

   * - 1.  | **USB Typ-B Anschluss**
           | USB1.1-Hosts und -Slave-Geräte
       #.  | **RESET-Taste**
       #.  | **BOOT-Taste**
           | bei RESET drücken, um in den UF2 Upload-Modus zu gelangen
       #.  | **Grove Port 1~7**
           | wahlweise UART, I²C, SPI, ADC, GPIO/PWM
       #.  | **WS2812B**
           | 2 RGB-LED an Spezial-PIO
       #.  | **Benutzer-Tasten**
       #.  | **Piezo-Summer**
           | 2,730kHz mit 80~87dB
       #.  | **Benutzer-LEDs (einfarbig)**
           | für Diagnosezwecke (keine Spannungsanzeige)
       #.  | **RP2040**
           | MCU: Dual Core, ARM Cortex-M0+
       #.  | **W25Q16JV**
           | NOR Flash: 2MB (permanent)
       #.  | **On/Off Schalter**
           | Haupt-Stromversorgungsschalter
     - 12. | **LiPo/-Ion Batterie-Anschluss**
           | MX1.25-Steckverbinder für 3,7-V-Lithium-Batterie;
             gleichzeitig Laden und Stromversorgung
       #.  | **Motor Spannungsklemme**
           | Schraubklemmenblock: für 3,6~6V Alkalibatterien oder Akkus
       #.  | **CT2105**
           | Lithium-Akku, einzellig, hochpräzises Ladegerät mit
             Überladeschutz für Spannung und Strom
       #.  | **MCP7381T-2ACI**
           | Lithium-Akku, einzellig, 500mA @ 4,20V Laderegler
       #.  | **MT3608** (oder **SY7208**)
           | 2A DC/DC Abwärts-/Aufwärtswandler, 1~1,2MHz
       #.  | **MX1515** (oder **MX1508**/**MX1208**)
           | 1,5A @ 2~10V Zweikanal H-Brücke für Bürsten-DC-Motoren
             mit 2,5A Spitze
       #.  | **DC-Motorklemmen**
       #.  | **Klemmen für Servomotoren**
       #.  | **DEBUG-Punkte** (SWD)

.. vi: ft=rst ai ts=3 et sw=3 sta
