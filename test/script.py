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
    subprocess.run(["pyside6-rcc", r"resources.qrc", "-o", r"lib_test/resources.py"])

print("CONVERTER .ui to .py ... [Write 1 to continue]")
if input("_ ") == "1":
    subprocess.run(["pyside6-uic", r"lib_test\__forms_ui\QLIST.ui", "-o", r"lib_test\__forms_ui\PYSIDE_QLIST.py"])

print()
print("FIN ------------------------------")
print()
