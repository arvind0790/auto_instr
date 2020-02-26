class ke2000(object):
    
    ## DC VOLTAGE##
    def read_DCV(instr,integration_rate = 1, auto_range_en =1 ,filter_en=0,filter_type = 'MOV',
                 filter_average_count=10):
        #integration rate can vary from 0.01 to 10
        #for filter_type repeat pass 'REP'
        instr.write("*CLS")
        instr.write('INIT:CONT OFF;:ABORT')
        instr.write("SENS:FUNC 'VOLT:DC'")
        instr.write('SENS:VOLT:DC:NPLC %f' %integration_rate)
        instr.write('SENS:VOLT:DC:RANG:AUTO %i' %auto_range_en)
        instr.write('SENS:VOLT:DC:DIG 7')
        instr.write('SENS:VOLT:DC:AVER:STAT %i' %filter_en)
        instr.write('SENS:VOLT:DC:AVER:TCON %s' %filter_type)
        instr.write('SENS:VOLT:DC:AVER:COUN %i' %filter_average_count)
        instr.write('FORM:ELEM READ')
        instr.write('TRIG:COUN 1')
        instr.write('SAMP:COUN 1')
        instr.write('TRIG:DEL 0')
        instr.write('TRIG:SOUR IMM')
        instr.write(':READ?')
        data= instr.read()
        return data

    ## DC CURRENT##
    def read_DCI(instr,integration_rate = 1, auto_range_en =1 ,filter_en=0,filter_type = 'MOV',
                 filter_average_count=10):
        # integration rate can vary from 0.01 to 10
        # for filter_type repeat pass 'REP'
        instr.write("*CLS")
        instr.write('INIT:CONT OFF;:ABORT')
        instr.write("SENS:FUNC 'CURR:DC'")
        instr.write('SENS:CURR:DC:NPLC %f' %integration_rate)
        instr.write('SENS:CURR:DC:RANG:AUTO %i' %auto_range_en)
        instr.write('SENS:CURR:DC:DIG 7')
        instr.write('SENS:CURR:DC:AVER:STAT %i' %filter_en)
        instr.write('SENS:CURR:DC:AVER:TCON %s' %filter_type)
        instr.write('SENS:CURR:DC:AVER:COUN %i' %filter_average_count)
        instr.write('FORM:ELEM READ')
        instr.write('TRIG:COUN 1')
        instr.write('SAMP:COUN 1')
        instr.write('TRIG:DEL 0')
        instr.write('TRIG:SOUR IMM')
        instr.write(':READ?')
        data= instr.read()
        return data

    #####   RESISTANCE   ########
    def read_RES(instr,integration_rate = 1,auto_range_en =1 ,filter_en=0,filter_type = 'MOV',filter_average_count=10):
        # integration rate can vary from 0.01 to 10
        # for filter_type repeat pass 'REP'
        instr.write("*CLS")
        instr.write('INIT:CONT OFF;:ABORT')
        instr.write("SENS:FUNC 'RES'")
        instr.write('SENS:RES::NPLC %f' %integration_rate)
        instr.write('SENS:RES:RANG:AUTO %i' %auto_range_en)
        instr.write('SENS:RES:DIG 7')
        instr.write('SENS:RES:AVER:STAT %i' % filter_en)
        instr.write('SENS:RES:AVER:TCON %s' % filter_type)
        instr.write('SENS:RES:AVER:COUN %i' % filter_average_count)
        instr.write('FORM:ELEM READ')
        instr.write('TRIG:COUN 1')
        instr.write('SAMP:COUN 1')
        instr.write('TRIG:DEL 0')
        instr.write('TRIG:SOUR IMM')
        instr.write(':READ?')
        data= instr.read()
        return data

    #####    AC VOLTAGE   #########
    def read_ACV(instr,integration_rate = 1, auto_range_en =1 ,filter_en=0,filter_type = 'MOV',
                 filter_average_count=10,bandwidth = 30): #BW can lie between 3 to 300e3
        instr.write("*CLS")
        instr.write('INIT:CONT OFF;:ABORT')
        instr.write("SENS:FUNC 'VOLT:AC'")
        instr.write('SENS:VOLT:AC:NPLC %f' %integration_rate)
        instr.write('SENS:VOLT:AC:RANG:AUTO %i' %auto_range_en)
        instr.write('SENS:VOLT:AC:DIG 7')
        instr.write('SENS:VOLT:AC:AVER:STAT %i' %filter_en)
        instr.write('SENS:VOLT:AC:AVER:TCON %s' %filter_type)
        instr.write('SENS:VOLT:AC:AVER:COUN %i' %filter_average_count)
        instr.write('SENS:VOLT:AC:DET:BAND %f' % bandwidth)
        instr.write('FORM:ELEM READ')
        instr.write('TRIG:COUN 1')
        instr.write('SAMP:COUN 1')
        instr.write('TRIG:DEL 0')
        instr.write('TRIG:SOUR IMM')
        instr.write(':READ?')
        data= instr.read()
        return data
    ## AC CURRENT##
    def read_ACI(instr,integration_rate = 1, auto_range_en =1 ,filter_en=0,filter_type = 'MOV',
                 filter_average_count=10, bandwidth = 30): #BW can lie between 3 to 300e3
        instr.write("*CLS")
        instr.write('INIT:CONT OFF;:ABORT')
        instr.write("SENS:FUNC 'CURR:AC'")
        instr.write('SENS:CURR:AC:NPLC %f' %integration_rate)
        instr.write('SENS:CURR:AC:RANG:AUTO %i' %auto_range_en)
        instr.write('SENS:CURR:AC:DIG 7')
        instr.write('SENS:CURR:AC:AVER:STAT %i' %filter_en)
        instr.write('SENS:CURR:AC:AVER:TCON %s' %filter_type)
        instr.write('SENS:CURR:AC:AVER:COUN %i' %filter_average_count)
        instr.write('SENS:CURR:AC:DET:BAND %f' %bandwidth)
        instr.write('FORM:ELEM READ')
        instr.write('TRIG:COUN 1')
        instr.write('SAMP:COUN 1')
        instr.write('TRIG:DEL 0')
        instr.write('TRIG:SOUR IMM')
        instr.write(':READ?')
        data= instr.read()
        return data
