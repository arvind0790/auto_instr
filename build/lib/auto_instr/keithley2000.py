class ke2000(object):
    
    ## DC VOLTAGE##
    def read_DCV(instr):
        instr.write("*CLS")
        instr.write('INIT:CONT OFF;:ABORT')
        instr.write("SENS:FUNC 'VOLT:DC'")
        instr.write('SENS:VOLT:DC:RANG:AUTO 1')
        instr.write('SENS:VOLT:DC:DIG 6')
        instr.write('FORM:ELEM READ')
        instr.write('TRIG:COUN 1')
        instr.write('SAMP:COUN 1')
        instr.write('TRIG:DEL 0')
        instr.write('TRIG:SOUR IMM')
        instr.write(':READ?')
        data= instr.read()
        return data

    ## DC CURRENT##
    def read_DCI(instr):
        instr.write("*CLS")
        instr.write('INIT:CONT OFF;:ABORT')
        instr.write("SENS:FUNC 'CURR:DC'")
        instr.write('SENS:CURR:DC:RANG:AUTO 1')
        instr.write('SENS:CURR:DC:DIG 6')
        instr.write('FORM:ELEM READ')
        instr.write('TRIG:COUN 1')
        instr.write('SAMP:COUN 1')
        instr.write('TRIG:DEL 0')
        instr.write('TRIG:SOUR IMM')
        instr.write(':READ?')
        data= instr.read()
        return data

    #####   RESISTANCE   ########
    def read_RES(instr):
        instr.write("*CLS")
        instr.write('INIT:CONT OFF;:ABORT')
        instr.write("SENS:FUNC 'RES'")
        instr.write('SENS:RES:RANG:AUTO 1')
        instr.write('SENS:RES:DIG 6')
        instr.write('FORM:ELEM READ')
        instr.write('TRIG:COUN 1')
        instr.write('SAMP:COUN 1')
        instr.write('TRIG:DEL 0')
        instr.write('TRIG:SOUR IMM')
        instr.write(':READ?')
        data= instr.read()
        return data

    #####    AC VOLTAGE   ########
    def read_ACV(instr):
        instr.write("*CLS")
        instr.write('INIT:CONT OFF;:ABORT')
        instr.write("SENS:FUNC 'VOLT:AC'")
        instr.write('SENS:VOLT:AC:RANG:AUTO 1')
        instr.write('SENS:VOLT:AC:DIG 6')
        instr.write('FORM:ELEM READ')
        instr.write('TRIG:COUN 1')
        instr.write('SAMP:COUN 1')
        instr.write('TRIG:DEL 0')
        instr.write('TRIG:SOUR IMM')
        instr.write(':READ?')
        data= instr.read()
        return data
    
