Anschlüsse
##########

.. figure:: https://www.raspberrypi.com/documentation/microcontrollers/images/the-probe.png
   :name: raspberry-pi-debug-probe-pinouts
   :align: center

   Anschlüsse und Optionen am *Raspberry Pi – Debug Probe*

.. list-table::
   :align: center
   :width: 100%
   :widths: 10, 40, 40
   :stub-columns: 1
   :header-rows: 1

   * - Pin
     - UART (➌)
     - DAP (➊ & ➋)

   * - **1**
     - ``RxD`` (Receive Data, input)
     - ``SC`` (Serial Clock, output)

   * - **2**
     - ``GND``
     - ``GND``

   * - **3**
     - ``TxD`` (Transmit Data, output)
     - ``SD`` (Serial Data, bidirectional)

.. vi: ft=rst ai ts=3 et sw=3 sta
