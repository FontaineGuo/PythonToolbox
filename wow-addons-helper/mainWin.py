import sys
import os
import ntpath


from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from mainUI import Ui_MainWindow
from dir_mng import dir_general, file_tools
from zip_tools import extract_addons, pack_addons


class AddonHelper(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)
        #<----------------import the style config--------------->
        # try:
        #     with open('style.qss') as f:
        #         style = f.read()
        #         self.setStyleSheet(style)
        # except:
        #     print("open stylesheet error")
        # <----------------import the style config--------------->
        # <--------------------init the btn--------------------->
        self.lb1_chose_btn_one.clicked.connect(self.chose_backup_path_btn_click)
        self.lb1_chose_btn_two.clicked.connect(self.chose_backup_confirm_btn_click)

        self.lb2_chose_btn_one.clicked.connect(self.chose_import_path_btn_click)
        self.lb2_chose_btn_two.clicked.connect(self.chose_import_confirm_btn_click)
        # <----------------------------------------------------->

        self.backup_process_bar.setValue(0)
        self.import_process_bar.setValue(0)

        self.__backup_path = ""
        self.__import_path = ""

        self.__file_number = 0




    def chose_backup_path_btn_click(self):
        dir_path =  str(QFileDialog.getExistingDirectory(self, 'Select Directory'))
        dir_path = file_tools.format_path(dir_path)
        if dir_general.check_wow_retail_path(dir_path):
            print("found the wow dir")
            self.__backup_path = dir_path
            self.__file_number = file_tools.count_files(self.__backup_path)
            self.backup_path_text.setText(dir_path)
        else:
            print("not found the wow dir")
            QMessageBox.about(self, "Title", "Couldn't found the wow _retail_ folder")
            self.__backup_path = ""

    def chose_backup_confirm_btn_click(self):
        if self.__backup_path == "":
            QMessageBox.about(self, "Title", "Please chose WOW folder")
            return
        self.backup_process_bar.setValue(0)
        process_val = 0
        for log in pack_addons.zip_dir(self.__backup_path, r'Addons.zip'):
            self.backup_detail_text.append(log)
            process_val = process_val + 1
            self.backup_process_bar.setValue((process_val/float(self.__file_number)) * 100)

    def chose_import_path_btn_click(self):
        dir_path = str(QFileDialog.getExistingDirectory(self, 'Select Directory'))
        dir_path = file_tools.format_path(dir_path)
        if dir_general.check_wow_retail_path(dir_path):
            print("found the wow dir")
            self.__import_path = dir_path
            self.import_path_text.setText(dir_path)
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
        self.import_process_bar.setValue(0)
        self.import_detail_text.append("Extracting Addons.zip")

        extract_addons.extract_package('.\\Addons', r'Addons.zip')
        self.__file_number = file_tools.count_files('.\\Addons')

        process_val = 0
        for log in dir_general.copy_dir(".\\Addons",self.__import_path):
            self.import_detail_text.append(log[0] + ' to ' + log[1])
            process_val = process_val + 1

            self.import_process_bar.setValue((process_val / float(self.__file_number)) * 100)
        dir_general.del_dir(".\\Addons")


# <-----------------------define the funcation of player data----------------------------------------------->


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AddonHelper()
    w.show()
    sys.exit(app.exec_())