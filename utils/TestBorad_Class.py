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
        self.__Run_Test()
    
    def __Run_Test(self):
        print(self.__Board_type)
        self.run_thread = threading.Thread(target = self.__Running_commend)
        self.run_thread.start()

    def __Running_commend(self):
        #print(self.running_commend)
        #list_a = self.running_commend.split(" ")
        #print(list_a)
        #self.running_cmd = subprocess.Popen(list_a)
        #os.system(self.running_commend)
        #print("----end----")
        pass