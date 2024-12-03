.. _hs-cli-i2c-scan:

Shell-Kommando ``i2c``
######################

.. sidebar:: Ziel

   Rudimentäre Zugriffe auf den I²C Bus, finden von Geräten.

.. topic:: Übersicht

   Der **Inter-Integrated-Circuit Bus** – kurz nur **I²C** oder **IIC** Bus –
   ist ein seit den 1980er Jahren fest etablierter digitaler Kommunikationsbus
   zwischen verschiedenen Schaltkreisen innerhalb technischer Geräte. Für die
   Anbindung digitaler Sensoren, Aktoren und vielem mehr ist der Bus bis heute
   im Einsatz. Zephyr stellt dir für die Arbeit mit I²C Geräten das zugehörige
   Kommando :bcy:`i2c` mit seinen Unterkommandos bereit. Dieses ist eine direkte
   Abbildung auf die zugrundeliegende Zephyr API, siehe dazu auch
   :ref:`zephyr:i2c_api` in der Zephyr Dokumentation.

   Obwohl vom Bus-Standard nie vorgesehen und bis heute auch nicht spezifiziert,
   kann das Bus-Protokoll für eine Art *"autodetection"* :spelling:ignore:`bzw.`
   *"enumeration"* der Bus-Teilnehmer genutzt werden. Dieser **"I²C Bus Scan"**
   ist **nur Bestandteil des Zephyr Shell Kommandos** :bcy:`i2c` und **nicht der
   Zephyr I²C API**.

   Du wirst in dieser Übung zunächst deine I²C Bus Struktur experimentell
   erforschen, bevor du in der :ref:`folgenden Übung <hs-cli-i2c-bmp280>` auf
   die Rohdaten in einem I²C Gerät zugreifen wirst.

.. rubric:: Wissenswertes

Die :ref:`Zephyr I²C API <zephyr:i2c_api>` unterstützt die wichtigsten
funktionalen Eigenschaften des I²C Bus-Protokolls. Das sind: *Speed-Standard*,
*Speed-Fast*, *Speed-Fast-Plus*, *Speed-High*, *Speed-Ultra*, *Address-10Bit*,
*Transfer-Read*, *Transfer-Write*, *Transfer-Write-Read* und *Bus-Recover*.
Alle diese Eigenschaften sind für jeden einzelnen I²C Bus in einem System durch
das Shell Kommando :bcy:`i2c` zugänglich.

Das von dir benutzte MCU-Board ist mit dem Mikrocontroller **RP2040**
ausgestattet und bietet dir insgesamt 2 I²C Busse. Der erste davon ist am
Steckverbinder **GROVE 4** herausgeführt. Wie bei Bussen üblich, wirst du dort
verschiedene I²C Geräte anschließen können. Der I²C Bus wird zusammen mit den
Einstellungen für den Betrieb (z.B. Geschwindigkeit) im Devicetree definiert.

Hier ein Auszug:

.. code-block:: DTS

   &i2c0 {
     status = "okay";
     pinctrl-0 = <&i2c0_makerpi>;
     pinctrl-names = "default";
     clock-frequency = <I2C_BITRATE_STANDARD>;
   };

.. rst-class:: page-break

   .. only:: rinoh

      |nbsp|
.. QUIRKS: Only with this dummy paragraph, the special rinohtype class
   'page-break-paragraph' react as expected. But the '.. code-block::' directive
   should also be handled as a 'ParagraphStyle' and trigger that class, But
   it doesn't work as expected. Fix this later!

.. code-block:: DTS

   &pinctrl {
     i2c0_makerpi: i2c0_makerpi {
       group1617_i2c {
         pinmux = <I2C0_SDA_P16>, /* GP16: I2C0_SDA */
                  <I2C0_SCL_P17>; /* GP17: I2C0_SCL */
         bias-pull-up;
         input-enable;
         input-schmitt-enable;
       };
     };
   };

.. include:: bom.rsti
.. include:: assembly.rsti
.. include:: doing.rsti

.. target-notes::

.. vi: ft=rst ai ts=3 et sw=3 sta
