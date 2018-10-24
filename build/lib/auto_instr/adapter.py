import visa
rm = visa.ResourceManager()
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