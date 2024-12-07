.. _hs-cli-adc:

Shell-Kommando ``adc``
######################

.. sidebar:: Ziel

   Kanal einrichten und Wert vom Potentiometer einlesen.

.. topic:: Übersicht

   **Analog to Digital Converter** – oder kurz nur **ADC** – dient der
   Umsetzung analoger Eingangssignale in einen digitalen Datenstrom. Sie setzt
   zeit- und wert-kontinuierliche Signale in zeit- und wert-diskrete Folgen
   von natürlichen ganzen Zahlen um, eine numerische Quantisierung. Das
   zugehörige Kommando :bcy:`adc` mit seinen Unterkommandos ist eine direkte
   Abbildung auf die zugrundeliegende Zephyr API, siehe dazu auch
   :ref:`zephyr:adc_api` in der Zephyr Dokumentation.

.. admonition:: Wissenswertes
   :class: worth-knowing note
   :collapsible:

   Die :ref:`Zephyr ADC API <zephyr:adc_api>` unterstützt alle gegenwärtig
   am Markt bekannten funktionalen Eigenschaften von ADCs. Das sind:
   *Acquisition-Resolution*, *Acquisition-Reference*, *Acquisition-Time*,
   *Acquisition-Oversampling*, *Signal-Gain*, *Signal-Negation*,
   *Signal-Differential* und *Multiple-Channels*. Alle diese Eigenschaften
   sind für jede einzelne ADC in einem System durch das Shell Kommando
   :bcy:`adc` zugänglich, vorausgesetzt, die ADCs wurden auch im jeweiligen
   Devicetree für Zephyr definiert. In dem von dir benutzten MCU-Board, dem
   *Cytron – Maker Pi RP2040*, wurde das für die ADC im Mikrocontroller getan.
   Im Devicetree findet man folgende Definition dazu:

   .. code-block:: DTS

      &adc {
        status = "okay";
        pinctrl-0 = <&adc_makerpi>;
        pinctrl-names = "default";
      };

   .. code-block:: DTS

      &pinctrl {
        adc_makerpi: adc_makerpi {
          group0123_adc {
            pinmux = <ADC_CH0_P26>, /* GP26: ADC_CH0 */
                     <ADC_CH1_P27>, /* GP27: ADC_CH1 */
                     <ADC_CH2_P28>, /* GP28: ADC_CH2 */
                     <ADC_CH3_P29>; /* GP29: ADC_CH3 */
            input-enable;
          };
        };
      };

.. include:: bom.rsti
.. include:: assembly.rsti
.. include:: doing.rsti

.. vi: ft=rst ai ts=3 et sw=3 sta
