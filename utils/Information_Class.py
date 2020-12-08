import os
import pandas as pd
import numpy as np
import configparser

class Information_Class():
    def __init__(self,Path):
        self.__BSP_String = "Wait"
        self.__JetPack_String = "Wait"
        self.__Camera = "None"
        self.__dir_data = Path

        self.__BSP_list = []
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
            if list_value[1] != 0 and list_value[1] != '0':
                testingitem_name.append(list_value[0])
                testingeitem_bool.append(list_value[1])
        return testingitem_name,testingeitem_bool
    
    def __get_BSP_Name(self):
        try:
            BSP_file = open("/proc/device-tree/nvidia,dtsfilename","r")
            BSP_Text = BSP_file.read()
        except:
            BSP_Text ="R32_4_3_Xavier-NX_AN110_Camera_IMX290_Dual_1.dts"

        BSP_list = BSP_Text.split("_")
        self.__BSP_list = BSP_list
        self.__BSP_String = BSP_list[0] + "_" + BSP_list[1] + "_" + BSP_list[2]
        self.__JetPack_String = "4." + BSP_list[1]
        #print(BSP_list[3],"\n")
        
        
        if len(BSP_list) == 9:
            self.__Camera = BSP_list[6] + "_" + BSP_list[7]
        elif len(BSP_list) == 8:
            self.__Camera = BSP_list[6]
        elif len(BSP_list) == 10:
            self.__Camera = BSP_list[6] + "_" + BSP_list[7] + "_" + BSP_list[8] 
        else: 
            self.__Camera = "NO Camera"
        
        
        #print(self.__TestingItem_list)

    def __get_TestingItem(self):
        Testing_x = None #確認對到csv的哪一列
        TestingItem_list = [] #測試的總項目
        dir_data = './data/'
        f_app = os.path.join(dir_data, 'TestingItem_2.csv')
        #print('Path of read in data: %s' % (f_app))
        TestingItem = pd.read_csv(f_app)
        TestingItem_Col = TestingItem.columns.values.tolist()

        for i in range(TestingItem.shape[0]) :
            if TestingItem['Module'][i] == self.__BSP_list[3]:
                if TestingItem['Board'][i] == self.__BSP_list[4]:

                    if self.__Camera == "NO Camera":
                        Testing_x = i
                        break
                    elif TestingItem['Camera'][i] == self.__Camera:
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
            
class Config_Class():

    def __init__(self,Path):
        self.Path = Path
        self.config = configparser.ConfigParser()
        self.config.read(Path)
        
    def get_items_value(self,name):
        name_lower = str.lower(name)
        val = self.config.get("items", name_lower)
        return val

    def write_items_value(self,name,value):
        name_lower = str.lower(name)
        self.config.set("items",name_lower,value)
        self.config.write(open(self.Path, "w"))


    def get_infos_value(self):
        gondan = self.config.get("infos","gondannumber")
        part = self.config.get("infos","partnumber")
        board = self.config.get("infos","boardnumber")
        return gondan,part,board
        
    def write_gondanpart_infos(self,gondanpart):
        try:
            list_gondanpart = gondanpart.split(" ",1)
            self.config.set("infos","gondannumber","\""+list_gondanpart[0]+"\"")
            self.config.set("infos","partnumber","\""+list_gondanpart[1]+"\"")
            self.config.write(open(self.Path, "w"))
        except:
            return False
        #print(list_gondanpart)

    
    def write_board_infos(self,boardnumber):
        #print(boardnumber)
        self.config.set("infos","boardnumber","\""+boardnumber+"\"")
        self.config.write(open(self.Path, "w"))