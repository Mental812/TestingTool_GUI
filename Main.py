import sys 	
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from utils.UI_Class import Ui_MainWindow
from utils.Information_Class import Information_Class

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.Info_class = Information_Class()
        
    def init_information(self):
        BSP,JetPack,Camera,Support = self.Info_class.get_Information()

        self.lineEdit_BSP.setText(BSP)
        self.lineEdit_JetPack.setText(JetPack)
        self.lineEdit_Camera.setText(Camera)

        if Support == "Yes":
            self.lineEdit_Support.setStyleSheet("background: green;")
            TestingItem_Name = self.Info_class.get_TestingItem_list() #get Testing item list 
            self.__set_TableView(TestingItem_Name)
        elif Support == "No":
            self.lineEdit_Support.setStyleSheet("background: red;")
        self.lineEdit_Support.setText(Support)

    def __set_TableView(self,TestingItem_Name):
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers) #close edit in UI
        model =  QStandardItemModel(len(TestingItem_Name), 2)
        model.setHorizontalHeaderLabels(['Item', 'Status'])
        for row in range(len(TestingItem_Name)):
            #print(TestingItem_Name[row])
            item = QStandardItem(str(TestingItem_Name[row]))
            model.setItem(row, 0, item)
            #model.setItem(row, 1, "Wait...")
        self.tableView.setModel(model)

    
if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin = MyMainWindow()  
    myWin.show()
    myWin.init_information()  
    sys.exit(app.exec_()) 