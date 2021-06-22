import sys
import os
from PyQt5 import QtWidgets 
from PyQt5.QtGui import QPixmap
sys.path.append(os.path.abspath("D:\Desktop\Projects\dupl_imgs_founder\src"))

import design
import founder

path_to_img = 'D:\Desktop\Projects\dupl_imgs_founder\src\imgs'
 

class Window(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.btnDirSearch.clicked.connect(self.chose_directory) 
        self.btnStart.clicked.connect(self.find_img_dupl) 
        self.btnOpenInDir.clicked.connect(self.open_img_in_dir)

        self.dir = None 
    

    def chose_directory(self):
        self.clear_setapp()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выбрать папку")

        if directory:
            self.listWidget.addItem(directory)
            item = self.listWidget.item(0)

            if item is not None:
                self.dir = item.text()

    
    def clear_setapp(self):
        self.listWidget.clear()
        self.textLabel.clear()
        self.table.clear()
        self.table.hide()
        self.btnOpenInDir.hide()
        self.load_image(path_to_img + '\cattips.png')


    def find_img_dupl(self):
        if self.dir:
            try:
                founder.compare_images(self.dir + '/')
                if len(founder.lower_res) > 0:
                    self.textLabel.setText(f'{founder.msg}')
                    self.set_cbox(founder.lower_res)
                else: self.textLabel.setText('Я старался найти, но дубликатов тут нетб')

            except :
                self.textLabel.setText('Эта папка не содержит изображений. Выбери другую папку')
                print(sys.exc_info())  
        else:
            self.textLabel.setText('Выбeри папку')


    def set_cbox(self, list):
        table = self.table
        table.setRowCount(len(list))

        for index, el in enumerate(list):
            table.setItem(index, 0, QtWidgets.QTableWidgetItem(el))
            table.setCellWidget(index, 1, QtWidgets.QCheckBox())
         
        table.show()
        self.load_image(path_to_img + '\image.png')
        self.btnOpenInDir.show()


    def load_image(self, file_name):
        pixmap = QPixmap(file_name)
        self.displayLabel.setPixmap(pixmap)
        self.displayLabel.resize(pixmap.width(), pixmap.height())
        
    
    def open_img_in_dir(self):
        table = self.table

        for row in range(table.rowCount()):
            if QtWidgets.QCheckBox.checkState(table.cellWidget(row, 1)):
                item_text = table.item(row, 0).text().replace(" (1)", "")
                try:
                    os.system("start " + f'{self.dir}/{item_text}')
                except:
                    print(sys.exc_info())

    
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.load_image(path_to_img + '\cattips.png')
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(sys.exc_info())
        sys.exit()
