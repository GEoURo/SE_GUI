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

        self.__rawlist = []
        self.__core = Core()

    def __click_search(self):
        if not self.__wsearch and not self.__csearch:
            self.__prompt_warning(_Main='Illegal running parameter!',
            _Detail='A type of search mode must be selected!')
            return
        if not self.__inputbyfile and not self.__inputbyhand:
            self.__prompt_warning(_Main='Missing input Method!',
            _Detail='A type of input method must be selected!')
            return
        if self.__set_headchar and (not self.__headchar.isalpha() or len(self.__headchar) != 1):
            self.__prompt_warning(_Main='Illegal head character!',
            _Detail='The assigned head of the chain must be a single alphabet!')
            return
        if self.__set_tailchar and (not self.__tailchar.isalpha() or len(self.__tailchar) != 1):
            self.__prompt_warning(_Main='Illegal tail character!',
            _Detail='The assigned tail of the chain must be a single alphabet!')
            return
        if self.__set_solilen and self.__solilen < 1:
            self.__prompt_warning(_Main='IIlegal input number!',
            _Detail='The assigned length of the chain must be above 1!')
            return

        if self.__inputbyfile:
            self.__set_Path()
            go_on, self.__rawlist = self.__read_file(self.__filepath)
            if not go_on:
                return

        elif self.__inputbyhand:
            pass

    def __read_file(self, _filename):
        if _filename[0] != '/' and _filename[0:2] != './':
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Non absolute address detected!")
            msg.setInformativeText("Click \"Ok\" to continue the search on current directory or \"Cancel\" to re-enter the address.")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Ok)
            go_on = msg.exec()
            if go_on == QMessageBox.Cancel:
                return False, []
            else:
                _filename = "./" + _filename
        
        try:
            in_file = open(_filename, 'r')
            is_reading = False
            tmpword = ''
            wordlist = []
            while True:
                tmpchar = in_file.read(1)
                if tmpchar == '':
                    break
                elif tmpchar.isalpha():
                    is_reading = True
                    tmpword += tmpchar.lower()
                elif is_reading:
                    is_reading = False
                    if not tmpword in wordlist:
                        wordlist.append(tmpword)
                    tmpword = ''
                
            in_file.close()
            return True, wordlist
        
        except IOError:
            self.__prompt_warning(_Main="File operation error!",
            _Detail="Cannot open file! Please check the address.")
            return False, []
        
    def __prompt_warning(self, _Title="Warning", _Main='', _Detail=''):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle(_Title)
        msg.setText(_Main)
        msg.setInformativeText(_Detail)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        return msg.exec()
    
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
        outfilepath = self.ui.result_output.text()
        try:
            outfile = open(outfilepath, 'w+')
            outfile.write(self.ui.outputarea.toPlainText())
        except IOError:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Export Error!")
            msg.setInformativeText("Cannot write to this file!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            return msg.exec()
        finally:            
            outfile.close()

    def __print_result(self):
        return
        



if __name__ == '__main__':
    gui = QApplication(sys.argv)
    gui_window = SuperUIForm()
    gui_window.show()
    sys.exit(gui.exec_())