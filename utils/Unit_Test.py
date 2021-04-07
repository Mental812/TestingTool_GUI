from libTestOfBoard_Class import libTest_Class

libtest = libTest_Class()

print("-----------------Test LAN----------------")
libtest.TOB_LAN_testing()
print("-----------------------------------------")
print("-----------------Test WIFI---------------")
libtest.TOB_WIFI_testing()
print("-----------------------------------------")



'''
import usb.util
import sys
all_devs = usb.core.find(find_all=True)
for d in all_devs:
    try:
        if d.bcdUSB == 0x300 or d.bcdUSB == 0x200:
            if d.bDeviceClass == 0x0 :
                print(d)
        
    except Exception as e:
        print(e)
        pass
'''