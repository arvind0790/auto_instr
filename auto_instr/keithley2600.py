class ke2600(object):
    def off(instr,ch=1):
        if ch==1:
            instr.write("smua.source.output=smua.OUTPUT_OFF")
        if ch==2:
            instr.write("smub.source.output=smub.OUTPUT_OFF")
    def on(instr,ch=1):
        if ch==1:
            instr.write("smua.source.output=smua.OUTPUT_ON")
        if ch==2:
            instr.write("smub.source.output=smub.OUTPUT_ON")
    def forImeasV(instr, current, volt_cmpl, ch=1):
        if ch==1:
            instr.write('display.smua.measure.func = display.MEASURE_DCVOLTS')
            instr.write('smua.source.func = smua.OUTPUT_DCAMPS')
            instr.write('smua.source.limitv = %f'%volt_cmpl)
            instr.write("smua.source.leveli = %f"%current)
            instr.write("smua.source.output=smua.OUTPUT_ON")
            instr.write("currenta, voltagea = smua.measure.iv()")
            volt_data = instr.ask("print(voltagea)")
        if ch==2:
            instr.write('display.smub.measure.func = display.MEASURE_DCVOLTS')
            instr.write('smub.source.func = smub.OUTPUT_DCAMPS')
            instr.write('smub.source.limitv = %f'%volt_cmpl)
            instr.write("smub.source.leveli = %f"%current)
            instr.write("smub.source.output=smub.OUTPUT_ON")
            instr.write("currentb, voltageb = smub.measure.iv()")
            volt_data = instr.ask("print(voltageb)")
        return volt_data
    def forVmeasI(instr, voltage, curr_cmpl , ch=1):
        if ch==1:
            instr.write('display.smua.measure.func = display.MEASURE_DCAMPS')
            instr.write('smua.source.func = smua.OUTPUT_DCVOLTS')
            instr.write('smua.source.limiti = %f'%curr_cmpl)
            instr.write("smua.source.levelv = %f"%voltage)
            instr.write("smua.source.output=smua.OUTPUT_ON")
            instr.write("currenta, voltagea = smua.measure.iv()")
            curr_data = instr.ask("print(currenta)")
        if ch==2:
            instr.write('display.smub.measure.func = display.MEASURE_DCAMPS')
            instr.write('smub.source.func = smub.OUTPUT_DCVOLTS')
            instr.write('smub.source.limiti = %f' % curr_cmpl)
            instr.write("smub.source.levelv = %f" % voltage)
            instr.write("smub.source.output=smub.OUTPUT_ON")
            instr.write("currentb, voltageb = smub.measure.iv()")
            curr_data = instr.ask("print(currentb)")
        return curr_data
    def forVmeasV(instr, voltage, volt_cmpl ,ch=1):
        if ch==1:
            instr.write('smua.sense = smua.SENSE_REMOTE')
            instr.write('display.smua.measure.func = display.MEASURE_DCVOLTS')
            instr.write('smua.source.func = smua.OUTPUT_DCVOLTS')
            instr.write('smua.source.limitv = %f'%volt_cmpl)
            instr.write("smua.source.levelv = %f"%voltage)
            instr.write("smua.source.output=smua.OUTPUT_ON")
            instr.write("currenta, voltagea = smua.measure.iv()")
            curr_data = instr.ask("print(voltagea)")
        if ch==2:
            instr.write('smub.sense = smub.SENSE_REMOTE')
            instr.write('display.smub.measure.func = display.MEASURE_DCVOLTS')
            instr.write('smub.source.func = smub.OUTPUT_DCVOLTS')
            instr.write('smub.source.limitv = %f' % volt_cmpl)
            instr.write("smub.source.levelv = %f" % voltage)
            instr.write("smub.source.output=smub.OUTPUT_ON")
            instr.write("currentb, voltageb = smub.measure.iv()")
            curr_data = instr.ask("print(voltageb)")
        return curr_data
    def autorang_forVmeasI(instr,ch=1):
        if ch==1:
            instr.write('smua.measure.autorangei = smua.AUTORANGE_ON')
            instr.write('smua.source.autorangev = smua.AUTORANGE_ON')
        if ch==2:
            instr.write('smub.measure.autorangei = smub.AUTORANGE_ON')
            instr.write('smub.source.autorangev = smub.AUTORANGE_ON')
    def autorang_forImeasV(instr,ch=1):
        if ch==1:
            instr.write('smua.measure.autorangev = smua.AUTORANGE_ON')
            instr.write('smua.source.autorangei = smua.AUTORANGE_ON')
        if ch==2:
            instr.write('smub.measure.autorangev = smub.AUTORANGE_ON')
            instr.write('smub.source.autorangei = smub.AUTORANGE_ON')
