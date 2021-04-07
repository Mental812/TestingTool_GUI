
import socket,fcntl,struct

class libLanClass():
    def __init__(self):
        pass
    def get_ip_address(self,ifname):
        try:    
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            location = (socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', bytes(ifname[:15],'utf-8')))[20:24]), 80)
            result_of_check = s.connect_ex(location)
            if result_of_check == 0:
                return True
            else:
                return False
        except Exception as e:
            #print(e)
            return False