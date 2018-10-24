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
        elif shape == 'SIN':
            instr.write('SOUR%i:FUNC:SHAP SIN' %channel)
        elif shape == 'RAMP':
            instr.write('SOUR%i:FUNC:SHAP RAMP' %channel)
        elif shape == 'PULS':
            instr.write('SOUR%i:FUNC:SHAP PULS' %channel)
            instr.write('SOUR%i:PULS:DCYC %f'%duty_cycle)
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

