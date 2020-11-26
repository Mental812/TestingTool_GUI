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

        self.__TestingItem_list = []

        self.__get_BSP_Name()
        self.__TestingItem_list = self.__get_TestingItem()

    def get_Information(self):
        if self.__TestingItem_list == []:
            Support = "No"
        else :
            Support = "Yes"

        return self.__BSP_String ,self.__JetPack_String ,self.__Camera,Support

    def get_TestingItem_list(self):
        testingitem_name = []
        testingeitem_bool =[]
        for list_value in self.__TestingItem_list:
            if list_value[1] != 0:
                testingitem_name.append(list_value[0])

        return testingitem_name
    
    def __get_BSP_Name(self):
        try:
            BSP_file = open("/proc/device-tree/nvidia,dtsfilename","r")
            BSP_Text = BSP_file.read()
        except:
            BSP_Text ="R32_4_3_Xavier-NX_AN810_1.dts"

        BSP_list = BSP_Text.split("_")
        self.__BSP_list = BSP_list
        self.__BSP_String = BSP_list[0] + "_" + BSP_list[1] + "_" + BSP_list[2]
        self.__JetPack_String = "4." + BSP_list[1]
        #print(BSP_list[3],"\n")
        if len(BSP_list) >= 7:
            self.__Camera = BSP_list[5]
        else: 
            self.__Camera = "NO Camera"
            
        
        #print(self.__TestingItem_list)


    def __get_TestingItem(self):
        Testing_x = None
        TestingItem_list = []
        dir_data = './data/'
        f_app = os.path.join(dir_data, 'TestingItem_2.csv')
        #print('Path of read in data: %s' % (f_app))
        TestingItem = pd.read_csv(f_app)
        TestingItem_Col = TestingItem.columns.values.tolist()

        for i in range(TestingItem.shape[0]) :
            if TestingItem['Module'][i] == self.__BSP_list[3]:
                if TestingItem['Board'][i] == self.__BSP_list[4]:
                    #print("this BSP is ",TestingItem['Module'][i],"_",TestingItem['Board'][i])
                    Testing_x = i
                    break
        
        if Testing_x is not None:
            for t_col in TestingItem_Col:
                #print(TestingItem[t_col][Testing_x])
                TestingItem_list.append([t_col,TestingItem[t_col][Testing_x]])
        else:
            TestingItem_list = []

        #print(TestingItem_list)
        return  TestingItem_list
            
                
