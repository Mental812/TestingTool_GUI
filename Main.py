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
        #self.Conf_class.write_items_value("times",str(0))
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
            
            self.__set_TableView(TestingItem_Name,Testing_Bool)
            self.__auto_item = TestingItem_Name
            print(Testing_Bool)
            #print()
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

    def __click_action_Exit(self):
        sys.exit(0) 

    def __click_action_Debug(self): #debug模式控制
        if self.actionDebug.isChecked() :  #"如果debug被觸發"
            self.lineEdit_message.setStyleSheet("background: green;") 
            self.lineEdit_message.setText("-----Debug Mode (Please doubleclick item)-----")
            self.textEdit_gondan.setEnabled(False)
            self.lineEdit_board.setEnabled(False)
            
            self.tableView.doubleClicked.connect(self.__click_tableview_deubg)
            self.pushButton_start.setEnabled(True)
        else :
            self.lineEdit_message.setStyleSheet("background: white;") 
            self.lineEdit_message.setText("-----請掃描工單及品號條碼-----")
            self.tableView.disconnect()
            self.pushButton_start.setEnabled(False)
            self.textEdit_gondan.setEnabled(True)
            self.lineEdit_board.setEnabled(True)
        
    def __click_tableview_deubg(self):
        # #selected cell value.
        repeat = False
        index=(self.tableView.selectionModel().currentIndex())
        # print(index)
        value=index.sibling(index.row(),index.column()).data()
        print(value)
        for item in self.__debug_item:
            if value == item:
                #print("repeat")
                repeat = True
                break
            else:
                repeat = False
        if repeat is False: 
            self.__debug_item.append(value)
        #print(self.__debug_item)
        #index.
        #index.row() # gives current selected row.
        #index.column() # gives current selected column.
        #index.sibling(index.row(),index.column()).data() # will return cell data
    
    def __set_TableView(self,TestingItem_Name,TestingItem_bool):
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers) #close edit in UI
        model =  QStandardItemModel(len(TestingItem_Name), 2)
        model.setHorizontalHeaderLabels(['Item', 'Status'])
        for row in range(len(TestingItem_Name)):
            #print(TestingItem_Name[row])
            item = QStandardItem(str(TestingItem_Name[row]))
            model.setItem(row, 0, item)
        module = QStandardItem(str(TestingItem_bool[0]))
        board = QStandardItem(str(TestingItem_bool[1]))
        model.setItem(0, 1,module ) #set module
        model.setItem(1, 1,board ) #set board
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setModel(model)
    

if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin = MyMainWindow()  
    myWin.show()
    myWin.init_information()  
    sys.exit(app.exec_()) 