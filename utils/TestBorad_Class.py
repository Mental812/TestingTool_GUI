import os 
import sys 
import threading
sys.path.append("./utils")

class Test_Class():
    def __init__(self,Config_class,Libtest_class):
        self.__Board_type = []
        self.__Test_item = []
        self.__config = Config_class
        self.__libTest_Class = Libtest_class

    def Start_Test(self,board_type,testitem):
        self.__Board_type = board_type
        self.__libTest_Class.import_boardtype(board_type)
        self.__Test_item = testitem
        return self.__Running_commend()
        #print(self.__Board_type, self.__Test_item)
        #self.__Run_Test()
    
    def __Run_Test(self):
        #print(self.__Board_type)
        self.run_thread = threading.Thread(target = self.__Running_commend)
        self.run_thread.start()

    def __Running_commend(self):
        if "LAN" in self.__Test_item:
            result = self.__libTest_Class.TOB_LAN_testing()
            return result
        if "WIFI" in self.__Test_item:
            result = self.__libTest_Class.TOB_WIFI_testing()
        if "BT" in self.__Test_item:
            result = self.__libTest_Class.TOB_BT_testing()
        if "SDCARD" in self.__Test_item:
            result = self.__libTest_Class.TOB_SDCARD_testing()
        if "MSATA" in self.__Test_item:
            result = self.__libTest_Class.TOB_MSATA_testing()
        if "MPCIE" in self.__Test_item:
            result = self.__libTest_Class.TOB_MPCIE_testing()
        if "RS232" in self.__Test_item:
            result = self.__libTest_Class.TOB_RS232_testing()
        if "UART" in self.__Test_item:
            result = self.__libTest_Class.TOB_UART_Testing()
        if "UART2" in self.__Test_item:
            result = self.__libTest_Class.TOB_UART2_Testing()
        if "UART_CSI" in self.__Test_item:
            result = self.__libTest_Class.TOB_UART_CSI_Testing()
        if "GPIO" in self.__Test_item:
            result = self.__libTest_Class.TOB_GPIO_Testing()
        if "FAN" in self.__Test_item:
            result = self.__libTest_Class.TOB_FAN_Testing()
        if "eDP" in self.__Test_item:
            result = self.__libTest_Class.TOB_EDP_Testing()
        if "CANbus" in self.__Test_item:
            result = self.__libTest_Class.TOB_CANbus_Testing()
        if "I2C" in self.__Test_item:
            result = self.__libTest_Class.TOB_I2C_Testing()
        if "I2C_II" in self.__Test_item:
            result = self.__libTest_Class.TOB_I2C_II_Testing()
        if "I2C_CSI" in self.__Test_item:
            result = self.__libTest_Class.TOB_I2C_CSI_Testing()
        if "SPI" in self.__Test_item:
            result = self.__libTest_Class.TOB_SPI_testing()
        if "USB_MICRO" in self.__Test_item:
            result = self.__libTest_Class.TOB_USB_Micro_Testing()
        if "USB_A" in self.__Test_item:
            result = self.__libTest_Class.TOB_USB_A_Testing()
        if "USB_C" in self.__Test_item:
            result = self.__libTest_Class.TOB_USB_C_Testing()
        if "M2EKEY" in self.__Test_item:
            result = self.__libTest_Class.TOB_M2_EKEY_Testing()
        if "M2BKEY" in self.__Test_item:
            result = self.__libTest_Class.TOB_M2_BKEY_Testing()
        if "M2MKEY_SATA" in self.__Test_item:
            result = self.__libTest_Class.TOB_M2_MKEY_SATA_Testing()
        if "M2MKEY_PCIE" in self.__Test_item:
            result = self.__libTest_Class.TOB_M2_MKEY_PCIE_Testing()
        if "EEPROM" in self.__Test_item:
            result = self.__libTest_Class.TOB_EEPROM_Testing()
        if "CAMERA" in self.__Test_item:
            result = self.__libTest_Class.TOB_Camera_Testing()
        if "TEMPERATURE" in self.__Test_item:
            result = self.__libTest_Class.TOB_Temperature_Testing()