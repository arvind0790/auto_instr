========
Adapter
========
This library is used for configuring the connection with the instrument. It supports following classes.

- gpib

- serial

- lan

- usb

These classes support *addr* method, in which user is expected to pass the port address or IP of the instrument.
The method opens the visa resource and returns the instrument object, which then could be used with other instrument classes or independently to write SCPI commands.

--------
Examples
--------
- **my_afg = serial.addr(2)** , my_afg is an instrument object configured via serial connection.

- **my_afg.write('OUTP1:IMP INF')** , SCPI command for configuring high Z mode is sent to my_afg.

- **tekafg3102.off(my_afg,1)** , the channel 1 output of my_afg is turned off.


