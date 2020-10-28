import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow
from utils.UI_Class import Ui_MainWindow
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        
    def change_Text(self):
        self.lineEdit_BSP.setText("go...")
        self.lineEdit_JetPack.setText("s...")
        self.lineEdit_Camera.setText( "sada...")
        
if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin = MyMainWindow()  
    myWin.show()
    myWin.change_Text()  
    sys.exit(app.exec_())  