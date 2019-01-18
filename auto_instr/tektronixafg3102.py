class tekafg3102(object):
    def off(instr,channel):
        instr.write('OUTP%i:STAT OFF' %channel)

    def on(instr,channel):
        instr.write('OUTP%i:STAT ON' %channel)

    def rst(instr):
        instr.write('*RST;*CLS;*OPC')

    def outimp(instr,channel,imp):
        if type(imp) == int:
            instr.write('OUTP%i:IMP %f' %(channel, imp))
        elif imp == 'INF':
            instr.write('OUTP%i:IMP INF' %channel)
        else:
            print("Invalid input")

    def shape(instr, channel, shape,duty_cycle=50):
        if shape == 'SQU':
            instr.write('SOUR%i:FUNC:SHAP SQU' %channel)  # SIN,SQU,RAMP,PULS
        elif shape == 'SIN':
            instr.write('SOUR%i:FUNC:SHAP SIN' %channel)
        elif shape == 'RAMP':
            instr.write('SOUR%i:FUNC:SHAP RAMP' %channel)
        elif shape == 'PULS':
            instr.write('SOUR%i:FUNC:SHAP PULS' %channel)
            instr.write('SOUR%i:PULS:DCYC %f' % duty_cycle)
        else:
            print("Invalid input")


    def freq(instr, channel, frequency):
        instr.write('SOUR%i:FREQ:CW %fKHz' %(channel, frequency))

    def phase(instr, channel, phase):
        instr.write('SOUR%i:PHAS:ADJ %fDEG' %(channel, phase))

    def offset(instr, channel, offset):
        instr.write('SOUR%i:VOLT:OFFS %f' %(channel, offset))

    def amplitude(instr, channel, amplitude):
        instr.write('SOUR%i:VOLT:AMPL %fVPP' % (channel, amplitude))

    def quickset(instr, channel, imp, shape, frequency, phase, offset, amplitude,duty_cycle=50):
        tekafg3102.on(instr, channel)
        tekafg3102.outimp(instr, channel, imp)
        tekafg3102.shape(instr, channel, shape,duty_cycle)
        tekafg3102.freq(instr, channel, frequency)
        tekafg3102.phase(instr, channel, phase)
        tekafg3102.offset(instr, channel, offset)
        tekafg3102.amplitude(instr, channel, amplitude)

    def awg(instr, channel, freq, filename , Vlow, Vhigh):
        instr.write('SOUR%i:FUNC:EFILe "%s"' % (channel, filename))
        instr.write('SOUR%i:FUNC:SHAP EFILe' % channel)
        instr.write('OUTP%i:IMP INF' % channel)
        instr.write('SOUR%i:VOLT:LEV:IMMediate:LOW %fV' % (channel, Vlow))
        instr.write('SOUR%i:VOLT:LEV:IMMediate:HIGH %fV' % (channel, Vhigh))
        instr.write('SOUR%i:BURS:STAT 1' % (channel))
        instr.write('SOUR%i:BURS:NCYCles 1' % channel)
        instr.write('SOUR%i:FREQ:FIX %fHz' % (channel, freq))
        instr.write('OUTP%i:STAT 1' % channel)
    def Burst_Exttrig_mode(instr,nocyc,exttriglev,pha):
        instr.write('SOUR1:BURS:NCYC %i'%nocyc)
        instr.write('TRIG1:SOUR EXT')
        instr.wite('TRIG1:LEV %f'%exttriglev)
        instr.write('TRIG:SLOP POS')
        instr.write('SOUR1:BURST:PHASE %f'%pha)
        instr.write('SOUR1:BURS:STAT ON')
        instr.write('OUTP1:STAT ON')
    def Burst_Remote_mode(instr,nocyc,pha):
        instr.write('SOUR1:BURS:NCYC %i'%nocyc)
        instr.write('TRIG1:SOUR BUS')       
        instr.write('SOUR1:BURST:PHASE %f'%pha)
        instr.write('SOUR1:BURS:STAT ON')
        instr.write('OUTP1:STAT ON')
    def Burst_Immediate_mode(instr,nocyc,pha,per):
        instr.write('SOUR1:BURS:NCYC %i'%nocyc)
        instr.write('TRIG1:SOUR IMM')
        instr.write('SOUR1:BURST:PHASE %f'%pha)
        instr.write('SOUR1:BURS:INT:PER %f'%per)
        instr.write('SOUR1:BURS:STAT ON')
        instr.write('OUTP1:STAT ON')
