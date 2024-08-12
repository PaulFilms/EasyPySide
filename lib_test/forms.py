'''
Toolkit with simplified functions and methods for development with PySide6

TASK:
    - Create unit test module 

WARNINGS:
    - ...

________________________________________________________________________________________________ '''
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'
__update__ = '2024.08.12'

''' SYSTEM LIBRARIES '''
from enum import Enum, auto

''' EXTERNAL LIBRARIES '''
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QMessageBox, QInputDialog, QDialog



''' INFOBOXES
________________________________________________________________________________________________ '''

def INFOBOX(info: str, winTitle: str = "INFO", icon: QIcon = None) -> None:
    '''
    Information Window
    '''
    infobox = QMessageBox()
    infobox.setIcon(QMessageBox.Icon.Information)
    infobox.setFont(QFont('Consolas', 10))
    infobox.setWindowTitle(winTitle)
    infobox.setText(info)
    if icon:
        infobox.setWindowIcon(icon)
    infobox.exec()

def YESNOBOX(info: str, winTitle: str = "QUESTION", icon: QIcon = None) -> bool:
    '''
    Question Window with YES/NO Options
    '''
    yesnobox = QMessageBox()
    yesnobox.setFont(QFont('Consolas', 10))
    yesnobox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    yesnobox.setIcon(QMessageBox.Icon.Question)
    yesnobox.setWindowTitle(winTitle)
    yesnobox.setText(info)
    if icon:
        yesnobox.setWindowIcon(icon)
    reply = yesnobox.exec()
    if reply == yesnobox.StandardButton.Yes:
        return True
    if reply == yesnobox.StandardButton.No:
        return False

def INPUTBOX(info: str = None, winTitle: str = "INPUT", icon: QIcon = None) -> str:
    '''
    Input Window for Entering a Value
    '''
    inputbox = QInputDialog()
    inputbox.setWindowTitle(winTitle)
    if info:
        inputbox.setLabelText(info)
    if icon:
        inputbox.setWindowIcon(icon)
    reply = inputbox.exec()
    if reply:
        return inputbox.textValue()
    else:
        return None


''' Qt CUSTOM FORMS
________________________________________________________________________________________________ '''

class MYFONTS(Enum):
    '''
    '''
    FONT_LABEL = QFont("Roboto Black", pointSize=6, weight=8)
    FONT_WIDGET = QFont("Consolas", pointSize=12)
    FONT_TABLE = QFont("Consolas", pointSize=10)

from .forms_ui import PYSIDE_QLIST

class QLIST(QDialog):
    '''
    QList Widget Dialog
    
    Get an avalilable <str> data from the list

    `Returns:` str
    '''
    def __init__(self, LIST: list | tuple, Window_Title: str="List", icon: QIcon = None):
        QDialog.__init__(self)

        ''' INIT '''
        self.ui = PYSIDE_QLIST.Ui_Dialog()
        self.ui.setupUi(self)

        ''' WIDGETS '''
        if icon: self.setWindowIcon(icon)
        self.setWindowTitle(Window_Title)
        for item in LIST:
            self.ui.lst.addItem(item)
        self.data: str = None

        ''' CONNECTIONS '''
        self.ui.lst.doubleClicked.connect(self.DATA_SELECT)
    
    def DATA_SELECT(self) -> None:
        self.data = self.ui.lst.currentItem().text()
        self.close()

...