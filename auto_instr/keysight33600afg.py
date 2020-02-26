class keyafg33600(object):

    def off(instr,channel):
        instr.write('OUTP%i:STAT OFF' %channel)
    
    def on(instr,channel):
        instr.write('OUTP%i:STAT ON' %channel)
    
    def rst(instr):
        instr.write('*RST;*CLS;*OPC')
    
    def outimp(instr,channel,imp):
        if type(imp) == int:
            instr.write('OUTP%i:LOAD %f' %(channel, imp))
        elif imp == 'INF':
            instr.write('OUTP%i:LOAD INF' %channel)
        else:
            print("Invalid input")
    
    def shape(instr, channel, shape, duty_cycle=50):
        if shape == 'SQU':
            instr.write('SOUR%i:FUNC:SHAP SQU' %channel)  # SIN,SQU,RAMP,PULS
            instr.write('SOUR%i:FUNC:SQU:DCYC %f' %(channel,duty_cycle))
        elif shape == 'SIN':
            instr.write('SOUR%i:FUNC:SHAP SIN' %channel)
        elif shape == 'RAMP':
            instr.write('SOUR%i:FUNC:SHAP RAMP' %channel)
        elif shape == 'PULS':
            instr.write('SOUR%i:FUNC:SHAP PULS' %channel)
        else:
            print("Invalid input")

    def freq(instr, channel, frequency):
        instr.write('SOUR%i:FREQ:MODE CW' %(channel))
        instr.write('SOUR%i:FREQ %fKHz' %(channel, frequency))
    
    def phase(instr, channel, phase):
        instr.write('SOUR%i:PHAS:ADJ %fDEG' %(channel, phase))
    
    def offset(instr, channel, offset):
        instr.write('SOUR%i:VOLT:OFFS %f' %(channel, offset))
    
    def amplitude(instr, channel, amplitude):
        instr.write('SOUR%i:VOLT:AMPL %fVPP' % (channel, amplitude))
    
    def quickset(instr, channel, imp, shape, frequency, phase, offset, amplitude,duty_cycle=50):
        keyafg33600.on(instr, channel)
        keyafg33600.outimp(instr, channel, imp)
        keyafg33600.shape(instr, channel, shape,duty_cycle)
        keyafg33600.freq(instr, channel, frequency)
        keyafg33600.phase(instr, channel, phase)
        keyafg33600.offset(instr, channel, offset)
        keyafg33600.amplitude(instr, channel, amplitude)

    def Burst_Exttrig_mode(instr, channel, nocyc, exttriglev, pha):
        instr.write('SOUR%i:BURS:NCYC %i' % (channel, nocyc))
        instr.write('TRIG1:SOUR EXT')
        instr.wite('TRIG1:LEV %f' % exttriglev)
        instr.write('TRIG1:SLOP POS')
        instr.write('SOUR%i:BURST:PHASE %f' % (channel, pha))
        instr.write('SOUR%i:BURS:STAT ON' % channel)
        instr.write('OUTP%i:STAT ON' % channel)

    def highlow(instr, channel, low, high, frequency, imp):
        keyafg33600.shape(instr, channel,'SQU')
        keyafg33600.freq(instr, channel, frequency)
        keyafg33600.outimp(instr,channel, imp)
        instr.write('SOUR%i:VOLT:LEV:IMMediate:LOW %fV' % (channel,low))
        instr.write('SOUR%i:VOLT:LEV:IMMediate:HIGH %fV'% (channel,high))
        keyafg33600.on(instr,channel)

    def dutycycle(instr, channel, dutycycle):
        instr.write('SOUR%i:PULSe:DCYCle %f' % (channel, dutycycle))

    def pulsewidth(instr, channel, pulsewidth):
        instr.write('SOUR%i:PULSe:WIDTh %fns' % (channel, pulsewidth))

    def Burst_Exttrig_mode(instr,channel,nocyc,exttriglev,pha):
        instr.write('SOUR%i:BURS:NCYC %i'%(channel,nocyc))
        instr.write('TRIG1:SOUR EXT')
        instr.wite('TRIG1:LEV %f'%exttriglev)
        instr.write('TRIG1:SLOP POS')
        instr.write('SOUR%i:BURST:PHASE %f'%(channel,pha))
        instr.write('SOUR%i:BURS:STAT ON'%channel)
        instr.write('OUTP%i:STAT ON'%channel)

    def Burst_Remote_mode(instr, channel, nocyc, pha):
        instr.write('SOUR%i:BURS:NCYC %i' % (channel, nocyc))
        instr.write('TRIG1:SOUR BUS')
        instr.write('SOUR%i:BURST:PHASE %f' % (channel, pha))
        instr.write('SOUR%i:BURS:STAT ON' % channel)
        instr.write('OUTP%i:STAT ON' % channel)

    def Burst_Immediate_mode(instr, channel, nocyc, pha, per):
        instr.write('SOUR%i:BURS:NCYC %i' % (channel, nocyc))
        instr.write('TRIG1:SOUR IMM')
        instr.write('SOUR1:BURST:PHASE %f'%pha)
        instr.write('SOUR1:BURS:INT:PER %f'%per)
        instr.write('SOUR1:BURS:STAT ON')
        instr.write('OUTP1:STAT ON')
        
    def Burst_arbitary_remote_trigger(instr,nocyc,file_name):
        instr.write('MMEM:DATA "usb:\Myfiles\%s.arb"'%file_name)
        instr.write('SOUR1:ARB "usb:\Myfiles\%s.arb"'%file_name)
        instr.write('SOUR1:BURS:NCYC %i' % nocyc)
        instr.write('TRIG1:SOUR BUS')
        instr.write('SOUR1:BURS:STAT ON')
        instr.write('OUTP1:STAT ON')
        instr.write('SOUR1:BURST:PHASE %f'%pha)
        instr.write('SOUR1:BURS:INT:PER %f'%per)
        instr.write('SOUR1:BURS:STAT ON')
        instr.write('OUTP1:STAT ON')
        instr.write('SOUR%i:BURST:PHASE %f' % (channel, pha))
        instr.write('SOUR%i:BURS:INT:PER %f' % (channel, per))
        instr.write('SOUR%i:BURS:STAT ON' % channel)
        instr.write('OUTP%i:STAT ON' % channel)
