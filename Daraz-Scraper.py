# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Daraz-Scraper.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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

        self.retranslateUi(DarazScraper)
        QtCore.QMetaObject.connectSlotsByName(DarazScraper)

    def retranslateUi(self, DarazScraper):
        _translate = QtCore.QCoreApplication.translate
        DarazScraper.setWindowTitle(_translate("DarazScraper", "Daraz Scraper"))
        self.label.setText(_translate("DarazScraper", "Search Keyword"))
        self.pushButton.setText(_translate("DarazScraper", "Collect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DarazScraper = QtWidgets.QWidget()
    ui = Ui_DarazScraper()
    ui.setupUi(DarazScraper)
    DarazScraper.show()
    sys.exit(app.exec_())

