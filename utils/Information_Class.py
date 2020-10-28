import os
import pandas as pd
import numpy as np

class Information_Class():
    def __init__(self):
        self.__BSP_String = "Wait"
        self.__JetPack_String = "Wait"
        self.__Camera = "None"
        self.__BSP_list = []
        self.__dir_data = './data/TestingItem.csv'
        self.__get_BSP_Name()
    def get_Information(self):
        
        return self.__BSP_String ,self.__JetPack_String ,self.__Camera
    
    def __get_BSP_Name(self):
        BSP_file = open("/proc/device-tree/nvidia,dtsfilename","r")
        BSP_Text = BSP_file.read()
        BSP_list = BSP_Text.split("_")
        self.__BSP_list = BSP_list
        self.__BSP_String = BSP_list[0] + "_" + BSP_list[1] + "_" + BSP_list[2]
        self.__JetPack_String = "4." + BSP_list[1]
        print(BSP_list[3],"\n")
        if len(BSP_list) >= 7:
            self.__Camera = BSP_list[5]
        else: 
            self.__Camera = "NO Camera"
        self.__get_TestingItem()
    def __get_TestingItem(self):
        dir_data = './data/'
        f_app = os.path.join(dir_data, 'TestingItem_2.csv')
        #print('Path of read in data: %s' % (f_app))
        TestingItem = pd.read_csv(f_app)
        print(TestingItem.shape[0])
        for i in range(TestingItem.shape[0]) :
            if TestingItem['Module'][i] == self.__BSP_list[3]:
                if TestingItem['Board'][i] == self.__BSP_list[4]:
                    print("this BSP is ",TestingItem['Module'][i],"_",TestingItem['Board'][i])
                    print("\n",)
                    print(TestingItem.ix[i])
                    break
                
                
