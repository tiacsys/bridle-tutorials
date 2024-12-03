.. _hs-cli-gpio:

Shell-Kommando ``gpio``
#######################

.. sidebar:: Ziel

   Beliebige LED und Benutzer-Taste manuell setzen
   :spelling:ignore:`bzw.` lesen.

.. topic:: Übersicht

   **General Purpose Input / Output** – oder kurz nur **GPIO** – ist die
   einfachsten Art und Weise, um **digitale Signale** in einem System zu
   beeinflussen. Das zugehörige Kommando :bcy:`gpio` mit seinen Unterkommandos
   ist eine direkte Abbildung auf die zugrundeliegende Zephyr API, siehe dazu
   auch :ref:`zephyr:gpio_api` in der Zephyr Dokumentation.

.. rubric:: Wissenswertes

Die :ref:`Zephyr GPIO API <zephyr:gpio_api>` unterstützt alle gegenwärtig am
Markt bekannten elektrischen Eigenschaften digitaler Ein- und Ausgänge. Das
sind: *Push/Pull*, *Pull-Up*, *Pull-Down*, *Open-Drain*, *Open-Source*,
*Level-High-Trigger*, *Level-Low-Trigger*, *Level-Both-Trigger*,
*Edge-Rising-Triger*, *Edge-Falling-Triger*, *Edge-Both-Triger*,
*Assert-Level-High* für den logischen Wert '1', *Assert-Level-Low* für den
logischen Wert '1' (Negation) und spezielle Funktionen wie *Disconnected*,
*Init-High* oder *Init-Low* und *Driver-Strength*. Alle diese Eigenschaften
sind für jedes einzelne GPIO in einem System durch das Shell Kommando
:bcy:`gpio` zugänglich.

.. include:: bom.rsti
.. include:: assembly.rsti
.. include:: doing.rsti

.. vi: ft=rst ai ts=3 et sw=3 sta
