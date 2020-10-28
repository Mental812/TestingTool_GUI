import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow
from utils.UI_Class import Ui_MainWindow
from utils.Information_Class import Information_Class
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.Info_class = Information_Class()
        
    def change_Text(self):
        BSP,JetPack,Camera = self.Info_class.get_Information()
        self.lineEdit_BSP.setText(BSP)
        self.lineEdit_JetPack.setText(JetPack)
        self.lineEdit_Camera.setText(Camera)
        
if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin = MyMainWindow()  
    myWin.show()
    myWin.change_Text()  
    sys.exit(app.exec_())  