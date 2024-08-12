import os
import subprocess

print()
print("START FLEXICAL DESKTOP SCRIPT")
print("-----------------------------")
print()

print("SYS PATH:")
print(os.getcwd())
print()

# print("VENV Activate ... [Write 1 to continue]")
# if input("_ ") == "1":
#     venv_path = r".venv\Scripts\activate.bat"
#     subprocess.call(venv_path, shell=True, stdout=subprocess.PIPE)

print("RESOURCES .qrc to .py ... [Write 1 to continue]")
if input("_ ") == "1":
    subprocess.run(["pyside6-rcc", r"lib_test/__resources.qrc", "-o", r"lib_test/__resources_rc.py"])

print("CONVERTER .ui to .py ... [Write 1 to continue]")
if input("_ ") == "1":
    # subprocess.run(["pyside6-uic", "forms_ui/FLEXICALv3.ui", "-o", "_data/GUI.py"])
    # subprocess.run(["pyside6-uic", "forms_ui/DEVELOPER.ui", "-o", "_data/DEV.py"])
    # subprocess.run(["pyside6-uic", "forms_ui/CAL_DATA.ui", "-o", "_data/DIAG_CALDATA.py"])
    # subprocess.run(["pyside6-uic", "forms_ui/TEMPLATES.ui", "-o", "_data/DIAG_TEMPLATE.py"])
    # subprocess.run(["pyside6-uic", "forms_ui/AUTOMATION.ui", "-o", "_data/DIAG_AUTOMATION.py"])
    pass

print()
print("FIN ------------------------------")
print()
