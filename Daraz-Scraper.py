from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
import runpy
from selenium import webdriver
# from openpyxl import workbook, load_workbook
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import sys


class Ui_DarazScraper(object):
    def setupUi(self, DarazScraper):

        DarazScraper.setObjectName("DarazScraper")
        DarazScraper.resize(500, 200)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        DarazScraper.setFont(font)
        self.label = QtWidgets.QLabel(DarazScraper)
        self.label.setGeometry(QtCore.QRect(30, 70, 121, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(DarazScraper)
        self.lineEdit.setGeometry(QtCore.QRect(170, 60, 291, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(DarazScraper)
        self.pushButton.setGeometry(QtCore.QRect(154, 122, 191, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(lambda: self.clicked())


        self.retranslateUi(DarazScraper)
        QtCore.QMetaObject.connectSlotsByName(DarazScraper)

    def retranslateUi(self, DarazScraper):
        _translate = QtCore.QCoreApplication.translate
        DarazScraper.setWindowTitle(_translate("DarazScraper", "Daraz Scraper"))
        self.label.setText(_translate("DarazScraper", "Search Keyword"))
        self.pushButton.setText(_translate("DarazScraper", "Collect"))

    def clicked(self):
        keyword = self.lineEdit.text()
        outfile = open('keyword.txt', 'w')

        outfile.write(keyword)
        outfile.close()
        self.execution = ExecutionThread()
        self.execution.start()

        # runpy.run_path(path_name='scraper.py')


class ExecutionThread(QThread):
    def run(self):
        runpy.run_path(path_name='scraper.py')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    DarazScraper = QtWidgets.QWidget()
    ui = Ui_DarazScraper()
    ui.setupUi(DarazScraper)
    DarazScraper.show()
    sys.exit(app.exec_())

