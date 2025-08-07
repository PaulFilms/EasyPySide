Sub-Library of PySide6 with simplified Python Functions

![Last commit](https://img.shields.io/github/last-commit/PaulFilms/EasyPySide?label=Last%20commit)

<br>

## 🔧 Tools included

Module    | Description                                                  
----------|------------
forms     | A set of simple configuration forms for the most common uses 
tools     | Generic system tools (Type converters, fonts, delay, etc)    
widgets   | Simple functions for widget manipulation                     
---

<br>

## Installation Method

- Latest development version

   ```plaintext
   pip install git+https://github.com/PaulFilms/EasyPySide@main
   ```

<br>

## 🧪Examples

```python
from easypyside.forms import INFOBOX

INFOBOX(info='This is a warning info', winTitle='WARNING')
```

```python
from easypyside.tools import TIME_SLEEP

TIME_SLEEP(SEG=3)
```

```python
from PySide6.QtWidgets import QCheckBox
from PySide6.QtWidgets import QTableWidget
from easypyside.widgets import WIDGET_WR, WIDGET_RD, CELL_WR, CELL_RD

# QWidget
my_checkbox = QCheckBox(...)
WIDGET_WR(my_checkbox, True) # Write
value = WIDGET_RD(my_checkbox) # read

# QTableWidget 
my_table = QTableWidget(...)
CELL_WR(my_table, ROW=1, COLUMN=1, "Some value") # Write
value = CELL_RD(my_checkbox, ROW=1, COLUMN=1) # read
```

<br>

## 📦 Dependencies

This project relies on the following open-source libraries:

| Package      | License       | Description                                                   |
|--------------|---------------|---------------------------------------------------------------|
| `pyside6`    | LGPL 3.0 / GPL 3.0 | Official Qt for Python bindings — used for creating modern GUI applications. |
| `pandas`     | BSD 3-Clause  | High-performance data manipulation and analysis.              |
| `markdown2`  | MIT           | A fast and complete implementation of Markdown in Python.     |

---

<br>

## TASK 📒

- Create unit test
- FORMS | pyside6-rcc easypyside/__resources.qrc -o easypyside/__resources_rc.py
- WIDGETS | Add more compatible widgets

## WARNINGS ⛔

- ...
