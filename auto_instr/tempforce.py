from time import sleep
class tempforce(object):

    def flow_off(instr):
        instr.write('FLOW 0\n')

    def flow_on(instr):
        instr.write('FLOW 1\n')

    def head_down(instr):
        instr.write('HEAD 1\n')

    def head_up(instr):
        instr.write('HEAD 0\n')

    def reset(instr):
        instr.write('*RST')
        instr.write('RSTP')

    def meas_air_temp(instr):
        return instr.query('TMPA?')

    def meas_DUT_temp(instr):
        return instr.query('TMPD?')

    def meas_main_temp(instr):
        current = 0
        current = instr.query('TEMP?')
        current = current.strip()
        current = float(current)
        return current

    def set_temp(instr, temp=0, soak=150):
        if temp >= 30:
            instr.write('SETN 0')
        elif 20 <= temp < 30:
            instr.write('SETN 1')
        else:
            instr.write('SETN 2')
        current = tempforce.meas_main_temp(instr)
        instr.write('SETP ' + str(temp));
        while (abs(current - temp) > 1):
            current = tempforce.meas_main_temp(instr)
            sleep(soak)

    def quick_set(instr, temp, soak):
        tempforce.head_down(instr)
        tempforce.flow_on(instr)
        tempforce.set_temp(instr, temp, soak)