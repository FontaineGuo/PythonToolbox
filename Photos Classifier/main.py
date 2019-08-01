import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from mainUI import Ui_MainWindow
from photo_tools import file_tools as ft


class PhotoClassifier(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.Btn_input.clicked.connect(self.chose_input_path_btn_click)
        self.Btn_output.clicked.connect(self.chose_output_path_click)
        self.Btn_start.clicked.connect(self.start_btn_click)

        self.progressBar.setValue(0)

        self.TxtB_inputPath.setText("")
        self.TxtB_outputPath.setText("")

        self.__input_path = ""
        self.__output_path = ""
        self.__file_number = 0

    def chose_input_path_btn_click(self):
        dir_path = str(QFileDialog.getExistingDirectory(self, 'Select Input Directory'))
        dir_path = ft.format_path(dir_path)


        if dir_path != "":
            self.__input_path = dir_path
            self.TxtB_inputPath.setText(self.__input_path)
            self.__file_number = ft.count_files(self.__input_path)
        else:
            QMessageBox.about(self, "Title", "Please choose a input path")
            self.TxtB_inputPath.setText("")
            self.__input_path = ""


    def chose_output_path_click(self):
        dir_path = str(QFileDialog.getExistingDirectory(self, 'Select Input Directory'))
        dir_path = ft.format_path(dir_path)

        if dir_path != "":
            self.__output_path = dir_path
            self.TxtB_outputPath.setText(self.__output_path)
        else:
            QMessageBox.about(self, "Title", "Please choose a output path")
            self.TxtB_outputPath.setText("")
            self.__output_path = ""

    def start_btn_click(self):
        if self.__input_path == "":
            QMessageBox.about(self, "Title", "Please chose input folder")
            return

        if self.__output_path == "":
            QMessageBox.about(self, "Title", "Please chose output folder")
            return

        process_val = 0
        self.Btn_input.setEnabled(False)
        self.Btn_output.setEnabled(False)
        self.Btn_start.setEnabled(False)

        self.progressBar.setValue(0)

        for log in ft.move_photo_to_folder(self.__input_path, self.__output_path):
            QApplication.processEvents()
            self.TxtB_process_detial.append(log[0] + ' to ' + log[1])
            process_val += 1
            self.progressBar.setValue((process_val/float(self.__file_number)) * 100)

        self.TxtB_process_detial.append("classifier done")

        self.Btn_input.setEnabled(True)
        self.Btn_output.setEnabled(True)
        self.Btn_start.setEnabled(True)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = PhotoClassifier()
    w.show()
    sys.exit(app.exec_())