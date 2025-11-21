'''
Toolkit with simplified functions and methods for development with PySide6

INCOMPLETE:

- QTime edit wraps

PLANNED:

- 

'''
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'
__update__ = '2025.10.28'

''' SYSTEM LIBRARIES '''
from dataclasses import dataclass
from enum import Enum, auto
# from re import match
from typing import Any, List, Tuple, Union, TYPE_CHECKING
# from unittest import case

''' EXTERNAL LIBRARIES '''
from PySide6.QtCore import QDate, QTime, Qt, Signal
from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import QWidget, QHBoxLayout, QHeaderView
from PySide6.QtWidgets import QLineEdit, QTextEdit, QComboBox, QSpinBox, QDoubleSpinBox, QCheckBox, QDateEdit, QTimeEdit, QPushButton, QPlainTextEdit
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
# if TYPE_CHECKING:
import pandas as pd

''' INTERNAL LIBRARIES '''
from .tools import DATE_QDATE_CONVERTER, DATE_STR_CONVERTER, TIME_STR_CONVERTER



''' CONTENT
________________________________________________________________________________________________ '''

class CheckBoxCell(QWidget):
    '''
    Customized QCheckBox with center layout inside cell 
    '''
    # Reemitimos la señal del checkbox
    stateChanged = Signal(int)
    # cellStateChanged = Signal(int, int, bool)       # (row, column, checked)

    def __init__(self, checked=False, parent=None, parent_table: QTableWidget = None, row: int = None, column: int = None):
        super().__init__(parent)

        self.parent_table = parent_table
        self.row = row
        self.column = column

        self.checkbox = QCheckBox()
        self.checkbox.setChecked(checked)

        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.checkbox)

        # Reemitir la señal
        self.checkbox.stateChanged.connect(self._on_state_changed)
        self.checkbox.stateChanged.connect(self.stateChanged.emit)

    def isChecked(self):
        return self.checkbox.isChecked()

    def setChecked(self, value: bool):
        self.checkbox.setChecked(value)

    def _on_state_changed(self, state: int):
        """Cuando cambia el estado, actualiza la celda actual si la tabla es conocida."""
        if self.parent_table and self.row is not None and self.column is not None:
            # 🔹 Actualizamos la celda activa en la tabla
            self.parent_table.setCurrentCell(self.row, self.column)

    # def _on_state_changed(self, state: int):
    #     """
    #     Cuando cambia el estado:
    #     - Actualiza la celda actual (currentCell)
    #     - Emite una señal con (row, column, checked)
    #     """
    #     if self.parent_table and self.row is not None and self.column is not None:
    #         self.parent_table.setCurrentCell(self.row, self.column)

    #         # 🔹 Emitir señal extendida
    #         self.cellStateChanged.emit(self.row, self.column, self.isChecked())



def WIDGET_WR(WIDGET: QWidget, VALUE: Any) -> None:
    '''
    Edit value in selected QtWidgets \n
    
    Supported QtWidgets:
        - QTextEdit / QLineEdit
        - QComboBox
        - QSpinBox / QDoubleSpinBox
        - QCheckBox
        - QDateEdit <str: "yyyy-mm-dd"> / QTimeEdit <str: "hh:mm">
        - QPushButton
        - QWidget (Layout) <QCheckBox>
    '''
    match WIDGET:
        case QLineEdit() | QTextEdit():
            if not VALUE:
                WIDGET.setText("")
            else:
                WIDGET.setText(str(VALUE))
        case QComboBox():
            if WIDGET.count() == 0:
                WIDGET.addItem(str(VALUE))
            WIDGET.setCurrentIndex(WIDGET.findText(VALUE))
        case QSpinBox():
            if not VALUE:
                WIDGET.setValue(WIDGET.minimum())
            else:
                WIDGET.setValue(int(VALUE))
        case QDoubleSpinBox():
            if not VALUE:
                WIDGET.setValue(WIDGET.minimum())
            else:
                WIDGET.setValue(float(VALUE))
        case QCheckBox() | CheckBoxCell():
            if isinstance(VALUE, bool):
                WIDGET.setChecked(VALUE)
            elif isinstance(VALUE, str):
                truthy = {"1", "true", "yes", "on", "t", "y"}
                if VALUE.lower() in truthy:
                    isChecked: bool = True
                else:
                    isChecked: bool = False
                WIDGET.setChecked(isChecked)
            else: 
                WIDGET.setChecked(False)
        case QDateEdit():
            if not VALUE:
                WIDGET.setDate(QDate(WIDGET.minimumDate()))
            elif isinstance(VALUE, QDate):
                WIDGET.setDate(VALUE)
            elif isinstance(VALUE, str): # 2023-01-01 / 2023-1-1
                DATE = DATE_STR_CONVERTER(VALUE)
                if DATE:
                    WIDGET.setDate(DATE)
                else:
                    WIDGET.setDate(QDate(WIDGET.minimumDate()))
        case QTimeEdit():
            if not VALUE:
                WIDGET.setTime(QTime(WIDGET.minimumTime()))
            elif isinstance(VALUE, QTime):
                WIDGET.setTime(VALUE)
            elif isinstance(VALUE, str) and len(VALUE) == 5: # 01:12
                time = TIME_STR_CONVERTER(VALUE)
                if time and time.isValid():
                    WIDGET.setTime(time)
                else:
                    WIDGET.setTime(QTime(WIDGET.minimumDate()))
            else:
                WIDGET.setTime(QTime(WIDGET.minimumDate()))
        case QPushButton():
            WIDGET.setText(str(VALUE))
        case QWidget(): # <LAYOUT>
           for child in WIDGET.findChildren(QWidget):
                try:
                    WIDGET_WR(child, VALUE) # Recursión
                except Exception as e:
                    print(f"WIDGET_WR ERROR: {e} / {type(child)}")
        ## NOT IMPLEMENTED
        case _:
            print("WIDGET_WR", type(WIDGET), "/ NOT IMPLEMENTED")

def WIDGET_RD(WIDGET: QWidget) -> Any:
    '''
    Read value of selected QtWidgets

    `Supported QtWidgets:`
        - QTextEdit / QLineEdit / QPlainTextEdit
        - QPushButton
        - QComboBox
        - QSpinBox / QDoubleSpinBox
        - QCheckBox
        - QDateEdit <str: "yyyy-mm-dd"> / QTimeEdit <str: "hh:mm">
    '''
    match WIDGET:
        case QLineEdit() | QTextEdit():
            return WIDGET.text()
        case QPlainTextEdit():
            return WIDGET.toPlainText()
        case QComboBox():
            return WIDGET.currentText()
        case QCheckBox():
            return WIDGET.isChecked()
        case CheckBoxCell():
            return WIDGET.isChecked()
        case QSpinBox():
            return WIDGET.value()
        case QDoubleSpinBox():
            return WIDGET.value()
        case QDateEdit():
            return DATE_QDATE_CONVERTER(WIDGET.date())
        case QTimeEdit():
            return f"{WIDGET.time().hour():02d}:{WIDGET.time().minute():02d}"
        case QPushButton():
            return WIDGET.text()
        case QWidget(): # <LAYOUT> ⚠️
            for child in WIDGET.findChildren(QWidget):
                try:
                    return WIDGET_RD(child)
                except Exception as e:
                    print(f"WIDGET_RD ERROR: {e} / {type(child)}")
        case _:
            print("WIDGET_RD", type(WIDGET), "/ NOT IMPLEMENTED")
            return None

def WIDGET_CLEAR(WIDGET, widgetEnabled: bool = False):
    '''
    Clear data of select widget \n
    `Supported QtWidgets:`
        - QComboBox
        - QLineEdit / QTextEdit
        - QCheckBox
        - QSpinBox
        - QDateEdit
        - QTimeEdit
        - QTableWidget

    ** widgetEnabled: Set the widget like "not enabled" before to clear \n
    ** with QTableWidget only set to 0 the row count \n
    
    BUG:
        - QComboBox:
            - Hay que ver si merece la pena hacer clear
    '''
    if widgetEnabled: 
        WIDGET.setEnabled(False)
    ## QComboBox
    if type(WIDGET) == QComboBox:
        WIDGET.clear()
        WIDGET.setCurrentText("")
    ## QLineEdit
    elif type(WIDGET) == QLineEdit:
        WIDGET.setText("")
    ## QTextEdit
    elif type(WIDGET) == QTextEdit:
        WIDGET.setText("")
    ## QCheckBox
    elif type(WIDGET) == QCheckBox:
        WIDGET.setChecked(False)
    ## QSpinBox
    elif type(WIDGET) == QSpinBox:
        WIDGET.setValue(WIDGET.minimum())
    ## QDoubleSpinBox
    elif type(WIDGET) == QDoubleSpinBox:
        WIDGET.setValue(WIDGET.minimum())
    ## QDateEdit
    elif type(WIDGET) == QDateEdit:
        WIDGET.setDate(QDate(WIDGET.minimumDate()))
    ## QTimeEdit
    elif type(WIDGET) == QTimeEdit:
        WIDGET.setTime(QTime(WIDGET.minimumTime()))
    ## QTableWidget
    elif type(WIDGET) == QTableWidget:
        WIDGET.setRowCount(0)
    ## QWidget <LAYOUT>
    elif type(WIDGET) == QWidget:
        # QCheckBox
        CHILD = WIDGET.findChild(type(QCheckBox()))
        if type(CHILD) == QCheckBox:
            CHILD.setChecked(False)
    ## NOT IMPLEMENTED
    else:
        print("WIDGET_CLEAR", type(WIDGET), "/ NOT IMPLEMENTED")
    if widgetEnabled: 
        WIDGET.setEnabled(True)

def WIDGET_CONNECT(WIDGET, FUNCTION):
    '''
    Connect select widget with selected function\n
    `Supported QtWidgets:`
        - QComboBox
        - QLineEdit / QTextEdit
        - QCheckBox
        - QSpinBox
        - QDoubleSpinBox
        - QDateEdit
        - QTimeEdit
        - QWidget <LAYOUT>: QCheckBox
    '''
    ## QComboBox
    if type(WIDGET) == QComboBox:
        WIDGET.currentTextChanged.connect(FUNCTION)
    ## QLineEdit / QTextEdit
    elif type(WIDGET) == QLineEdit or type(WIDGET) == QTextEdit:
        WIDGET.textChanged.connect(FUNCTION)
    ## QCheckBox
    elif type(WIDGET) == QCheckBox:
        WIDGET.stateChanged.connect(FUNCTION)
    ## CheckBoxCell
    elif type(WIDGET) == CheckBoxCell:
        WIDGET.stateChanged.connect(FUNCTION)
    ## QSpinBox
    elif type(WIDGET) == QSpinBox:
        WIDGET.valueChanged.connect(FUNCTION)
    ## QDoubleSpinBox
    elif type(WIDGET) == QDoubleSpinBox:
        WIDGET.valueChanged.connect(FUNCTION)
    ## QDateEdit
    elif type(WIDGET) == QDateEdit:
        WIDGET.dateChanged.connect(FUNCTION)
    ## QTimeEdit
    elif type(WIDGET) == QTimeEdit:
        WIDGET.timeChanged.connect(FUNCTION)
    ## QWidget <LAYOUT>
    elif type(WIDGET) == QWidget:
        # QCheckBox
        CHILD = WIDGET.findChild(type(QCheckBox()))
        if type(CHILD) == QCheckBox:
            CHILD.stateChanged.connect(FUNCTION)
    ## NOT IMPLEMENTED
    else:
        print("WIDGET_CONNECT", type(WIDGET), "/ NOT IMPLEMENTED")

def CELL_WR(TABLE: QTableWidget, ROW: int, COLUMN: Union[int, str], VALUE: Any):
    '''
    Write value in select cell
    '''
    COLUMN_INDEX: int = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    ##
    WIDGET = TABLE.cellWidget(ROW, COLUMN_INDEX)
    if WIDGET:
        WIDGET_WR(WIDGET, VALUE)
    else:
        ITEM = QTableWidgetItem()
        if VALUE != None:
            ITEM = QTableWidgetItem(str(VALUE))
        TABLE.setItem(ROW, COLUMN_INDEX, ITEM)

def CELL_RD(TABLE: QTableWidget, ROW: int, COLUMN: Union[int, str]) -> Any:
    """
    Read value of selected cell

    Supported cellWidget:
        - QLineEdit / QTextEdit
        - QComboBox
        - QSpinBox / QDoubleSpinBox
        - QCheckBox / CheckBoxCell
        - QDateEdit
        - QPushButton (debug)
    """
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    # print(
    #     'cellWidget', TABLE.cellWidget(ROW, COLUMN_INDEX), '\n',
    #     'item', TABLE.item(ROW, COLUMN_INDEX), '\n',
    # )

    # --- 1. Try to read from cellWidget ---
    CELL = TABLE.cellWidget(ROW, COLUMN_INDEX)
    if CELL:
        match CELL:
            case QLineEdit() | QTextEdit():
                return CELL.text()
            case QComboBox():
                return CELL.currentText()
            case QCheckBox() | CheckBoxCell():
                return CELL.isChecked()
            case QSpinBox() | QDoubleSpinBox():
                return CELL.value()
            case QDateEdit():
                return DATE_QDATE_CONVERTER(CELL.date())
            case QPushButton():
                return CELL.text()
            case _:
                print("CELL_RD cellWidget:", type(CELL), "/ NOT IMPLEMENTED")
                return None

    # --- 2. Try to read from QTableWidgetItem ---
    ITEM = TABLE.item(ROW, COLUMN_INDEX)
    if ITEM:
        item_type = ITEM.data(Qt.UserRole)

        # Si el ítem es checkable, devuelve bool
        if item_type == "checkable":
            # print('checkState')
            return ITEM.checkState() == Qt.Checked

        # Texto del item
        text = ITEM.text().strip()
        if text:
            # print('text', text)
            return text

        # Normaliza valores comunes a tipos Python
        # lower = text.lower()
        # if lower in {"true", "1", "yes", "y", "on"}:
        #     return True
        # if lower in {"false", "0", "no", "n", "off"}:
        #     return False

        # Int o float si es posible
        # for cast in (int, float):
        #     try:
        #         return cast(text)
        #     except ValueError:
        #         continue

        # Fallback a string
        # return text

    # --- 3. Si no hay nada ---
    return None

def CELL_READONLY(TABLE: QTableWidget, ROW: int, COLUMN: Union[int, str]) -> None:
    '''
    Set the cell as non-editable \n

    ** If edit a protected cell, the cell loses protection
    '''
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    ## CELL WIDGET
    CELL: QWidget = TABLE.cellWidget(ROW, COLUMN_INDEX)
    if CELL:
        CELL.setEnabled(False)
        return
    ## TABLE ITEM
    ITEM: QTableWidgetItem = TABLE.item(ROW, COLUMN_INDEX)
    if ITEM:
        ITEM.setFlags(ITEM.flags() ^ Qt.ItemFlag.ItemIsEditable)
        return
    ## NULL ITEM
    ITEM = QTableWidgetItem()
    ITEM.setFlags(ITEM.flags() ^ Qt.ItemFlag.ItemIsEditable)
    TABLE.setItem(ROW, COLUMN_INDEX, ITEM)

def CELL_EDITABLE(TABLE: QTableWidget, ROW: int, COLUMN: Union[int, str], EDITABLE: bool) -> None:
    """
    Activa o desactiva la edición de una celda en un QTableWidget.

    Args:
        TABLE: QTableWidget donde está la celda.
        ROW: Fila de la celda.
        COLUMN: Índice o nombre de columna (usa TBL_GET_HEADER_INDEX).
        EDITABLE: True para editable, False para solo lectura.
    """
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)

    # --- Caso 1: la celda tiene un widget incrustado (QLineEdit, QComboBox, etc.)
    CELL: QWidget = TABLE.cellWidget(ROW, COLUMN_INDEX)
    if CELL:
        CELL.setEnabled(EDITABLE)
        return

    # --- Caso 2: la celda tiene un QTableWidgetItem
    ITEM: QTableWidgetItem = TABLE.item(ROW, COLUMN_INDEX)
    if not ITEM:
        ITEM = QTableWidgetItem()
        TABLE.setItem(ROW, COLUMN_INDEX, ITEM)

    FLAGS = ITEM.flags()

    if EDITABLE:
        # Agregamos la bandera de edición
        FLAGS |= Qt.ItemFlag.ItemIsEditable
    else:
        # Quitamos la bandera de edición
        FLAGS &= ~Qt.ItemFlag.ItemIsEditable

    ITEM.setFlags(FLAGS)

def CELL_TX(TABLE: QTableWidget, ROW: int, COLUMN: Union[int, str], TEXT: Any) -> QTableWidgetItem:
    '''
    Set Text Item in selected cell

    Signal : itemChanged
    '''
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    ##
    TABLE.setCellWidget(ROW, COLUMN_INDEX, None)
    ITEM = QTableWidgetItem("" if TEXT is None else str(TEXT))

    # Desactivar momentáneamente la señal para evitar recursión
    # try:
    #     TABLE.blockSignals(True)
    TABLE.setItem(ROW, COLUMN_INDEX, ITEM)
    # finally:
    #     TABLE.blockSignals(False)

    return ITEM

def CELL_COMBOBOX(TABLE: QTableWidget, ROW: int, COLUMN: Union[int, str], LIST: list | tuple, EDITABLE: bool = False) -> QComboBox:
    '''
    setCellWidget -> QComboBox
    '''
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    ##
    combo = QComboBox()
    combo.setEditable(EDITABLE)
    combo.list = LIST
    combo.addItems(LIST)
    ##
    TABLE.setCellWidget(ROW,COLUMN_INDEX,combo)
    return combo

def CELL_CHECKSTATE(TABLE: QTableWidget, ROW: int, COLUMN: Union[int, str], VALUE: bool) -> QTableWidgetItem:
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    item_check = QTableWidgetItem()
    item_check.setFlags(item_check.flags() | Qt.ItemIsUserCheckable)
    if VALUE:
        item_check.setCheckState(Qt.Checked)
    else:
        item_check.setCheckState(Qt.Unchecked)
    TABLE.setItem(ROW, COLUMN_INDEX, item_check)
    return item_check

def CELL_CHECKBOX(TABLE: QTableWidget, ROW: int, COLUMN: Union[int, str], STATE: bool = False) -> CheckBoxCell:
    '''
    setCellWidget -> QWidget
    '''
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)

    # checkBox = QCheckBox()
    checkBox = CheckBoxCell(
        checked=bool(STATE),
        parent_table=TABLE, 
        row=ROW, 
        column=COLUMN_INDEX
    )

    TABLE.setCellWidget(ROW, COLUMN_INDEX, checkBox)
    return checkBox

# def CELL_CHECKBOX_LAYOUT(TABLE: QTableWidget, ROW: int, COLUMN: Union[int, str], STATE: bool = False) -> QCheckBox:
#     '''
#     setCellWidget -> QWidget <QCheckBox>
#     Set the QCheckBox centered into cell
#     '''
#     COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
#     ##
#     widget = QWidget()
#     # item = QCheckBox()
#     # if STATE == 1 or STATE == "1" or STATE == True or STATE == "TRUE":
#     #     item.setChecked(True)
#     # else:
#     #     item.setChecked(False)
#     checkbox = QCheckBox()
#     checkbox.setChecked(bool(STATE in [1, "1", True, "TRUE"]))
#     def select_cell() -> None:
#         TABLE.setCurrentCell(ROW, COLUMN_INDEX)
#     # item.stateChanged.connect(select_cell)
#     layout = QHBoxLayout()
#     layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
#     # layout.addWidget(item)
#     layout.addWidget(checkbox)
#     layout.setContentsMargins(0,0,0,0)
#     widget.setLayout(layout)
#     ##
#     TABLE.setCellWidget(ROW, COLUMN_INDEX, widget)

#     return checkbox

def CELL_SPINBOX(TABLE: QTableWidget, ROW: int, COLUMN: Union[int, str], VALUE: int, MIN: int = 0, MAX: int = 99) -> QSpinBox:
    '''
    setCellWidget -> QSpinBox
    '''
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    ##
    widget = QSpinBox()
    widget.setMinimum(MIN)
    widget.setMaximum(MAX)
    widget.setValue(VALUE)
    ##
    TABLE.setCellWidget(ROW, COLUMN_INDEX, widget)
    return widget

def CELL_DATEEDIT(TABLE: QTableWidget, ROW: int, COLUMN: Union[int, str]) -> QDateEdit:
    '''
    setCellWidget -> QDateEdit
    '''
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    widget = QDateEdit()
    widget.setSpecialValueText("-")
    widget.setMinimumDate(QDate(2020,1,1))
    widget.setMaximumDate(QDate(2100,1,1))
    widget.setDisplayFormat("yyyy-MM-dd")
    ##
    TABLE.setCellWidget(ROW, COLUMN_INDEX, widget)
    return widget

def CELL_TIMEEDIT(TABLE: QTableWidget, ROW: int, COLUMN: Union[int, str], TIME: Union[QTime, str]) -> QTimeEdit:
    '''
    setCellWidget -> QTimeEdit
    '''
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    widget = QTimeEdit()
    widget.setMinimumTime(QTime(0,0,0))
    if isinstance(TIME, QTime):
        widget.setTime(TIME)
    elif isinstance(TIME, str):
        widget.setTime(TIME_STR_CONVERTER(TIME))
    widget.setButtonSymbols(QTimeEdit.NoButtons)
    # widget.setReadOnly(True)
    ##
    TABLE.setCellWidget(ROW, COLUMN_INDEX, widget)
    return widget

def CELL_FONT(TABLE: QTableWidget, ROW: int, COLUMN: Union[int, str], SIZE: int=10, BOLD: bool=True, fontFamily="Consolas"):
    '''
    INCOMPLETE
    '''
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    ##
    font = QFont()
    font.setFamily(fontFamily)
    font.setPointSize(SIZE)
    font.setBold(BOLD)
    ITEM = TABLE.item(ROW, COLUMN_INDEX)
    # print("ITEM: ", ITEM)
    if ITEM == None: 
        TABLE.setItem(ROW, COLUMN_INDEX, QTableWidgetItem(""))
    ITEM.setFont(font)

class COLORS(Enum):
    '''
    Standard colors
    '''
    GREEN = QColor(0, 80, 0)
    YELLOW = QColor(210, 190, 80)
    RED = color = QColor(100, 0, 0)
    # BLACK = QColor
    # GREY = QColor

def CELL_COLOR(TABLE: QTableWidget, ROW: int, COLUMN: Union[int, str], COLOR: QColor) -> None:
    '''
    Set the backgroung Color of a cel with selected str color
    BUG: Incomplete
    '''
    TABLE.setAlternatingRowColors(False)
    COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, COLUMN)
    if TABLE.item(ROW, COLUMN_INDEX) is None:
        TABLE.setItem(ROW, COLUMN_INDEX, QTableWidgetItem())
    item = TABLE.item(ROW, COLUMN_INDEX)
    # item.setBackground(None)
    # if COLOR:
    item.setBackground(COLOR)

@dataclass
class TBL_FIELD_FORMAT:
    '''
    '''
    FIELD_NAME: str
    COLUMN: int
    ALIAS: str
    TYPE_DATA: Union[bool, str, int, float]
    DATA: list
    WIDTH: int = None
    PROTECT: bool = False
    HIDE: bool = False

# @dataclass
# class TBL_FIELD:
#     id: int
#     width: int = None
#     resize: bool = True
#     hide: bool = False

def TBL_INIT(TABLE: QTableWidget) -> None:
    '''
    Reset the Table, set 0 rowCount
    '''
    TABLE.setEnabled(False)
    TABLE.setRowCount(0)
    TABLE.setColumnCount(0)
    TABLE.setEnabled(True)

def TBL_POP_PANDAS_DF(TABLE: QTableWidget, DATAFRAME: 'pd.DataFrame', HIDE_COLUMNS: list=[], PROTECTED_COLUMNS: list=[]) -> None:
    '''
    Populate QTable with a Pandas DataFrame
    
    VARIABLES:
        - HIDE_COLUMNS: list **Hide the list of columns by int (column index) or str (calumn name)
        - PROTECTED_COLUMNS: list **Config the list of columns selected by int (column index) or str (calumn name)
    
    BUG: 
        - Some times show: QAbstractItemView::closeEditor called with an editor that does not belong to this view
        - Add the TBL_FIELD_FORMAT class
    '''
    ## INIT TBL
    TABLE.setEnabled(False)
    TABLE.setRowCount(0)
    TABLE.setColumnCount(0)
    ## 
    columns = DATAFRAME.columns.to_list()
    TABLE.setColumnCount(len(columns))
    TABLE.setHorizontalHeaderLabels(columns)
    TABLE.setRowCount(len(DATAFRAME.index))

    # def is_protected(col_idx):
    #     # Normalize protected columns to indices for quick lookup
    #     protected_indices = []
    #     for prot in PROTECTED_COLUMNS:
    #         if isinstance(prot, int):
    #             protected_indices.append(prot)
    #         elif isinstance(prot, str) and prot in columns:
    #             protected_indices.append(columns.index(prot))
    #     return col_idx in protected_indices
    
    ## POPULATE TABLE CELLS
    # Populate table cells
    for row_idx, (_, row_data) in enumerate(DATAFRAME.iterrows()):
        for col_idx, col_name in enumerate(columns):
            cell_value = row_data[col_name]
            if pd.isnull(cell_value):
                continue
            
            # Decide which cell widget to use based on dtype
            dtype = DATAFRAME[col_name].dtype
            if dtype == bool:
                CELL_CHECKBOX(TABLE, row_idx, col_idx, cell_value)
            # elif dtype.kind in ('i', 'u', 'f'):  # integer, unsigned, float
            #     CELL_SPINBOX(TABLE, row_idx, col_idx, cell_value)
            # elif dtype.kind == 'M':  # datetime64
            #     CELL_DATEEDIT(TABLE, row_idx, col_idx, cell_value)
            elif dtype == object and isinstance(cell_value, str):
                CELL_TX(TABLE, row_idx, col_idx, cell_value)
            else:
                CELL_WR(TABLE, row_idx, col_idx, cell_value)
            
            # Apply protection if column is in protected list
            # if is_protected(col_idx):
            if col_name in PROTECTED_COLUMNS or col_idx in PROTECTED_COLUMNS:
                CELL_READONLY(TABLE, row_idx, col_idx)

    ## HIDE COLUMS
    for col in HIDE_COLUMNS:
        if isinstance(col, int) and 0 <= col < len(columns):
            TABLE.setColumnHidden(col, True)
        elif isinstance(col, str) and col in columns:
            TABLE.setColumnHidden(columns.index(col), True)
    
    ## POP ROWS
    TABLE.resizeColumnsToContents()
    TABLE.setEnabled(True)

def TBL_GET_HEADERS(TABLE: QTableWidget) -> List[str]:
    '''
    Get a list of horizontal headers in the selected Qtable

    ** If header name is empty, function return the int of column
    '''
    # HEADERS: list = []
    # for head in range(TABLE.columnCount()):
    #     header_text = TABLE.horizontalHeaderItem(head).text()
    #     if header_text == "" or header_text == None: 
    #         header_text = head
    #     HEADERS.append(header_text)
    # return HEADERS
    return [TABLE.horizontalHeaderItem(i).text() for i in range(TABLE.columnCount())]

def TBL_GET_HEADER_INDEX(TABLE: QTableWidget, COLUMN: Union[int, str]) -> int:
    '''
    Get the index value of selected Header

    ** If the header name is not correct return None value, check after function the result in case of error
    '''
    if type(COLUMN) == int:
        return COLUMN
    elif type(COLUMN) == str:
        HEADERS = TBL_GET_HEADERS(TABLE)
        # if COLUMN in HEADERS: 
        #     return HEADERS.index(COLUMN)
        # else:
        #     print(f"CELL_RD ERROR / WRONG HEADER NAME [{COLUMN}]")
        #     return None
        return HEADERS.index(COLUMN) if COLUMN in HEADERS else None

def TBL_FIELD_RESIZE(TABLE: QTableWidget, header: Union[int, str]) -> None:
    '''
    '''
    header_indx = TBL_GET_HEADER_INDEX(TABLE, COLUMN=header)
    TABLE.horizontalHeader().setSectionResizeMode(header_indx, QHeaderView.ResizeMode.Fixed)

def TBL_GET_PANDAS_DF(TABLE: QTableWidget) -> 'pd.DataFrame':
    '''
    Create Pandas DataFrame from QTable data
    '''
    HEADERS: list = TBL_GET_HEADERS(TABLE)
    ## 
    DATAFRAME: dict = {}
    for field in HEADERS: 
        LIST: list = []
        for row in range(TABLE.rowCount()):
            VALUE = CELL_RD(TABLE, row, field)
            LIST.append(VALUE)
        DATAFRAME[field] = LIST
    ## 
    DATAFRAME = pd.DataFrame(DATAFRAME)
    return DATAFRAME

def TBL_VHEADER_WIDTH_FIX(TABLE: QTableWidget, COLUMNS: List[int] | List[str] | Tuple[int] | Tuple[str]):
    '''
    Set the field selected in COLUMNS list as fixed column width
    '''
    for col in COLUMNS:
        COLUMN_INDEX = TBL_GET_HEADER_INDEX(TABLE, col)
        TABLE.horizontalHeader().setSectionResizeMode(COLUMN_INDEX, QHeaderView.ResizeMode.Fixed)
