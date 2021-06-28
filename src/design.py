from PyQt5 import QtCore, QtGui, QtWidgets
import os

ico_png = 'src\imgs\ico.png'
ico = os.path.abspath(ico_png)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(904, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setObjectName("centralwidget")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 28, 410, 31))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet('background-color: rgb(253, 254, 253)')

        self.btnDirSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnDirSearch.setGeometry(QtCore.QRect(270, 80, 170, 41))
        self.btnDirSearch.setObjectName("btnDirSearch")
        self.btnDirSearch.setStyleSheet('background-color: rgb(49, 55, 66); color: rgb(253, 254, 253)')

        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(30, 80, 170, 41))
        self.btnStart.setObjectName("btnStart")
        self.btnStart.setStyleSheet('background-color: rgb(49, 55, 66); color: rgb(253, 254, 253)')

        self.textLabel = QtWidgets.QLabel(self.centralwidget)
        self.textLabel.setGeometry(QtCore.QRect(460, 10, 541, 101))
        self.textLabel.setText("")
        self.textLabel.setStyleSheet('font: bold italic;')
        self.textLabel.setStyleSheet('margin-top: 0')
        self.textLabel.setObjectName("label")

        self.displayLabel = QtWidgets.QLabel(self.centralwidget)
        self.displayLabel.setGeometry(QtCore.QRect(26, 140, 871, 531))
        self.displayLabel.setText("")
        self.displayLabel.setObjectName("displayLabel")

        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(470, 130, 380, 481))
        self.table.setObjectName("table")
        self.table.setStyleSheet('background-color: rgb(250, 250, 250); color: rgb(13, 10, 10);')
        self.table.setColumnCount(2)
        self.table.setColumnWidth(0, 302)
        self.table.setColumnWidth(1, 60)
        self.table.setContentsMargins(0, 0, 5, 0)
        self.table.setHorizontalHeaderLabels(['У этих изображений наихудшее качество', ''])
        self.table.hide()

        self.btnOpenInDir = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenInDir.setGeometry(QtCore.QRect(470, 620, 200, 41))
        self.btnOpenInDir.setObjectName("btnOpenInDir")
        self.btnOpenInDir.setStyleSheet('background-color: rgb(49, 55, 66); color: rgb(253, 254, 253)')
        self.btnOpenInDir.hide()

        self.btnStart.raise_()
        self.listWidget.raise_()
        self.btnDirSearch.raise_()
        self.textLabel.raise_()
        self.displayLabel.raise_()
        self.table.raise_()
        self.btnOpenInDir.raise_()
        
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setStyleSheet('background-color: rgb(255,255,255)')
       
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Кот на поиске дубликатов картиночек"))
        MainWindow.setWindowIcon(QtGui.QIcon(ico))
        self.btnDirSearch.setText(_translate("MainWindow", "Выбрать папку"))
        self.btnStart.setText(_translate("MainWindow", "Начать сканирование"))
        self.btnOpenInDir.setText(_translate("MainWindow", "Открыть выбранные изображения"))
