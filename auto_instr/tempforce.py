from auto_instr import serial
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

    def dut_sensor_type(instr,type = 0): #2 for K type(Yellow), 1 for T type (Blue)
        instr.write('DSNS '+ str(type))

    def dut_mode_on(instr):
        instr.write('DUTM 1')

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

    def quick_set(instr, temp =0, soak =150 ,type =0, plotting_enable =0):#2
        # for K
        # type(Yellow),
        # 1 for T type (
        # Blue)
        # tempforce.reset(instr)
        tempforce.dut_mode_on(instr)
        tempforce.dut_sensor_type(instr,type)
        tempforce.head_down(instr)
        tempforce.flow_on(instr)
        if plotting_enable ==1:
            import matplotlib.pyplot as plt
            import matplotlib.animation as animation
            plt.ion()
            fig = plt.figure()
            i =0
            if temp >= 30:
                instr.write('SETN 0')
            elif 20 <= temp < 30:
                instr.write('SETN 1')
            else:
                instr.write('SETN 2')
            current = tempforce.meas_main_temp(instr)
            instr.write('SETP ' + str(temp));
            while (abs(current - temp) > 1):
                plt.title('DUT Temp Vs time')
                plt.xlabel('Elapsed time (s)')
                plt.ylabel('Temperature (C)')
                current = tempforce.meas_main_temp(instr)
                plt.scatter(i, current, s=10, c='r', marker='o')
                i = i + 1
                plt.draw()
                plt.show()
                plt.pause(1)
                plt.close(fig)
            sleep(soak)
        else:
            tempforce.set_temp(instr, temp, soak)

    def purge (instr, temp = 100, soak = 30 ,type =0):#2 for K type(Yellow), 1 for T type (Blue)
        tempforce.dut_mode_on(instr)
        tempforce.dut_sensor_type(instr,type)
        tempforce.head_down(instr)
        tempforce.flow_on(instr)
        tempforce.set_temp(instr, temp, soak)

    def plot_dut_temp_vs_time(instr, plot_time_duration = 60): #plot time duration in seconds
        import matplotlib.pyplot as plt
        import matplotlib.animation as animation
        plt.ion()
        fig = plt.figure()
        plt.title('DUT Temp Vs time')
        plt.xlabel('Elapsed time (s)')
        plt.ylabel('Temperature (C)')
        for i in range(plot_time_duration):
            current_temp1 = tempforce.meas_main_temp(instr)
            plt.scatter(i, current_temp1, s=10, c='r', marker='o')
            plt.draw()
            plt.show()
            plt.pause(1)
        plt.close(fig)

