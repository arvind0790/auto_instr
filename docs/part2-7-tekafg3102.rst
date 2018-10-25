=====================================================
tekafg3102- Dual channel arbitrary function generator
=====================================================

This class is written for the Tektronics 3102 dual channel arbitrary function generator (AFG). It supports following methods.

------
Off/On
------
- Syntax: off(instr,channel) or on(instr,channel)
- Description: The arguments of this method are the instrument object and channel number, it turns off or on the output.

----------------
Output Impedance
----------------
- Syntax: outimp(instr, channel, imp)
- Description: The arguments of this method are instrument object, channel number and the desired output impedance respectively.

------
Shape
------
- Syntax: shape(instr, channel, shape, duty_cycle)
- Description: This method is used for selecting the shape of output waveform i.e square, sine, ramp, pulse etc. The arguments are instrument object, channel number, shape type and duty cycle (only required for pulse).

---------
Frequency
---------
- Syntax: freq(instr, channel, frequency)
- Description: It sets the desired frequency, the unit is KHz.

------
Phase
------
- Syntax: phase(instr, channel, phase)
- Description: It sets the desired phase, the unit is degree.

---------
Amplitude
---------
- Syntax: amplitude(instr, channel, amplitude)
- Description: It sets the desired peak to peak voltage (amplitude), the unit is volt.

-------
Offset
-------
- Syntax: offset(instr, channel, offset)
- Description: It sets the desired offset value, the unit is volt.

---------
Quick set
---------
- Syntax: quickset(instr, channel, imp, shape, frequency, phase, offset, amplitude,duty_cycle=50)
- Description : This method is used for configuring the AFG in one step. Arguments are instrument object, channel number, output impedance, shape, frequency, phase, offset, amplitude and duty cycle(required only for pulse).