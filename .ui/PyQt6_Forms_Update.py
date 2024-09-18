import os
import subprocess

print("PyQt6 Forms Update ----------")
print(os.getcwd())

## Set the PYSIDE6DEPLOY_QT_LIB environment variable
# os.environ["PYSIDE6DEPLOY_QT_LIB"] = "PySide6"
# PYSIDE6DEPLOY_QT_LIB="PySide6"
# print(os.environ["PYSIDE6DEPLOY_QT_LIB"])

## Run the pyuic6 tool
SUBPROCESS_LIST = [
    # ["pyuic6", "-x", "forms/PYQT_QLIST.ui", "-o", "forms/PYQT_QLIST.py"] # La opcion -x es para crear el eejecutable
    ["pyuic6", "Forms_UI/QACQUISITIONS.ui", "-o", "pydeveloptools/forms/PYQT_QACQUISITIONS.py"],
    ["pyuic6", "Forms_UI/QCALENDAR.ui", "-o", "pydeveloptools/forms/PYQT_QCALENDAR.py"],
    ["pyuic6", "Forms_UI/QLICENSE.ui", "-o", "pydeveloptools/forms/PYQT_QLICENSE.py"],
    ["pyuic6", "Forms_UI/QLIST_FORM.ui", "-o", "pydeveloptools/forms/PYQT_QLIST_FORM.py"],
    ["pyuic6", "Forms_UI/QLIST.ui", "-o", "pydeveloptools/forms/PYQT_QLIST.py"],
    ["pyuic6", "Forms_UI/QMARKDOWN.ui", "-o", "pydeveloptools/forms/PYQT_QMARKDOWN.py"],
    ["pyuic6", "Forms_UI/QTABLE_DICT.ui", "-o", "pydeveloptools/forms/PYQT_QTABLE_DICT.py"],
    ["pyuic6", "Forms_UI/QTABLE_FORM.ui", "-o", "pydeveloptools/forms/PYQT_QTABLE_FORM.py"],
]
for procss in SUBPROCESS_LIST:
    subprocess.run(procss)

print("FIN ----------")
print()