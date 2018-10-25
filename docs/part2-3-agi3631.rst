=============================
Agilent 3631- DC Power Supply
=============================

This class is written for the Agilent 3631 dual channel DC power supply. It supports following methods.

------
Off/On
------
- Syntax: off(instr) or on(instr)
- Description: The only argument of this method is the instrument object, it turns off or on the output.

---------------
Setting voltage
---------------
- Syntax: setvolt(instr, channel, voltage, cmpl)
- Description: The arguments of this method are instrument object, channel number, voltage to be forced and the current compliance respectively.

