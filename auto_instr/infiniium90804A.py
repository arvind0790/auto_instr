from time import sleep

class infi90804(object):
    ####### Acquisition Commands ###########
    def run(instr):
        instr.write(':RUN')
    def single(instr):
         instr.write(':SINGle')
####### Channel Commands ###############
    def offset(instr,ch_no,offset):
        instr.write(':CHANnel%i:OFFSet %f' %(ch_no, offset))
    def display(instr, ch_no,disp):
        instr.write(':CHANnel%i:DISPlay %i'%(ch_no, disp))
    def range(instr,ch_no,range):
        instr.write(':CHANnel%i:RANGe %f' %(ch_no, range))
    def scale(instr,ch_no,scale):
        instr.write(':CHANnel%i:SCALe %f' %(ch_no, scale))
    def mode_diff_on(instr,ch_no):
        instr.write(':CHANnel%i:DIFFerential ON' %ch_no)
    def mode_diff_off(instr,ch_no):
        instr.write(':CHANnel%i:DIFFerential OFF' %ch_no)
    def mode_comm_on(instr,ch_no):
        instr.write(':CHANnel%i:COMMonmode ON' %ch_no)
    def mode_comm_off(instr,ch_no):
        instr.write(':CHANnel%i:COMMonmode OFF' %ch_no)
    def diff_auto_on(instr,ch_no):
        infi90804.mode_diff_on(instr,ch_no)
        instr.write(':CHANnel%i:DISPlay:AUTO ON' %ch_no)
    def diff_auto_off(instr,ch_no):
        infi90804.mode_diff_on(instr,ch_no)
        instr.write(':CHANnel%i:DISPlay:AUTO OFF' %ch_no)
    def diff_offset(instr,ch_no,offset):
        infi90804.mode_diff_on(instr,ch_no)
        instr.write(':CHANnel%i:DISPlay:OFFSet %f' %(ch_no,offset))
    def diff_range(instr,ch_no,range):
        infi90804.mode_diff_on(instr,ch_no)
        instr.write(':CHANnel%i:DISPlay:RANGe %f' %(ch_no,range))
    def diff_scale(instr,ch_no,scale):
        infi90804.mode_diff_on(instr,ch_no)
        instr.write(':CHANnel%i:DISPlay:SCALe %f' %(ch_no,scale))
    def horizontal_range(instr,ch_no,range):
        instr.write(':CHANnel%i:TIMebase:RANGe%f' %(ch_no,range))
    def horizontal_scale(instr,ch_no,scale):
        instr.write(':CHANnel%i:TIMebase:SCALe%f' % (ch_no,scale))

####### Measurement functions ##########
    def meas_clrdisp(instr):
        instr.write(':CDISplay')
    def meas_clrres(instr):
        instr.write(':MEASure:CLEar')
    def meas_source(instr,ch_no):
        instr.write(':MEASure:SOURce CHAN%i' %ch_no)
    def meas_freq(instr):
        instr.write(':MEASure:FREQuency')
        return float(instr.query(':MEASure:FREQuency?'))
    def meas_abs_vmax(instr):
        instr.write(':MEASure:VMAX')
        return float(instr.query(':MEASure:VMAX?'))
    def meas_abs_vmin(instr):
        instr.write(':MEASure:VMIN')
        return float(instr.query(':MEASure:VMIN?'))
    def meas_vrms(instr):
        instr.write(':MEASure:VRMS CYCLe,DC,VOLT')
        return float(instr.query(':MEASure:VRMS? CYCLe,DC,VOLT'))
    def meas_vampl(instr):
        instr.write(':MEASure:VAMPlitude')
        return float(instr.query(':MEASure:VAMPlitude?'))
    def meas_vpp(instr):
        instr.write(':MEASure:VPP')
        return float(instr.query(':MEASure:VPP?'))
    def meas_duty(instr):
        instr.write(':MEASure:DUTYcycle FALLing')## not responding to edge selection.
        return float(instr.query(':MEASure:DUTYcycle?'))
    def meas_period(instr):
        instr.write(':MEASure:PERiod RISing')
        return float(instr.query(':MEASure:PERiod?'))
    def meas_pwidth(instr,ch_no):
        instr.write(':MEASure:SOURce CH%i' %ch_no)
        instr.write(':MEASure:PWIDth')
        return float(instr.query(':MEASure:PWIDth?'))
    def meas_nwidth(instr,ch_no):
        instr.write(':MEASure:SOURce CH%i' %ch_no)
        instr.write(':MEASure:NWIDth')
        return float(instr.query(':MEASure:NWIDth?'))
    def meas_risetime(instr,ch_no):
        instr.write(':MEASure:SOURce CH%i' %ch_no)
        instr.write(':MEASure:RISetime')
        return float(instr.query(':MEASure:RISetime?'))
    def meas_falltime(instr,ch_no):
        instr.write(':MEASure:SOURce CH%i' %ch_no)
        instr.write(':MEASure:FALLtime')
        return float(instr.query(':MEASure:FALLtime?'))
    def meas_delay(instr,ch_s1,ch_s2):
        instr.write(':MEASure:DELTAtime CHANnel1,CHANnel2' %(ch_s1,ch_s2))
        return instr.query(':MEASure:DELTatime? CHANnel1,CHANnel2' %(ch_s1,ch_s2))
    def meas_results(instr):
        return instr.query(':MEASure:RESults?')
    
########## Trigger Functions #####################
    def trigger_single(instr):
        instr.write(':TRIGger:SWEep SINGle')
    def trigger_auto(instr):
        instr.write(':TRIGger:SWEep AUTO')
    def trigger_pos_edge(instr):
        instr.write(':TRIGger:EDGE:SLOPe POS')
    def trigger_neg_edge(instr):
        instr.write(':TRIGger:EDGE:SLOPe NEG')
    def trigger_source(instr, ch_no=1):
        instr.write(':TRIGger:EDGE:SOUR CHAN%i' % ch_no)
    def trigger_level(instr, ch_no, lev):
        instr.write(':TRIGger:LEVel CHAN%i,%f' % (ch_no, lev))

############ Jitter Measurements ###########################
    def measure_jitter(instr):
        instr.write(':MEASure:RJDJ:MODE TIE')
        mode = instr.query('MEASure:RJDJ:MODE?')
        print('mode = ', mode)
        instr.write(':MEASure:RJDJ:CLOCk ON')
        clk = instr.query(':MEASure:RJDJ:CLOCk?')
        print('clk = ',clk)
        instr.write(':MEASure:CLOCk:METHod:EDGE RISing')
        clk_method = instr.query(':MEASure:CLOCk:METHod:EDGE?')
        print('clk_method = ', clk_method)
        instr.write(':MEASure:RJDJ:EDGE RISing')
        jit_clk_edge = instr.query(':MEASure:RJDJ:EDGE?')
        print('jit_clk_edge = ', jit_clk_edge)
        instr.write(':MEASure:RJDJ:BANDwidth Narrow')
        BW = instr.query(':MEASure:RJDJ:BANDwidth?')
        print('BW = ', BW)
        jit = instr.query(':MEASure:RJDJ:ALL?')
        return jit

    def measure_longterm_jitter(instr):
        instr.write(':MEASure:RJDJ:MODE TIE')
        mode = instr.query('MEASure:RJDJ:MODE?')
        print('mode = ', mode)
        instr.write(':MEASure:RJDJ:CLOCk ON')
        clk = instr.query(':MEASure:RJDJ:CLOCk?')
        print('clk = ', clk)
        instr.write(':MEASure:CLOCk:METHod:EDGE RISing')
        clk_method = instr.query(':MEASure:CLOCk:METHod:EDGE?')
        print('clk_method = ', clk_method)
        instr.write(':MEASure:RJDJ:EDGE RISing')
        jit_clk_edge = instr.query(':MEASure:RJDJ:EDGE?')
        print('jit_clk_edge = ', jit_clk_edge)
        instr.write(':MEASure:RJDJ:BANDwidth Narrow')
        BW = instr.query(':MEASure:RJDJ:BANDwidth?')
        print('BW = ', BW)
        instr.write(':MEASure:NCJitter CHANnel2,RISing,50,1')
        sleep(20)
        instr.write(':MEASure:STATISTICS ON')
        jit = instr.query(':MEASure:RES? ')
        return jit




