import os
import sys
from libLan_Class import libLanClass
class libTest_Class():
    def __init__(self):
        self.__device_info = {"module","board","Camera"}
    
    def import_boardtype(self,board_type):
        self.__device_info = {"module" : board_type[0],"board":board_type[1],"Camera":board_type[2]}
        #print(self.__device_info)

    def TOB_LAN_testing(self):
        lan_test = libLanClass()
        if lan_test.get_ip_address('eth0') is True:  # '192.168.0.110'
            return True
        else:
            return False


    def TOB_WIFI_testing(self):
        lan_test = libLanClass()
        if lan_test.get_ip_address('wlan0') is True:  # '192.168.0.110'
            return True
        else:
            return False

    def TOB_BT_testing(self):
        pass

    def TOB_SDCARD_testing(self):
        if os.path.exists("/dev/mmcblk1p1"):
            print("storage is true")
        else:
            print("storage is not exist")
        

        
    def TOB_MSATA_testing(self):
        pass
    def TOB_MPCIE_testing(self):
        pass
    def TOB_RS232_testing(self):
        pass
    def TOB_UART_Testing(self):
        pass
    def TOB_UART2_Testing(self):
        pass
    def TOB_UART_CSI_Testing(self):
        pass
    def TOB_GPIO_Testing(self):
        pass
    def TOB_FAN_Testing(self):
        pass
    def TOB_EDP_Testing(self):
        pass
    def TOB_CANbus_Testing(self):
        pass
    def TOB_I2C_Testing(self):
        pass
    def TOB_I2C_II_Testing(self):
        pass
    def TOB_I2C_CSI_Testing(self):
        pass
    def TOB_SPI_testing(self):
        pass
    def TOB_USB_Micro_Testing(self):
        pass
    def TOB_USB_A_Testing(self):
        pass
    def TOB_USB_C_Testing(self):
        pass
    def TOB_M2_EKEY_Testing(self):
        pass
    def TOB_M2_BKEY_Testing(self):
        pass
    def TOB_M2_MKEY_SATA_Testing(self):
        pass
    def TOB_M2_MKEY_PCIE_Testing(self):
        pass
    def TOB_EEPROM_Testing(self):
        pass
    def TOB_Camera_Testing(self):
        pass
    def TOB_Temperature_Testing(self):
        pass