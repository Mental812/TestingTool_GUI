import sys
import time	
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from utils.UI_Class import Ui_MainWindow
from utils.Information_Class import Information_Class,Config_Class


Config_Path = "./data/config.ini"
TestingItem_Path = "./data/TestingItem.csv"

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.Conf_class = Config_Class(Config_Path) #讀取config class
        self.Info_class = Information_Class(TestingItem_Path) #讀取csv class
        self.pushButton_start.setEnabled(False)
        self.lineEdit_message.setReadOnly(True)
        self.textEdit_gondan.setFocus() #自動換行至選取位置
        self.lineEdit_board.setMaxLength(11)
        self.__debug_item = []
        self.__auto_item = []
        self.__set_callback() #設定callback

    def init_information(self): #設定初始值
        BSP,JetPack,Camera,Support = self.Info_class.get_Information()
        # 設定BSP,Jetpacek,Camera版本
        self.lineEdit_BSP.setText(BSP) 
        self.lineEdit_JetPack.setText(JetPack)
        self.lineEdit_Camera.setText(Camera)
        self.lineEdit_message.setText("-----請掃描工單及品號條碼-----")
        # 設定是否support目前的板子
        if Support == "Yes":
            self.lineEdit_Support.setStyleSheet("background: green;") #設定背景顏色
            TestingItem_Name,Testing_Bool = self.Info_class.get_TestingItem_list() #獲取總測試項目
            
            #self.__set_TableView(TestingItem_Name,Testing_Bool)
            self.__set_tableWidget_Status_Init(TestingItem_Name,Testing_Bool)
            self.__auto_item = TestingItem_Name
            #print(Testing_Bool)
        elif Support == "No":
            self.lineEdit_Support.setStyleSheet("background: red;")
        self.lineEdit_Support.setText(Support)

    def __set_callback(self):
        self.textEdit_gondan.textChanged.connect(self.__check_gondan_max_lan)
        self.lineEdit_board.textChanged.connect(self.__check_board_max_len)
        self.pushButton_start.clicked.connect(self.__click_pushbottom_start)
        self.actionExit.triggered.connect(self.__click_action_Exit)
        self.actionDebug.triggered.connect(self.__click_action_Debug)
        
    def __check_gondan_max_lan(self):
        text =  self.textEdit_gondan.toPlainText()
        #print(len(text))
        if len(text) >= 33:
            self.textEdit_gondan.setStyleSheet("background: green;") #設定背景顏色
            self.textEdit_gondan.setEnabled(False) #不可編輯
            self.lineEdit_board.setFocus()
            self.lineEdit_message.setText("-----請掃描底板序號條碼-----")
            self.Conf_class.write_gondanpart_infos(text)

    def __check_board_max_len(self):
        text = self.lineEdit_board.text()
        #print(len(text))
        if len(text) >= 11:
            self.lineEdit_board.setStyleSheet("background: green;") #設定背景顏色
            self.lineEdit_board.setEnabled(False) #不可編輯
            self.Conf_class.write_board_infos(text)
            self.pushButton_start.setEnabled(True) #開啟按鍵
            self.pushButton_start.setFocus()
            self.lineEdit_message.setText("-----點按[start]開始-----")

    def __click_pushbottom_start(self): #未完成
        self.pushButton_start.setEnabled(False)
        if self.actionDebug.isChecked() :
            print(self.__debug_item)
        else:
            print(self.__auto_item)

    def __click_action_Exit(self):
        sys.exit(0) 

    def __click_action_Debug(self): #debug模式控制
        if self.actionDebug.isChecked() :  #"如果debug被觸發"
            #message#
            self.lineEdit_message.setStyleSheet("background: green;") 
            self.lineEdit_message.setText("-----Debug Mode (Please doubleclick item)-----")
            self.textEdit_gondan.setEnabled(False)
            self.lineEdit_board.setEnabled(False)
            #設定callback
            self.tableWidget_Status.doubleClicked.connect(self.__click_tableWidget_Status_debug)
            self.pushButton_start.setEnabled(True)
        else :
            self.lineEdit_message.setStyleSheet("background: white;") 
            self.lineEdit_message.setText("-----請掃描工單及品號條碼-----")
            self.tableWidget_Status.disconnect()
            self.pushButton_start.setEnabled(False)
            self.textEdit_gondan.setEnabled(True)
            self.lineEdit_board.setEnabled(True)
            self.__debug_item = []

            TestingItem_Name,Testing_Bool = self.Info_class.get_TestingItem_list() #獲取總測試項目
            self.__set_tableWidget_Status_Init(TestingItem_Name,Testing_Bool)
    def __click_tableWidget_Status_debug(self):
        index = self.tableWidget_Status.currentIndex()
        value=index.sibling(index.row(),index.column()).data()
        print(index.column())
        #print(value)
        if value in self.__debug_item:
            print("remove :",value)
            self.__debug_item.remove(value)
            self.tableWidget_Status.item(index.row(),1).setBackground(QBrush(QColor(255,255,255)))
            self.tableWidget_Status.item(index.row(),1).setText("-----")
        else:
            print("add :",value)
            self.__debug_item.append(value)
            self.tableWidget_Status.item(index.row(),1).setBackground(QBrush(QColor(100,255,0)))
            self.tableWidget_Status.item(index.row(),1).setText("Select")
        
        #print(self.__debug_item)

        

    def __set_tableWidget_Status_Init(self,item_list,bool_list):
        self.tableWidget_Status.setColumnCount(2)
        self.tableWidget_Status.setRowCount(len(item_list))
        self.tableWidget_Status.setHorizontalHeaderLabels(["item","status"])
        self.tableWidget_Status.horizontalHeader().resizeSection(0,115)
        self.tableWidget_Status.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_Status.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for row in range(len(item_list)):
            #print(item_list[row])
            item_value = QTableWidgetItem(item_list[row])
            self.tableWidget_Status.setItem(row,0,item_value)
            if row <= 1 :
                item_value = QTableWidgetItem(bool_list[row])
                self.tableWidget_Status.setItem(row,1,item_value)
            else:
                item_value = QTableWidgetItem("-----")
                self.tableWidget_Status.setItem(row,1,item_value)
    

if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin = MyMainWindow()  
    myWin.show()
    myWin.init_information()  
    sys.exit(app.exec_()) 