from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class MyTableModel(QAbstractTableModel):
    def __init__(self, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.items = [i for i in range(90)]

    def rowCount(self, parent):
        return len(self.items)       
    def columnCount(self, parent):
        return 1

    def data(self, index, role):
        if not index.isValid():
            return QVariant()

        row=index.row()
        column=index.column()

        if role == Qt.DisplayRole:
            if row<len(self.items):
                return QVariant(self.items[row])
            else:
                return QVariant()

        # if role==Qt.BackgroundColorRole:
        #     if row%2: bgColor=QColor(Qt.green)
        #     else: bgColor=QColor(Qt.blue)        
        #     return QVariant(QColor(bgColor))


class Proxy01(QSortFilterProxyModel):
    def __init__(self):
        super(Proxy01, self).__init__()

    def filterAcceptsRow(self, row, parent):
        if row%3: return True
        else: return False

class MyWindow(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)

        self.tablemodel=MyTableModel(self)               

        self.proxy1=Proxy01()
        self.proxy1.setSourceModel(self.tablemodel)

        tableviewA=QTableView(self) 
        tableviewA.setModel(self.proxy1)
        tableviewA.setSortingEnabled(True) 
        tableviewA.horizontalHeader().setSortIndicator(0, Qt.AscendingOrder)
        tableviewA.horizontalHeader().setStretchLastSection(True)
        tableviewA.setAlternatingRowColors(True)
        tableviewA.setStyleSheet("alternate-background-color: yellow; background-color: red;");

        layout = QVBoxLayout(self)
        layout.addWidget(tableviewA)

        self.setLayout(layout)

    def test(self, arg):
        print (arg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_()) 