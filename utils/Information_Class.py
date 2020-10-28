import os


class Information_Class():
    def __init__(self):
        self.__BSP_String = "Wait"
        self.__JetPack_String = "Wait"
        self.__Camera = "None"

    def get_Information(self):
        self.__get_BSP_Name()
        return self.__BSP_String ,self.__JetPack_String ,self.__Camera
    
    def __get_BSP_Name(self):
        BSP_file = open("/proc/device-tree/nvidia,dtsfilename","r")
        BSP_Text = BSP_file.read()
        BSP_list = BSP_Text.split("_")
        self.__BSP_String = BSP_list[0] + "_" + BSP_list[1] + "_" + BSP_list[2]
        self.__JetPack_String = "4." + BSP_list[1]
        if len(BSP_list) >= 7:
            self.__Camera = BSP_list[5]
        else: 
            self.__Camera = "NO Camera"