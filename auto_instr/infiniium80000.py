from time import sleep
class infi_scope(object):
############ Channel settings ####################
    def channel_offset(instr,ch_no, v_offset):
        instr.write('CHAN%i:OFFS %f' % (ch_no, v_offset))
    def channel_vscale(instr,ch_no, v_scale):
        instr.write('CHAN%i:SCAL %f' % (ch_no, v_scale))
    def horz_scale(instr,time):
        instr.write(':TIMebase:SCALe %f'%time)
    def autoscale(instr):
        instr.write(':AUT')
############ Acquisition modes ########################
    def run(instr):
        instr.write('ACQ:MODE ETIM')
    def single(instr):
        instr.write('ACQ:MODE RTIM')
    def high_resolution(instr):
        instr.write('ACQ:MODE HRES')
############### Measurement functions #############
    def meas_cls(instr):
        instr.write('MEAS:CLE')
    def measure_source(instr,ch_no=1):
        instr.write('MEAS:SOUR CHAN%i' %ch_no)
    def measure_amp(instr,ch_no=1):
        return instr.query('MEAS:VAMP? CHAN%i'%ch_no)
    def measure_high(instr,ch_no=1):
        return instr.query(':MEAS:VMAX? CHAN%i'%ch_no)
    def measure_low(instr,ch_no=1):
        return instr.query(':MEAS:VMIN? CHAN%i'%ch_no)
    def measure_results(instr):
        return instr.query(':MEASure:RESults?')
    def measure_freq(instr,ch_no=1):
        return instr.query(':MEASure:FREQuency? CHAN%i' %ch_no)
    def measure_period(instr, ch_no=1):
        return instr.query(':MEASure:PER? CHAN%i' % ch_no)
    def measure_pwidth(instr, ch_no=1):
        return instr.query(':MEASure:PWID? CHAN%i' % ch_no)
    def measure_nwidth(instr, ch_no=1):
        return instr.query(':MEASure:NWID? CHAN%i' % ch_no)
    def measure_duty_cycle(instr,ch_no=1):
        return instr.query(':MEASure:DUTY? CHAN%i' % ch_no)
    def measure_rise_time(instr,ch_no=1):
        return instr.query(':MEASure:RIS? CHAN%i' % ch_no)
    def measure_fall_time(instr,ch_no=1):
        return instr.query(':MEASure:FALL? CHAN%i' % ch_no)
    def measure_delta_time(instr,ch_s1,ch_s2):
        return instr.query(':MEASure:DELTatime? CHAN%i,CHAN%i'%(ch_s1,ch_s2))
    def set_abs_ref_lev(instr, ch_no, abs_min_ref_lev, abs_max_ref_lev, abs_mid_ref_lev):
        instr.write(':MEAS:DEF THR, VOLT, %f, %f, %f ,CHAN%i' % (abs_max_ref_lev,
                                                                abs_mid_ref_lev,
                                                                abs_min_ref_lev,ch_no))
    def set_perc_ref_lev(instr, ch_no=1, perc_min_ref_lev=10, perc_max_ref_lev=90, perc_mid_ref_lev
    =50):
        instr.write(':MEAS:DEF THR, PERC, %f, %f, %f , CHAN%i' % (perc_max_ref_lev,
                                                                 perc_mid_ref_lev,
                                                                 perc_min_ref_lev, ch_no))
############### trigger functions ##################
    def trigger_single(instr):
        instr.write(':TRIGger:SWEep SINGle')
    def trigger_auto(instr):
        instr.write(':TRIGger:SWEep AUTO')
    def trigger_pos_edge(instr):
        instr.write(':TRIGger:EDGE:SLOPe POS')
    def trigger_neg_edge(instr):
        instr.write(':TRIGger:EDGE:SLOPe NEG')
    def trigger_source(instr,ch_no=1):
        instr.write(':TRIGger:EDGE:SOUR CHAN%i'%ch_no)
    def trigger_level(instr,ch_no,lev):
        instr.write(':TRIGger:LEVel CHAN%i,%f'%(ch_no,lev))
