import os
import pandas as pd
import numpy as np
import configparser

class Information_Class():
    def __init__(self,Path):
        self.__device_info = {"module":"None","board":"None","Camera":"No Camera","Jetpack":"None","BSP":"None"}
   
        self.__JetPack_String = "Wait"

        self.__dir_data = Path

        self.__get_BSP_Name()
        self.__TestingItem_list = self.__get_TestingItem()

    def get_Information(self):
        if self.__TestingItem_list == []:
            Support = "No"
        else :
            Support = "Yes"

        return self.__device_info["BSP"],self.__device_info["Jetpack"],self.__device_info["Camera"],Support

    def get_TestingItem_list(self):
        testingitem_name = []
        testingeitem_bool =[]
        for list_value in self.__TestingItem_list:
            if list_value[1] != 0 :#and list_value[1] != '0':
                testingitem_name.append(list_value[0])
                testingeitem_bool.append(list_value[1])
        return testingitem_name,testingeitem_bool
    

    def __get_BSP_Name(self): #Get BSP name from dts.
        try:
            BSP_file = open("/proc/device-tree/nvidia,dtsfilename","r")
            BSP_Text = BSP_file.read()
        except:
            BSP_Text ="R32_4_3_Xavier-NX_AN110_Camera_IMX290_Dual_1.dts"
        

        BSP_list = BSP_Text.split("_")

        if "AIE-CN" in BSP_list[3]:
            module = "Xavier-NX"
            board = BSP_list[3]
        elif "AIE-CO" in BSP_list[3]:
            module = "Nano"
            board = BSP_list[3]
        else:
            module = BSP_list[3]
            board = BSP_list[4]

        if BSP_list[0] == "R32":
            Jetpack = "4." + BSP_list[1] + "." + BSP_list[2]

        if "Camera" in BSP_list:
            camera_list = []
            for i in range(len(BSP_list)):
                if "Camera" in BSP_list[i]:
                    camera_start = i + 1
                if "1.dts" in  BSP_list[i]:
                    camera_end = i
            for i in range(camera_start,camera_end):
                camera_list.append(BSP_list[i])
            
            self.__device_info["Camera"] = "_".join(camera_list)
            
        self.__device_info["BSP"] = BSP_Text
        self.__device_info["module"] = module 
        self.__device_info["board"] = board
        self.__device_info["Jetpack"] = Jetpack
    def __get_TestingItem(self): #Get Test item form csv file.

        Testing_x = None #確認對到csv的哪一列
        TestingItem_list = [] #測試的總項目
        f_app = os.path.join(self.__dir_data)
        #print('Path of read in data: %s' % (f_app))
        TestingItem = pd.read_csv(f_app)
        TestingItem_Col = TestingItem.columns.values.tolist()
        module = self.__device_info["module"]
        board = self.__device_info["board"]
        camera = self.__device_info["Camera"]

        for i in range(TestingItem.shape[0]) :
            if TestingItem['Module'][i] == module:
                if TestingItem['Board'][i] == board:
                    if camera == "No Camera":
                        Testing_x = i
                        break
                    elif TestingItem['Camera_module'][i] == self.__device_info["Camera"]:
                        Testing_x = i
                        break
        
        if Testing_x is not None:
            for item in TestingItem_Col:
                TestingItem_list.append([item,TestingItem[item][Testing_x]])
        else:
            TestingItem_list = []

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