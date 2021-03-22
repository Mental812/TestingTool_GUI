import os
import sys
class libTest_Class():
    def __init__(self):
        self.__module = None
        self.__board = None
        self.__camera = None
    
    def import_boardtype(self,board_type):
        self.__module = board_type[0]
        self.__board = board_type[1]
        self.__camera = board_type[2]         

    def TOB_LAN_testing(self):
        pass
    def TOB_WIFI_testing(self):
        pass
    def TOB_BT_testing(self):
        pass
    def TOB_SDCARD_testing(self):
        pass
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