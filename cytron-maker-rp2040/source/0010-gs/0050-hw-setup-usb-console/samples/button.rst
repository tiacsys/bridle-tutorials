Button über USB-CDC/ACM Console
*******************************

**Vergewissere** dich zunächst, das das :program:`Button` Beispiel aus
:ref:`der Übung zuvor <gs-gpio-led-btn>` weiterhin **in deinem bestehenden
Hardwareaufbau funktioniert**. Im Zweifel wiederholst du diesen kleinen
Teil der vorherigen Übung nochmal.

-----------------------------------------------------------------------------

Durchlaufe nun wieder den Dreiklang: (1) bauen, (2) laden, (3) beobachten.

-----------------------------------------------------------------------------

Zephyr UF2 Firmware aus dem Zephyr Beispiel ``button`` bauen und laden
======================================================================

Hole deine **Online-Sitzung von VS Code** in den Vordergrund.

-----------------------------------------------------------------------------

.. ..... BUILD ..............................................................

.. image:: /_images/symbol-coder-server-bl.*
   :class: sidecar

.. compound::

   **Baue die Zephyr UF2 Firmware** erneut, **jetzt aber mit** dem
   zusätzlichen Parameter :program:`-S usb-console` beim Aufruf von
   :program:`west build …`, gib ein:

   .. parsed-literal::
      :class: code

      west build -p -b |BOARD|        **-S usb-console** \\
                 zephyr/samples/basic/button

-----------------------------------------------------------------------------

.. ..... FLASH ..............................................................

.. image:: /_images/symbol-rp2040-uf2-rd.*
   :class: sidecar

**Lade** dir die **Zephyr UF2 Firmware** herunter und lade diese anschließend
**auf dein MCU-Board**.

Zephyr UF2 Firmware aus dem Zephyr Beispiel ``button`` benutzen
===============================================================

Hole deinen **Terminalemulator** in den Vordergrund und **öffne eine neue
Verbindung** über die neu entstandene serielle Schnittstelle (.z.B. ``COM4``).

-----------------------------------------------------------------------------

.. ..... ACTION .............................................................

.. image:: /_images/symbol-observe-or.*
   :class: sidecar

.. compound::

   **Beobachte die Ausgaben**, folgendes muss (wie zuvor über den USB Debug-\
   Adapter) jetzt über die direkte USB Verbindung (den Zephyr USB-CDC/ACM
   Klassentreiber) zu sehen sein:

   .. parsed-literal::
      :class: code

      \*\*\*\*\* delaying boot 4000ms (per build configuration) \*\*\*\*\*
      \*\*\* Booting Zephyr OS build zephyr-v3.6… (delayed boot 4000ms) \*\*\*
      Set up button at gpio@40014000 pin 20
      Set up LED at gpio@40014000 pin 7
      Press the button
      Button pressed at 1750227124
      Button pressed at 99850305
      Button pressed at 4185249554
      Button pressed at 4720712

Die **Benutzer-LED an GP7 leuchtet, wenn**
die **Benutzer-Taste an GP20 gedrückt** ist.

Hardwareaufbau verändern
========================

**Baue** nun an deinem Hardwareaufbau **den USB Debug-Adapter ab**, den
*Raspberry Pi – Debug Probe*, das kleine USB Gerät mit transparentem Gehäuse
und mit dem orangenen USB-Kabel. Du musst jetzt den neuen Aufbau aus
:numref:`gs-hw-setup-usb-console` erhalten.

-----------------------------------------------------------------------------

.. ..... ACTION .............................................................

.. image:: /_images/symbol-observe-or.*
   :class: sidecar

Gehe zurück in die eben noch von dir benutze Sitzung deines **Terminalemulators**
und **beobachte weiterhin die Ausgaben**. Diese müssen unverändert an dieser
Schnittstelle erscheinen, drücke im Zweifel auch noch mal die ``RST`` Taste.

Setze die Übung erst fort, wenn du dir sicher bist, dass die USB-CDC/ACM Console
für dich funktioniert. Ziehe zur Not uns Mentoren zu Rate.

.. include:: yourspace-short.rsti

.. admonition:: Nur für Mentoren
   :class: red-border bug
   :collapsible:

   :download:`GS-cytron_maker_pi_rp2040-usbcons-button.uf2
   </_assets/GS-cytron_maker_pi_rp2040-usbcons-button.uf2>`
   – als Not-Backup gedacht!

.. vi: ft=rst ai ts=3 et sw=3 sta
