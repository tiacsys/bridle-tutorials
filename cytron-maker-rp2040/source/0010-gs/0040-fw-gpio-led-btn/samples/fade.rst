Fade Beispiel über UART Console
###############################

Durchlaufe den bekannten Dreiklang: (1) bauen, (2) laden, (3) beobachten.

-----------------------------------------------------------------------------

.. ..... BUILD ..............................................................

.. image:: /_images/symbol-coder-server-bl.*
   :class: sidecar

Hole deine **Online-Sitzung von VS Code** in den Vordergrund und **baue die
Zephyr UF2 Firmware**, gib ein::

   west build -p -b cytron_maker_pi_rp2040 zephyr/samples/basic/fade_led

-----------------------------------------------------------------------------

.. ..... FLASH ..............................................................

.. image:: /_images/symbol-rp2040-uf2-rd.*
   :class: sidecar

**Lade** dir die **Zephyr UF2 Firmware** herunter und lade diese anschließend
**auf dein MCU-Board**.

-----------------------------------------------------------------------------

.. ..... ACTION .............................................................

.. image:: /_images/symbol-observe-or.*
   :class: sidecar

Hole deinen **Terminalemulator** in den Vordergrund und **beobachte die
Ausgaben**, folgendes muss zu sehen sein::

   *** Booting Zephyr OS build zephyr-v3.6… ***
   PWM-based LED fade

Die **Benutzer-LED an GP7 "faded"**, in etwa im Sekundentakt.

.. include:: yourspace.rsti

.. admonition:: Nur für Mentoren
   :class: red-border bug
   :collapsible:

   :download:`GS-cytron_maker_pi_rp2040-uartcons-fade_led.uf2
   </_assets/GS-cytron_maker_pi_rp2040-uartcons-fade_led.uf2>`
   – als Not-Backup gedacht!

.. vi: ft=rst ai ts=3 et sw=3 sta
