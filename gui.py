# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(520, 412)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.outputarea = QtWidgets.QTextBrowser(Dialog)
        self.outputarea.setMinimumSize(QtCore.QSize(235, 200))
        self.outputarea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.outputarea.setObjectName("outputarea")
        self.gridLayout.addWidget(self.outputarea, 10, 3, 1, 2)
        self.address_input = QtWidgets.QLineEdit(Dialog)
        self.address_input.setEnabled(False)
        self.address_input.setObjectName("address_input")
        self.gridLayout.addWidget(self.address_input, 6, 3, 1, 2)
        self.length_in = QtWidgets.QLineEdit(Dialog)
        self.length_in.setEnabled(False)
        self.length_in.setMinimumSize(QtCore.QSize(60, 0))
        self.length_in.setClearButtonEnabled(False)
        self.length_in.setObjectName("length_in")
        self.gridLayout.addWidget(self.length_in, 4, 4, 1, 1)
        self.export_Button = QtWidgets.QPushButton(Dialog)
        self.export_Button.setObjectName("export_Button")
        self.gridLayout.addWidget(self.export_Button, 8, 0, 1, 1)
        self.tailsel = QtWidgets.QCheckBox(Dialog)
        self.tailsel.setObjectName("tailsel")
        self.gridLayout.addWidget(self.tailsel, 3, 3, 1, 1)
        self.headsel = QtWidgets.QCheckBox(Dialog)
        self.headsel.setObjectName("headsel")
        self.gridLayout.addWidget(self.headsel, 3, 0, 1, 1)
        self.searchmode_c = QtWidgets.QRadioButton(Dialog)
        self.searchmode_c.setObjectName("searchmode_c")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.searchmode_c)
        self.gridLayout.addWidget(self.searchmode_c, 1, 3, 1, 1)
        self.tailchar_in = QtWidgets.QLineEdit(Dialog)
        self.tailchar_in.setEnabled(False)
        self.tailchar_in.setAcceptDrops(True)
        self.tailchar_in.setObjectName("tailchar_in")
        self.gridLayout.addWidget(self.tailchar_in, 4, 3, 1, 1)
        self.inputarea = QtWidgets.QPlainTextEdit(Dialog)
        self.inputarea.setEnabled(False)
        self.inputarea.setMinimumSize(QtCore.QSize(235, 200))
        self.inputarea.setObjectName("inputarea")
        self.gridLayout.addWidget(self.inputarea, 10, 0, 1, 3)
        self.headchar_in = QtWidgets.QLineEdit(Dialog)
        self.headchar_in.setEnabled(False)
        self.headchar_in.setText("")
        self.headchar_in.setObjectName("headchar_in")
        self.gridLayout.addWidget(self.headchar_in, 4, 0, 1, 1)
        self.result_output = QtWidgets.QLineEdit(Dialog)
        self.result_output.setObjectName("result_output")
        self.gridLayout.addWidget(self.result_output, 8, 3, 1, 2)
        self.searchmode_w = QtWidgets.QRadioButton(Dialog)
        self.searchmode_w.setObjectName("searchmode_w")
        self.buttonGroup.addButton(self.searchmode_w)
        self.gridLayout.addWidget(self.searchmode_w, 1, 0, 1, 1)
        self.byFile = QtWidgets.QRadioButton(Dialog)
        self.byFile.setObjectName("byFile")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.byFile)
        self.gridLayout.addWidget(self.byFile, 6, 0, 1, 1)
        self.lengthsel = QtWidgets.QCheckBox(Dialog)
        self.lengthsel.setObjectName("lengthsel")
        self.gridLayout.addWidget(self.lengthsel, 3, 4, 1, 1)
        self.byHand = QtWidgets.QRadioButton(Dialog)
        self.byHand.setObjectName("byHand")
        self.buttonGroup_2.addButton(self.byHand)
        self.gridLayout.addWidget(self.byHand, 5, 0, 1, 1)
        self.search_Button = QtWidgets.QPushButton(Dialog)
        self.search_Button.setObjectName("search_Button")
        self.gridLayout.addWidget(self.search_Button, 5, 3, 1, 2)

        self.retranslateUi(Dialog)
        self.headsel.toggled['bool'].connect(self.headchar_in.setEnabled)
        self.tailsel.toggled['bool'].connect(self.tailchar_in.setEnabled)
        self.lengthsel.toggled['bool'].connect(self.length_in.setEnabled)
        self.byFile.toggled['bool'].connect(self.address_input.setEnabled)
        self.byHand.toggled['bool'].connect(self.inputarea.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Word Chain"))
        self.address_input.setText(_translate("Dialog", "File address"))
        self.export_Button.setText(_translate("Dialog", "Export"))
        self.tailsel.setText(_translate("Dialog", "Tail character"))
        self.headsel.setText(_translate("Dialog", "Head character"))
        self.searchmode_c.setText(_translate("Dialog", "Longest character length"))
        self.inputarea.setPlainText(_translate("Dialog", "Input words here"))
        self.searchmode_w.setText(_translate("Dialog", "Longest word length"))
        self.byFile.setText(_translate("Dialog", "File input"))
        self.lengthsel.setText(_translate("Dialog", "Length"))
        self.byHand.setText(_translate("Dialog", "Manual Input"))
        self.search_Button.setText(_translate("Dialog", "Search"))


