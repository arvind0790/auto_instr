class hp3458(object):
        
    def read_DCV(instr):
        instr.write('RESET;END ALWAYS;DCV;TARM HOLD;TARM SGL')
        data=instr.read()
        return data
    def read_ACV(instr):
        instr.write('RESET;END ALWAYS;ACV;TARM HOLD;TARM SGL')
        data=instr.read()
        return data
    def read_DCI(instr):
        instr.write('RESET;END ALWAYS;DCI;TARM HOLD;TARM SGL')
        data=instr.read()
        return data
    def read_ACI(instr):
        instr.write('RESET;END ALWAYS;ACI;TARM HOLD;TARM SGL')
        data=instr.read()
        return data

