import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog


from mainUI import Ui_MainWindow

from dir_mng import dir_general
from zip_tools import extract_addons, pack_addons


class AddonHelper(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)
        # <--------------------init the btn--------------------->
        self.lb1_chose_btn_one.clicked.connect(self.chose_backup_path_btn_click)
        self.lb1_chose_btn_two.clicked.connect(self.chose_backup_confirm_btn_click)

        self.lb2_chose_btn_one.clicked.connect(self.chose_import_path_btn_click)
        self.lb2_chose_btn_two.clicked.connect(self.chose_backup_confirm_btn_click)
        # <----------------------------------------------------->

        self.__backup_path = ""
        self.__import_path = ""

    def chose_backup_path_btn_click(self):
        dir_path =  str(QFileDialog.getExistingDirectory(self, 'Select Directory'))
        # print(dir_path)
        if dir_general.check_wow_retail_path(dir_path):
            print("found the wow dir")
            self.__backup_path = dir_path
        else:
            print("not found the wow dir")
            QMessageBox.about(self, "Title", "Couldn't found the wow _retail_ folder")
            self.__bakcup_path = ""

    def chose_backup_confirm_btn_click(self):
        if self.__bakcup_path == "":
            QMessageBox.about(self, "Title", "Please chose WOW folder")
            return
        pack_addons.zip_dir(self.__bakcup_path, r'Addons.zip')

    def chose_import_path_btn_click(self):
        dir_path = str(QFileDialog.getExistingDirectory(self, 'Select Directory'))
        # print(dir_path)
        if dir_general.check_wow_retail_path(dir_path):
            print("found the wow dir")
            self.__import_path = dir_path
        else:
            print("not found the wow dir")
            QMessageBox.about(self, "Title", "Couldn't found the wow _retail_ folder")
            self.__import_path = ""

    def chose_import_confirm_btn_click(self):
        if self.__import_path == "":
            QMessageBox.about(self, "Title", "Please chose WOW folder")
            return
        if not os.path.exists(r'Addons.zip'):
            QMessageBox.about(self, "Title", "Couldn't found backup zip file 'Addons.zip'")
            return
        extract_addons.extract_package('.\\Addons', r'Addons.zip')
        dir_general.copy_dir(".\\Addons",self.__import_path)


# <-----------------------define the funcation of player data----------------------------------------------->


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AddonHelper()
    w.show()
    sys.exit(app.exec_())