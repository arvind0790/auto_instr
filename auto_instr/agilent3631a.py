class agi3631(object):
    def off(instr):
        instr.write('OUTP %i' %0)

    def on(instr):
        instr.write('OUTP %i' %1)

    def rst(instr):
        instr.write('*RST;*CLS;*OPC')

    def ch_sel(instr, channel=1):
        instr.write('INST:NSEL %i' %channel)

    def setvolt(instr, channel=1, voltage=1, cmpl=0.01):
        instr.write('INST:NSEL %i' % channel)
        instr.write('VOLT %f' % voltage)
        instr.write('CURR %f' % cmpl)
        instr.write('OUTP %i' % 1)

    def measure(instr):
        instr.write('MEAS:VOLT?')
        volt_data = instr.read()
        instr.write('MEAS:CURR?')
        curr_data = instr.read()
        data = volt_data.split(',') + curr_data.split(',')
        return data