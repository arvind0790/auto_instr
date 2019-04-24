class PSW800(object):
    #############Source a Voltage with OCP On############
    def set_volt(instr,volt,current_lim):
        instr.write('SOUR:CURR:PROT:LEV %f'%current_lim)
        instr.write('SOUR:CURR:PROT:STAT ON')
        instr.write('SOUR:VOLT:LEV:IMM %f'%volt)
        instr.write('OUTP:STAT:IMM ON')
    #################Switch off the supply###############
    def off_HV(instr):
        instr.write('OUTP:STAT:IMM OFF')
    #############Source voltage and measure current######
    def forceVMeasI(instr,volt,current_lim):
        instr.write('SOUR:CURR:PROT:LEV %f' % current_lim)
        instr.write('SOUR:CURR:PROT:STAT ON')
        instr.write('SOUR:VOLT:LEV:IMM %f' % volt)
        instr.write('OUTP:STAT:IMM ON')
        current=instr.query('MEAS:SCAL:CURR:DC?')
        return current

    def set_volt_high_speed_CC(instr,volt,current_lim):#need to select F-03 to one before. 120V/17ms with out load.
        instr.write('SOUR:CURR:PROT:LEV %f'%current_lim)
        instr.write('SOUR:CURR:PROT:STAT ON')
        instr.write('SOUR:VOLT:LEV:IMM %f'%volt)
        instr.write('OUTP:STAT:IMM ON')
    def set_volt_high_speed_CV(instr,volt,current_lim):#need to select F-03 to zero before.120V in 67mS with out load
        instr.write('SOUR:CURR:PROT:LEV %f'%current_lim)
        instr.write('SOUR:CURR:PROT:STAT ON')
        instr.write('SOUR:VOLT:LEV:IMM %f'%volt)
        instr.write('OUTP:STAT:IMM ON')
    def set_volt_slew_rate_rise_CV(instr,volt,slew_rate,current_lim):#need to select F-03 to two before.Fast 120V in 83mS  and slow can be 120V in 120S.
        instr.write('SOUR:CURR:PROT:LEV %f'%current_lim)
        instr.write('SOUR:CURR:PROT:STAT ON')
        instr.write('SOUR:VOLT:LEV:IMM %f'%volt)
        instr.write('SOUR:VOLT:SLEW:RIS %f '%slew_rate)
        instr.write('OUTP:STAT:IMM ON')
    def set_volt_slew_rate_fall_CV(instr,slew_rate):#need to select F-03 to two before.Fast 120V in 86mS  and slow can be 120V in 120S.
        instr.write('SOUR:VOLT:SLEW:FALL %f '%slew_rate)
        instr.write('OUTP:STAT:IMM OFF')

