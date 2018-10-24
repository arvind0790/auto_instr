============
Introduction
============
auto_instr uses an object-oriented approach for communicating with scientific instruments, 
which provides an intuitive interface where the low-level SCPI and GPIB commands are hidden 
from normal use. Users can focus on solving the measurement problems at hand, 
instead of re-inventing how to communicate with instruments.

Instruments with VISA (GPIB, Serial, LAN, USB etc.) are supported through the PyVISA package under the hood. 
Communication protocols can be swapped, so that instrument classes can be used with all supported protocols interchangeably.

Before using auto_instr, you may find it helpful to be acquainted with basic Python programming 
for the sciences and understand the concept of objects.
