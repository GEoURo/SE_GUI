import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from gui import Ui_Dialog
from core import *
from Error import *


class SuperUIForm(QWidget):

    def __init__(self):
        super(SuperUIForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.searchmode_w.toggled.connect(self.__searchMode)
        self.ui.searchmode_c.toggled.connect(self.__searchMode)
        self.ui.headsel.toggled.connect(self.__sel_HeadChar)
        self.ui.tailsel.toggled.connect(self.__sel_TailChar)
        self.ui.lengthsel.toggled.connect(self.__sel_SoliLen)
        self.ui.headchar_in.textChanged.connect(self.__set_HeadChar)
        self.ui.tailchar_in.textChanged.connect(self.__set_TailChar)
        self.ui.length_in.textChanged.connect(self.__set_SoliLen)
        self.ui.search_Button.clicked.connect(self.__click_search)
        self.ui.address_input.textChanged.connect(self.__set_Path)
        self.ui.byHand.toggled.connect(self.__inputMode)
        self.ui.byFile.toggled.connect(self.__inputMode)
        self.ui.export_Button.clicked.connect(self.__export_result)

        self.__wsearch = False
        self.__csearch = False
        self.__set_headchar = False
        self.__set_tailchar = False
        self.__set_solilen = False
        self.__inputbyhand = False
        self.__inputbyfile = False

        self.__filepath = ''
        self.__headchar = ''
        self.__tailchar = ''
        self.__solilen = 0

    def __click_search(self):
        if not self.__wsearch and not self.__csearch:
            QMessageBox.warning(self, 'Illegal running parameter!', 'A type of search mode must be selected!')
            return
        if not self.__inputbyfile and not self.__inputbyhand:
            QMessageBox.warning(self, 'Missing input Method!', 'A type of input method must be selected!')
            return
        if self.__set_headchar and (not self.__headchar.isalpha() or len(self.__headchar) != 1):
            QMessageBox.warning(self, 'Illegal input character!', 'The assigned head of the chain must be a single alphabet!')
            return
        if self.__set_tailchar and (not self.__tailchar.isalpha() or len(self.__tailchar) != 1):
            QMessageBox.warning(self, 'Illegal input character!', 'The assigned tail of the chain must be a single alphabet!')
            return
        if self.__set_solilen and self.__solilen < 1:
            QMessageBox.warning(self, 'Illegal input number!', 'The assigned length of the chain must be above 0!')
            return

        if self.__inputbyhand:
            pass


    def __prompt_warning(self, Title="Warning", Main='', Detail=''):
        return
    

    def __set_Path(self):
        self.__filepath = self.ui.address_input.text()

    def __searchMode(self):
        self.__wsearch = self.ui.searchmode_w.isChecked()
        self.__csearch = not self.__wsearch

    def __sel_HeadChar(self):
        self.__set_headchar = self.ui.headsel.isChecked()

    def __set_HeadChar(self):
        self.__headchar = self.ui.headchar_in.text()

    def __sel_TailChar(self):
        self.__set_tailchar = self.ui.tailsel.isChecked()

    def __set_TailChar(self):
        self.__tailchar = self.ui.tailchar_in.text()

    def __sel_SoliLen(self):
        self.__set_solilen = self.ui.lengthsel.isChecked()

    def __set_SoliLen(self):
        inputtmp = self.ui.length_in.text()
        if inputtmp.isdigit():
            self.__solilen = int(inputtmp)
        else: self.__solilen = 0

    def __inputMode(self):
        self.__inputbyhand = self.ui.byHand.isChecked()
        self.__inputbyfile = not self.__inputbyhand

    def __export_result(self):
        outfilepath = './search_result.txt'
        outfile = open(outfilepath, 'w+')
        outfile.write(self.ui.outputarea.toPlainText())
        outfile.close()

    def __print_result(self):
        return
        



if __name__ == '__main__':
    gui = QApplication(sys.argv)
    gui_window = SuperUIForm()
    gui_window.show()
    sys.exit(gui.exec_())