import visa
rm = visa.ResourceManager()
# rm = visa.ResourceManager('@py')
class gpib(object):
    def addr(gpib_no,gpib_port):
        add_var = 'GPIB%d::%d::INSTR' % (gpib_no,gpib_port)
        inst = rm.open_resource(add_var)
        return inst

class serial(object):
    def addr(port):
        add_var = 'ASRL%d::INSTR' %port
        inst = rm.open_resource(add_var)
        return inst

class lan(object):
    def addr(ip):
        add_var = 'TCPIP0::%s::inst0::INSTR' %ip
        inst = rm.open_resource(add_var)
        return inst

class lan_debug(object):
    def addr(ip):
        add_var = ip
        inst = rm.open_resource(add_var)
        return inst

class usb(object):
    def addr(usbid):
        add_var = 'USB0::%s::INSTR' %usbid
        inst = rm.open_resource(add_var)
        return inst

class usb_debug(object):
    def addr(usbid):
        add_var = usbid
        inst = rm.open_resource(add_var)
        return inst

class enumerate():
    @staticmethod
    def all_resources():
        all_res = rm.list_resources()
        print(all_res)
        return all_res

    @staticmethod
    def IDN():
        list = enumerate.all_resources()
        valid_res =[]
        for res in list:
            try:
                print('Pinging - %s' %res)
                open_res = rm.open_resource(res)
                print('Link opened')
                idn_query = open_res.query('*IDN?')
                print(idn_query)
                valid_res.append([res,idn_query])
                open_res.close()
            except:
                print('Communication failed')
                pass
        print(valid_res)
        return valid_res
