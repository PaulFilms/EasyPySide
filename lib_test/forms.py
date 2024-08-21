'''
PySide6 Custom Forms Toolkit for development 
'''
__update__ = '2024.08.21'

from typing import Tuple, List, Dict, Union
from dataclasses import dataclass

from PySide6.QtGui import QIcon, QFont, QCloseEvent
from PySide6.QtWidgets import QDialog, QMessageBox, QInputDialog, QHeaderView
import markdown2

import lib_test.resources ## Resources
from lib_test.widgets import CELL_WR, CELL_RD, CELL_CHECKBOX, CELL_SPINBOX, CELL_COMBOBOX, CELL_READONLY



''' INFOBOXES
________________________________________________________________________________________________ '''

ICO_INFO = QIcon(":/__forms/info.ico")

def INFOBOX(info: str, winTitle: str = "INFO", icon: QIcon = ICO_INFO) -> None:
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

def YESNOBOX(info: str, winTitle: str = "QUESTION", icon: QIcon = ICO_INFO) -> bool:
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

def INPUTBOX(info: str = None, winTitle: str = "INPUT", icon: QIcon = ICO_INFO) -> str:
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

from .__forms import PYSIDE_QLIST
from .__forms import PYSIDE_QLIST_FORM
from .__forms import PYSIDE_QTABLE_FORM
from .__forms import PYSIDE_QMARKDOWN
from .__forms import PYSIDE_QACQUISITIONS

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

class QLIST_FORM(QDialog):
    '''
    List Selection Form

    Get a List of <str> Values

    `Returns:` List[str]
    '''
    def __init__(self, LIST: Union[list, tuple] = None, Window_Title: str = "LIST EDIT", icon: QIcon = None, parent=None):
        QDialog.__init__(self, parent)
        
        ''' INIT '''
        self.ui = PYSIDE_QLIST_FORM.Ui_Dialog()
        self.ui.setupUi(self)
        self.data: List[str] = None

        ''' WIDGETS '''
        if icon:
            self.icon: QIcon = icon
            self.setWindowIcon(self.icon)
        self.setWindowTitle(Window_Title)
        if LIST:
            self.ui.lst_items.addItems([item for item in LIST])
        self.GET_ITEMS()
        
        ''' CONNECTIONS '''
        self.ui.btn_add.clicked.connect(self.ITEM_ADD)
        self.ui.btn_del.clicked.connect(self.ITEM_DEL)
        self.ui.btn_up.clicked.connect(self.ITEM_UP)
        self.ui.btn_down.clicked.connect(self.ITEM_DOWN)
        
    def ITEM_ADD(self) -> None:
        ITEM: str = self.ui.tx_newitem.text()
        if ITEM and ITEM != "":
            self.ui.lst_items.addItem(ITEM)
            self.ui.tx_newitem.clear()
            self.GET_ITEMS()
    
    def ITEM_DEL(self) -> None:
        if self.ui.lst_items.currentRow() < 0:
            return
        if not YESNOBOX("ATTENTION", "DO YOU WANT TO DELETE THIS FIELD ?", icon=self.icon):
            return
        self.ui.lst_items.takeItem(self.ui.lst_items.currentIndex().row())
        self.GET_ITEMS()
    
    def ITEM_UP(self) -> None:
        currentRow: int = self.ui.lst_items.currentRow()
        currentItem = self.ui.lst_items.takeItem(currentRow)
        self.ui.lst_items.insertItem(currentRow - 1, currentItem)
        self.ui.lst_items.setCurrentRow(currentRow-1)
        self.GET_ITEMS()
        
    def ITEM_DOWN(self) -> None:
        currentRow = self.ui.lst_items.currentRow()
        currentItem = self.ui.lst_items.takeItem(currentRow)
        self.ui.lst_items.insertItem(currentRow + 1, currentItem)
        self.ui.lst_items.setCurrentRow(currentRow+1)
        self.GET_ITEMS()
    
    def GET_ITEMS(self) -> None:
        self.data = [self.ui.lst_items.item(x).text() for x in range(self.ui.lst_items.count())]

class QTABLE_FORM(QDialog):
    '''
    QTable Form (1 Field: 1 Value)

    Get a dictionary with the data of selected fields in CONFIG

    `CONFIG:` List[ configValue]

    `Returns:` Dict[str, Union[str, int, float, bool]]
    '''
    @dataclass
    class configValue():
        '''
        Value object for use in data configuration
        '''
        fieldName: str
        value: Union[bool, str, int, float]
        mandatory: bool = False
        info: str = str()

    def __init__(self, CONFIG: Union[List[configValue], Tuple[configValue]], comboBoxEditables: bool=False, Window_Title: str="TABLE FORM", icon: QIcon = None) -> None:
        QDialog.__init__(self)
        self.__CONFIG = CONFIG
        self.comboBoxEditable = comboBoxEditables
        self.icon = icon
        self.data: Dict[str, Union[bool, str, int, float]] = None

        ## GUI
        self.ui = PYSIDE_QTABLE_FORM.Ui_Dialog()
        self.ui.setupUi(self)
        
        ## WIDGETS
        self.setWindowTitle(Window_Title)
        if self.icon: self.setWindowIcon(self.icon)
        self.ui.tbl_form.verticalHeader().setVisible(True)
        self.ui.tbl_form.setColumnCount(3)
        H_HEADERS: tuple = ("DATA", "", "INFO")
        self.ui.tbl_form.setHorizontalHeaderLabels(H_HEADERS)

        ## 
        self.CONNECTIONS()
        self.SETUP_DATA()

    def CONNECTIONS(self):
        self.ui.btn_intro.clicked.connect(self.DATA_INTRO)

    def SETUP_DATA(self):
        TABLE = self.ui.tbl_form
        ## SET CONFIG
        TABLE.setRowCount(len(self.__CONFIG))
        row = 0
        self.HEADERS = []
        for field in self.__CONFIG:
            row = self.__CONFIG.index(field)
            ## NAME
            self.HEADERS.append(field.fieldName)
            ## VALUE
            match field.value:
                case field.value if isinstance(field.value, bool):
                    CELL_CHECKBOX(TABLE, row, 0, field.value)
                case field.value if isinstance(field.value, str):
                    CELL_WR(TABLE, row, 0, field.value)
                case field.value if isinstance(field.value, int):
                    CELL_SPINBOX(TABLE, row, 0, field.value)
                case field.value if isinstance(field.value, float):
                    # BUG **Hay que ousar un doublespinbox ajustando la resolucion al valor indicado 
                    CELL_WR(TABLE, row, 0, field.value)
                case field.value if isinstance(field.value, list) or isinstance(field.value, tuple):
                    CELL_COMBOBOX(TABLE, row, 0, field.value, self.comboBoxEditable)
            # TYPE = type(field.value)
            # if type(field.value) == bool: 
            #     CELL_CHECKBOX(TABLE, row, 0, field.value)
            # if TYPE == str: CELL_WR(TABLE, row, 0, field.value)
            # if TYPE == list: CELL_COMBOBOX(TABLE, row, 0, field.value, self.comboBoxEditable)
            # if TYPE == tuple: CELL_COMBOBOX(TABLE, row, 0, field.value, self.comboBoxEditable)
            # if TYPE == int: CELL_SPINBOX(TABLE, row, 0, field.value)
            # if TYPE == float: CELL_WR(TABLE, row, 0, field.value)
            ## MANDATORY
            if field.mandatory: CELL_WR(TABLE, row, 1, "*")
            CELL_READONLY(TABLE, row, 1)
            ## INFO
            CELL_WR(TABLE, row, 2, field.info)
            CELL_READONLY(TABLE, row, 2)
        ## SET TABLE
        TABLE.setVerticalHeaderLabels(self.HEADERS)
        TABLE.resizeColumnsToContents()
        TABLE.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
        TABLE.setColumnWidth(0, 230)

    def DATA_INTRO(self):
        TABLE = self.ui.tbl_form
        self.data = {}
        summary = ""
        for field in self.HEADERS:
            row = self.HEADERS.index(field)
            value = CELL_RD(TABLE, row, 0)
            summary += f"{field}: "
            if value == "" or value == None:
                if CELL_RD(TABLE, row, 1) == "*": 
                    self.data = None
                    INFOBOX("PLEASE, FILL ALL THE MANDATORY (*) FIELDS", "ATTENTION", icon=self.icon)
                    return
                self.data[field] = None
            else:
                self.data[field] = value
                summary += f"{value}"
            summary += "\n"
        if YESNOBOX(f"DO YOU WANT SAVE THIS DATA?\n\n{summary}", "ATTENTION", icon=self.icon) == True:
            self.close()
        else:
            self.data = None
            return

class QMARKDOWN(QDialog):
    '''
    Markdown format Text Form
    '''
    def __init__(self, MD_TEXT: str = str(), Window_Title: str="MarkDown Text", icon: QIcon = None) -> None:
        QDialog.__init__(self)
        
        ''' INIT '''
        self.ui = PYSIDE_QMARKDOWN.Ui_Dialog()
        self.ui.setupUi(self)

        ''' WIDGETS '''
        if icon: self.setWindowIcon(icon)
        self.setWindowTitle(Window_Title)
        self.ui.tx_preview.setReadOnly(True)
        html_text = markdown2.markdown(MD_TEXT)
        self.ui.tx_preview.setHtml(html_text)

class QACQUISITIONS(QDialog):
    '''
    QAcquisitions Form

    `Args:`
        - VALUES: Dict[str, List] -> example: {"MEASURE": [], "INDICATION": []}
        - info: str -> Text info about parameters of acquisitions

    `Warnings:`
        - LEFT/RIGHT functions are Not Enabled by default, its necessary to config in the MainWindow
    '''    
    def __init__(self, VALUES: Dict[str, List] = None, info: str = str(), Window_Title: str="List", icon: QIcon = None):
        QDialog.__init__(self)
        self.data: Dict[str, List] = None

        ''' INIT '''
        self.ui = PYSIDE_QACQUISITIONS.Ui_Dialog()
        self.ui.setupUi(self)

        ''' WIDGETS '''
        if icon: self.setWindowIcon(icon)
        self.setWindowTitle(Window_Title)
        self.ui.cb_units.clear()
        self.ui.cb_units.addItems(["G","M","k","","m","µ","n"])
        self.ui.cb_units.setCurrentIndex(3)

        ## DATA
        self.SET_VALUES(info=info, values=VALUES)
        self.GET_VALUES()

        ''' CONNECTIONS '''
        self.ui.btn_addvalue.clicked.connect(self.VALUE_ADD)
        self.ui.btn_delete.clicked.connect(self.VALUE_DEL)
        self.ui.btn_exit.clicked.connect(self.close)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.GET_VALUES()

    def VALUE_ADD(self) -> None:
        '''
        '''
        value: float = float()
        try:
            value = float(self.ui.tx_value.text())
        except:
            value = 0
        unit: str = self.ui.cb_units.currentText()
        match unit:
            case "G":
                value = value * 1e9
            case "M":
                value = value * 1e6
            case "k":
                value = value * 1e3
            case "":
                value = value * 1
            case "m":
                value = value * 1e-3
            case "µ":
                value = value * 1e-6
            case "n":
                value = value * 1e-9
        row = self.ui.tbl_values.rowCount()
        self.ui.tbl_values.insertRow(row)
        CELL_WR(self.ui.tbl_values, row, 0, self.ui.cb_type.currentText())
        CELL_WR(self.ui.tbl_values, row, 1, value)
        self.GET_VALUES()

    def VALUE_DEL(self) -> None:
        '''
        '''
        row = self.ui.tbl_values.currentRow()
        if row < 0:
            return
        self.ui.tbl_values.removeRow(row)
        self.GET_VALUES()
    
    def EXIT(self) -> None:
        '''
        '''
        self.GET_VALUES()
        self.close()
    
    def SET_VALUES(self, info: str = str(), values: Dict[str, List] = None) -> None:
        self.ui.tx_info.setText(info)
        ## TABLE
        self.data = None
        self.ui.tx_value.clear()
        self.ui.cb_type.clear()
        self.ui.tbl_values.setRowCount(0)
        if values:
            self.ui.cb_type.addItems(list(values.keys()))
            for _type, _values in values.items():
                for value in _values:
                    row = self.ui.tbl_values.rowCount()
                    self.ui.tbl_values.insertRow(row)
                    CELL_WR(self.ui.tbl_values, row, 0, _type)
                    CELL_WR(self.ui.tbl_values, row, 1, value)
        else:
            self.ui.cb_type.addItem("-")
        self.ui.tx_value.setFocus()
        self.GET_VALUES()

    def GET_VALUES(self) -> None:
        '''
        Add current acquisition to self.data like dict
        '''
        self.data = dict()
        for item in range(self.ui.cb_type.count()):
            self.data[self.ui.cb_type.itemText(item)] = list()
        for row in range(self.ui.tbl_values.rowCount()):
            try:
                self.data[CELL_RD(self.ui.tbl_values, row, 0)].append(float(CELL_RD(self.ui.tbl_values, row, 1)))
            except:
                self.data[CELL_RD(self.ui.tbl_values, row, 0)].append(0.0)

...