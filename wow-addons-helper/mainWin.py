import sys
import mainUI
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import  QPixmap

from mainUI import Ui_MainWindow
class AddonHelper(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)

    def chose_backup_path_btn_click(self):
        # TODO: chose backup path
        pass

    def chose_backup_confirm_btn_click(self):
        # TODO: excute zip func
        pass

    def chose_import_path_btn_click(self):
        #TODO: chose import path
        pass

    def chose_import_confirm_btn_click(self):
        #TODO: excute copy_dir and flush the text area
        pass

# <-----------------------define the funcation of player data----------------------------------------------->


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AddonHelper()
    w.show()
    sys.exit(app.exec_())