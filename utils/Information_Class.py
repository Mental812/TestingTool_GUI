import os


class Information_Class():
    def __init__(self):
        self.__BSP_String = "Wait"
        self.__JetPack_String = "Wait"
        self.__Camera = False

    def get_Information(self):
        return self.__BSP_String ,self.__JetPack_String ,self.__Camera
    
    def __get_BSP_Name(self):
        BSP_file = open("","r")
        BSP_Text = BSP_file.read()