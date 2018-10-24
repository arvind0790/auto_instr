from time import sleep
class scope(object):

############ Channel settings ####################

    def channel_offset(instr,ch_no, v_offset):
        instr.write('CH%i:OFFS %f' % (ch_no, v_offset))

    def channel_scale(instr,ch_no, v_scale):
        instr.write('CH%i:SCA %f' % (ch_no, v_scale))

    def horz_scale(instr,scale):
        instr.write('HOR:MODE:SCA %s' % scale)

    def bandwidth_full(instr,ch_no):
        instr.write('CH%i:BANDWIDTH FUL'%ch_no)

    def set_bandwidth(instr,ch_no,bw):
        instr.write('CH%i:BANDWIDTH %s'%(ch_no,bw))

    def autoset(instr):
        instr.write('AUTOS EXEC')

    def set_abs_ref_lev(instr,abs_min_ref_lev,abs_max_ref_lev):
        instr.write('MEASU:IMM:REFL:METH ABS')
        instr.write('MEASU:IMM:REFL:ABS:HIGH %f' % abs_max_ref_lev)
        instr.write('MEASU:IMM:REFL:ABS:LOW %f' % abs_min_ref_lev)
    def set_perc_ref_lev(instr,perc_min_ref_lev=10,perc_max_ref_lev=90):
        instr.write('MEASU:IMM:REFL:METH PERC')
        instr.write('MEASU:IMM:REFL:PERC:HIGH %f' % perc_max_ref_lev)
        instr.write('MEASU:IMM:REFL:PERC:LOW %f' % perc_min_ref_lev)
############ Acquisition modes ########################

    def run(instr):
        instr.write('ACQ:STATE RUN')

    def stop(instr):
        instr.write('ACQ:STATE STOP')

    def run_mode(instr):
        instr.write('ACQ:STOPA RUNST')

    def single(instr):
        instr.write('ACQ:STOPA SEQ')

    def single_refresh(instr):
        instr.write('ACQ:STATE ON')

    def averaging(instr,no_avg):
        instr.write('ACQ:MOD AVE')
        instr.write('ACQ:NUMAV %i'%no_avg)

    def high_resolution(instr):
        instr.write('ACQ:MOD HIR')

############### Measurement functions #############

    def meas_cls(instr):
        instr.write('MEASU:STATI:COUN RESET')

    def measure_source(instr,ch_no):
        instr.write('MEASU:IMM:SOU1 CH%i' %ch_no)

    def measure_amp(instr):
        instr.write('MEASU:IMM:TYP AMP')
        return float(instr.ask('MEASU:IMM:VAL?'))

    def measure_high(instr):
        instr.write('MEASU:IMM:TYP HIGH')
        return float(instr.ask('MEASU:IMM:VAL?'))

    def measure_low(instr):
        instr.write('MEASU:IMM:TYP LOW')
        return float(instr.ask('MEASU:IMM:VAL?'))

    def measure_freq(instr):
        instr.write('MEASU:IMM:TYP FREQ')
        return float(instr.ask('MEASU:IMM:VAL?'))

    def measure_positive_duty(instr):
        instr.write('MEASU:IMM:TYP PDU')
        return float(instr.ask('MEASU:IMM:VAL?'))

    def measure_negative_duty(instr):
        instr.write('MEASU:IMM:TYP NDU')
        return float(instr.ask('MEASU:IMM:VAL?'))

    def measure_rise_time(instr):
        instr.write('MEASU:IMM:TYP RIS')
        return float(instr.ask('MEASU:IMM:VAL?'))

    def measure_fall_time(instr):
        instr.write('MEASU:IMM:TYP FALL')
        return float(instr.ask('MEASU:IMM:VAL?'))

    def measure_positive_pulse_width(instr):
        instr.write('MEASU:IMM:TYP PWI')
        return float(instr.ask('MEASU:IMM:VAL?'))

    def measure_negative_pulse_width(instr):
        instr.write('MEASU:IMM:TYP NWI')
        return float(instr.ask('MEASU:IMM:VAL?'))


 ############### Cursor functions ############

    def horizontal_curser(instr):
        instr.write('CURS:HBA:POSITION1 6.2')

    def source_cursor(instr):
        instr.write('CURSOR:SOURCE 1 CH2')

    def vertical_bar_position_query(instr):
        return str(instr.ask('CURSor:VBArs?'))

    def diff_between_vericalbar(instr):
        return float(instr.ask('CURSOR:VBARS:DELTA?'))
 
 ############### trigger functions ##################

    def trigger_level(instr):
        instr.write('TRIG:A:LEV:CH2 6.2')

    def trigger_level_ask(instr):
        return float(instr.ask('TRIG:A:LEV:CH2 ?'))
    
    def trigger_quickset(instr, ch_no,lev):
        instr.write('TRIG:A:EDGE:SOU CH%i' %ch_no)
        instr.write('TRIG:A:EDGE:SLO:CH%i RIS' % ch_no)
        instr.write('TRIG:A:LEV:CH%i %f' %(ch_no, lev))

    def trigger_quickset_rise(instr, ch_no,lev):
        instr.write('TRIG:A:EDGE:SOU CH%i' %ch_no)
        instr.write('TRIG:A:EDGE:SLO:CH%i RIS' % ch_no)
        instr.write('TRIG:A:LEV:CH%i %f' %(ch_no, lev))

    def trigger_quickset_fall(instr, ch_no,lev):
        instr.write('TRIG:A:EDGE:SOU CH%i' %ch_no)
        instr.write('TRIG:A:EDGE:SLO:CH%i FALL' % ch_no)
        instr.write('TRIG:A:LEV:CH%i %f' %(ch_no, lev))


    def single_acquisition_quickset(instr,ch_no,lev,edge='RISE'): #use FALL for falling egde trigger
        scope.run(instr)
        if edge =='FALL':
            scope.trigger_quickset_fall(instr, ch_no,lev)
        else:
            scope.trigger_quickset_rise(instr, ch_no, lev)
        scope.meas_cls(instr)
        scope.single(instr)
############## DPO JET functions (for jitter measurement) #############
    
    def dpojet_clr_meas(instr):
        instr.write('DPOJET:CLEARALLM')
    def dpojet_state(instr):
        return instr.ask('DPOJET:STATE?')
    def dpojet_run(instr):
        instr.write('DPOJET:STATE RUN')
    def dpojet_stop(instr):
        instr.write('DPOJET:STATE STOP')
    def dpojet_population(instr,n):
        instr.write('DPOJET:POPULATION:LIMIT %i' %n)
        instr.write('DPOJET:POPULATION:STATE 1')
    def dpojet_period(instr):
        instr.write('DPOJET:ADDM PERI')
    def dpojet_result(instr):
        data = instr.ask('DPOJET:MEAS1:RESUL:ALLA?').split(';;')
        # print(data)
        return data
    def dpojet_status_query(instr):
        data = instr.ask('DPOJET:MEAS1:RESUL:ALLA?').split(';;')
        curr_popu = int(data[0])
        return curr_popu
    def dpojet_quickset(instr,n):
        scope.dpojet_stop(instr)
        scope.dpojet_clr_meas(instr)
        scope.dpojet_period(instr)
        scope.dpojet_population(instr,n)
        sleep(2)
        scope.dpojet_run(instr)
        sleep(2)
        status = scope.dpojet_status_query(instr)
        while status < n:
            sleep(10)
            status = scope.dpojet_status_query(instr)
        meas_val = scope.dpojet_result(instr)
        scope.dpojet_stop(instr)
        return meas_val

############ Custom functions #########################
    def delay(instr, ch1=1, ch2=2,edge_ch1 = 'RISE',edge_ch2 = 'FALL',direction ='FORW'): #use BACKW for reverse direction
        instr.write('MEASU:IMM:SOU1 CH%i' %ch1)
        instr.write('MEASU:IMM:SOU2 CH%i' %ch2)
        instr.write('MEASU:IMM:DEL:EDGE1 %s'%edge_ch1)
        instr.write('MEASU:IMM:DEL:EDGE2 %s'%edge_ch2)
        instr.write('MEASU:IMM:DEL:DIREC %s'%direction)
        instr.write('MEASU:IMM:TYP DEL')
        return float(instr.ask('MEASU:IMM:VAL?'))

    def delay_imo(instr):
        instr.write('MEASU:IMM:SOU1 CH1')
        instr.write('MEASU:IMM:SOU2 CH2')
        instr.write('MEASU:IMM:DEL:EDGE1 RISE')
        instr.write('MEASU:IMM:DEL:EDGE2 FALL')
        instr.write('MEASU:IMM:DEL:DIREC FORW')
        instr.write('MEASU:IMM:TYP DEL')
        return float(instr.ask('MEASU:IMM:VAL?'))

    def delay_ilo(instr):
        instr.write('MEASU:IMM:SOU1 CH1')
        instr.write('MEASU:IMM:SOU2 CH2')
        instr.write('MEASU:IMM:DEL:EDGE1 FALL')
        instr.write('MEASU:IMM:DEL:EDGE2 FALL')
        instr.write('MEASU:IMM:DEL:DIREC FORW')
        instr.write('MEASU:IMM:TYP DEL')
        return float(instr.ask('MEASU:IMM:VAL?'))

    def delay_PDAC(instr):
        instr.write('MEASU:IMM:SOU1 CH1')
        instr.write('MEASU:IMM:SOU2 CH2')
        instr.write('MEASU:IMM:DEL:EDGE1 RISE')
        instr.write('MEASU:IMM:DEL:EDGE2 RISE')
        instr.write('MEASU:IMM:DEL:DIREC FORW')
        instr.write('MEASU:IMMED:REFL:PERC:MID2 95')
        instr.write('MEASU:IMM:TYP DEL')
        return float(instr.ask('MEASU:IMM:VAL?'))

    def delay_NDAC_small(instr):
        instr.write('MEASU:IMM:SOU1 CH1')
        instr.write('MEASU:IMM:SOU2 CH2')
        instr.write('MEASU:IMM:DEL:EDGE1 RISE')
        instr.write('MEASU:IMM:DEL:EDGE2 FALL')
        instr.write('MEASU:IMM:DEL:DIREC BACKW')
        instr.write('MEASU:IMMED:REFL:PERC:MID2 30')
        instr.write('MEASU:IMM:TYP DEL')
        return float(instr.ask('MEASU:IMM:VAL?'))

    def delay_NDAC(instr):
        instr.write('MEASU:IMM:SOU1 CH1')
        instr.write('MEASU:IMM:SOU2 CH2')
        instr.write('MEASU:IMM:DEL:EDGE1 RISE')
        instr.write('MEASU:IMM:DEL:EDGE2 FALL')
        instr.write('MEASU:IMM:DEL:DIREC BACKW')
        instr.write('MEASU:IMMED:REFL:PERC:MID2 10')
        instr.write('MEASU:IMM:TYP DEL')
        return float(instr.ask('MEASU:IMM:VAL?'))

    def delay_UV(instr,Cur1_ypos1,cur2_ypos2):
        instr.write('CURS:STATE ON')
        instr.write('CURS:FUNC SCREEN')
        instr.write('CURS:SCREEN:STY LINE_X')
        instr.write('CURS:SOU1 CH1')
        instr.write('CURS:SOU2 CH2')
        instr.write('CURS:SCREEN:YPOSITION1 %f' %Cur1_ypos1)
        instr.write('CURS:SCREEN:YPOSITION2 %f' %cur2_ypos2)
        sleep(4)
        t1 = float(instr.ask('CURS:SCREEN:XPOSITION1?'))
        t2 = float(instr.ask('CURS:SCREEN:XPOSITION2?'))
        # print(t1)
        # print(t2)
        t3 = float(t2-t1)
        return t3

    def delay_UV_4(instr,threshold):
        instr.write('CURS:STATE ON')
        instr.write('CURS:FUNC WAVE')
        instr.write('CURS:SCREEN:STY LINE_X')
        instr.write('CURS:SOU1 CH1')
        instr.write('CURS:SOU2 CH2')
        instr.write('CURS:WAVE:POS2 0E-6')
        # instr.write('CURS:WAVE:POS1 -10E-6')
        y1 = 0
        h1 = -0.00002
        for i in range(50):
            h2 = float(h1 + 0.000001)
            # print(h2)
            # sleep(2)
            instr.write('CURS:WAVE:POS1 %f' % h2)
            sleep(5)
            y = (instr.ask('CURS:WAVE:HPOS1?'))
            h = (instr.ask('CURS:WAVE:POS1?'))
            # print(h)
            y1 = float(y[0:5])
            h1 = -float(h[1:5]) * (0.000001)
            # print(y1,h1)
            if y1 >= threshold:
                t = abs(h1 - 0)
                return t
                break

    def delay_UV_5(instr,threshold):
        instr.write('CURS:STATE ON')
        instr.write('CURS:FUNC WAVE')
        instr.write('CURS:SCREEN:STY LINE_X')
        instr.write('CURS:SOU1 CH1')
        instr.write('CURS:SOU2 CH2')
        instr.write('CURS:WAVE:POS2 0E-6')
        # instr.write('CURS:WAVE:POS1 -10E-6')
        y1 = 0
        h1 = -0.00002
        for i in range(50):
            h2 = float(h1 + 0.000001)
            # print(h2)
            # sleep(2)
            instr.write('CURS:WAVE:POS1 %f' % h2)
            sleep(5)
            y = (instr.ask('CURS:WAVE:HPOS1?'))
            h = (instr.ask('CURS:WAVE:POS1?'))
            # print(y,h)
            y1 = float(y[0:5])
            h1 = -float(h[1:5]) * (0.000001)
            # print(y1, h1)
            if y1 >= threshold:
                t = abs(h1 - (0))
                return t
                break

    def delay_gpio_lscsa_ac(instr):
        instr.write('MEASU:IMM:SOU1 CH2')
        instr.write('MEASU:IMM:SOU2 CH1')
        instr.write('MEASU:IMM:DEL:EDGE1 RISE')
        instr.write('MEASU:IMM:DEL:EDGE2 RISE')
        instr.write('MEASU:IMM:DEL:DIREC FORW')
        instr.write('MEASU:IMM:TYP DEL')
        return float(instr.ask('MEASU:IMM:VAL?'))
        
    def delay_Tdelay_lscsa_ac(instr):
        instr.write('MEASU:IMM:SOU1 CH2')
        instr.write('MEASU:IMM:SOU2 CH3')
        instr.write('MEASU:IMM:DEL:EDGE1 RISE')
        instr.write('MEASU:IMM:DEL:EDGE2 RISE')
        instr.write('MEASU:IMM:DEL:DIREC FORW')
        instr.write('MEASU:IMM:TYP DEL')
        return float(instr.ask('MEASU:IMM:VAL?'))

