========
Adapter
========
This library is used for configuring the connection with the instrument. It supports following classes.

- gpib

- serial

- lan

- usb

These classes support *addr* method, in which user is expected to pass the port address or IP of the instrument.
The method opens the visa resource.
Subsequently the object is returned which could be used with other instrument classes or user can write SCPI commands himself.

--------
Examples
--------
- **my_afg1 = serial.addr(2)** , my_afg1 is an object configured via serial connection.

- **my_afg1.write('OUTP1:IMP INF')** , SCPI command for configuring high Z mode is directly written.

- **tekafg3102.off(my_afg1,1)** , my_afg1 channel 1 output is turned off.


