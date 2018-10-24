class ke2400(object):
    def off(instr):
        instr.write('OUTP OFF')

    def on(instr):
        instr.write('OUTP ON')

    def forImeasV(instr, current, volt_cmpl):
        instr.write('SENS:FUNC:OFF "CURR"')
        instr.write('SENS:FUNC:ON "VOLT"')
        instr.write('SOUR:FUNC:MODE CURR')
        instr.write('SOUR:CURR %f' % current)
        instr.write('SENS:VOLT:PROT %f' % volt_cmpl)
        instr.write('OUTP ON')
        # instr.write('SENS:VOLT:RANG:AUTO 1')
        # instr.write('SOUR:CURR:RANG:AUTO 1')
        instr.write('READ?')
        instr_data_raw = instr.read()
        instr_data = instr_data_raw.split(',')
        volt_data = instr_data[0]
        return float(volt_data)

    def forVmeasI(instr, voltage, curr_cmpl):
        instr.write('SENS:FUNC:OFF "VOLT"')
        instr.write('SENS:FUNC:ON "CURR"')
        instr.write('SOUR:FUNC:MODE VOLT')
        instr.write('SOUR:VOLT %f' % voltage)
        instr.write('SENS:CURR:PROT:LEV %f' % curr_cmpl)
        instr.write('OUTP ON')
        # instr.write('SENS:CURR:RANG:AUTO 1')
        # instr.write('SOUR:VOLT:RANG:AUTO 1')
        instr.write('READ?')
        instr_data_raw = instr.read()
        instr_data = instr_data_raw.split(',')
        curr_data = instr_data[1]
        return float(curr_data)

    def forVmeasV(instr, voltage, volt_cmpl):
        instr.write('SENS:FUNC:ON "VOLT"')
        instr.write('SENS:FUNC:OFF "CURR"')
        instr.write('SOUR:FUNC:MODE VOLT')
        instr.write('SOUR:VOLT %f' % voltage)
        instr.write('SENS:VOLT:PROT:LEV %f' % volt_cmpl)
        instr.write('OUTP ON')
        # instr.write('SENS:VOLT:RANG:AUTO 1')
        # instr.write('SOUR:VOLT:RANG:AUTO 1')
        instr.write('READ?')
        instr_data_raw = instr.read()
        instr_data = instr_data_raw.split(',')
        volt_data = instr_data[0]
        return float(volt_data)

    def autorang_forVmeasI(instr):
        instr.write('SENS:CURR:RANG:AUTO 1')
        instr.write('SOUR:VOLT:RANG:AUTO 1')

    def autorang_forImeasV(instr):
        instr.write('SENS:VOLT:RANG:AUTO 1')
        instr.write('SOUR:CURR:RANG:AUTO 1')

