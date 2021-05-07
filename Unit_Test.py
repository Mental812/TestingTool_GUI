import os 
from utils.libTestOfBoard_Class import libTest_Class

libtest = libTest_Class()
board_type = ['Xavier-NX','AIE-CN12','0']
libtest.import_boardtype(board_type)

print("-----------------Test LAN----------------")
print(libtest.TOB_LAN_testing())
print("-----------------------------------------")

print("-----------------Test WIFI---------------")
print(libtest.TOB_WIFI_testing())
print("-----------------------------------------")

print("-----------------Test SDCard-------------")
print(libtest.TOB_SDCARD_testing())
print("-----------------------------------------")
