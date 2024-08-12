'''
Toolkit with simplified functions and methods for development with PySide6

TASK:
    - ...

WARNINGS:
    - All functions are copied of PyQt6 Library, ¡¡ be carefull !!
    - Only tested under Windows 11

________________________________________________________________________________________________ '''

''' SYSTEM LIBRARIES '''
import os
from enum import Enum, auto

''' EXTERNAL LIBRARIES '''
from PySide6.QtCore import QEventLoop, QTimer, QDate, QTime, QUrl
from PySide6.QtGui import QFont, QDesktopServices



''' CONTENT
________________________________________________________________________________________________ '''

def TIME_SLEEP(SEG: float=1):
    '''
    time.sleep function for use with PyQt 
    '''
    time = float(SEG) * 1000
    try:
        time = int(time)
    except:
        time = 10
        print(f"TIME_SLEEP ERROR / TIME (s): {SEG}")
    loop = QEventLoop()
    QTimer.singleShot(time, loop.quit)
    loop.exec()

def DATE_STR_CONVERTER(DATE: str = "2023-01-01") -> QDate:
    '''
    Convert string ISO format date to QDate
    DATE str Format: yyyy-mm-dd 
    '''
    if DATE == "2020-01-01" or DATE == "2020-1-1":
        return None
    try:
        ## OLD METHOD
        # year: int = int(DATE[:4])
        # month: int = int(DATE[5:-3])
        # day: int = int(DATE[-2:])
        ## NEW METHOD
        date_list = DATE.split("-")
        if len(date_list) != 3:
            date_list = DATE.split("/")
        if len(date_list) != 3:
            date_list = DATE.split(".")
        ## GET VALUES
        year = int(date_list[0])
        month = int(date_list[1])
        day = int(date_list[2])
        date = QDate(year, month, day)
        return date
    except:
        return None

def DATE_QDATE_CONVERTER(DATE: QDate) -> str:
    '''
    Convert QDate to string ISO format date
    DATE str Format: yyyy-mm-dd 
    '''
    if DATE == None:
        return None
    YEAR = DATE.year()
    MONTH = f"{DATE.month():02d}"
    DAY = f'{DATE.day():02d}'
    DATE = f"{YEAR}-{MONTH}-{DAY}"
    return DATE

def TIME_STR_CONVERTER(TIME: str = "00:00") -> QTime:
    '''
    Convert string format time to QTime
    TIME str Format: hh:mm
    '''
    try:
        hour: int = int(TIME[:2])
        minute: int = int(TIME[-2:])
        time = QTime(hour, minute)
        return time
    except:
        return None

def PATH_OPEN(path: str = os.getcwd()):
    '''
    Open the selected path using the QDesktopServices
    '''
    url = QUrl.fromLocalFile(path)
    QDesktopServices.openUrl(url)

class MYFONTS(Enum):
    '''
    '''
    FONT_LABEL = QFont("Roboto Black", pointSize=6, weight=8)
    FONT_WIDGET = QFont("Consolas", pointSize=12)
    FONT_TABLE = QFont("Consolas", pointSize=10)