# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QTABLE_FORM.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGridLayout,
    QHeaderView, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(478, 300)
        Dialog.setMinimumSize(QSize(450, 300))
        font = QFont()
        font.setFamilies([u"Roboto"])
        Dialog.setFont(font)
#if QT_CONFIG(tooltip)
        Dialog.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        Dialog.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        Dialog.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        Dialog.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        Dialog.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        Dialog.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        Dialog.setWindowFilePath(u"")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tbl_form = QTableWidget(Dialog)
        self.tbl_form.setObjectName(u"tbl_form")
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(10)
        self.tbl_form.setFont(font1)
#if QT_CONFIG(tooltip)
        self.tbl_form.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tbl_form.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.tbl_form.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.tbl_form.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.tbl_form.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.tbl_form.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tbl_form.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_form.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.tbl_form, 0, 0, 1, 1)

        self.btn_intro = QPushButton(Dialog)
        self.btn_intro.setObjectName(u"btn_intro")
        self.btn_intro.setMinimumSize(QSize(0, 50))
        self.btn_intro.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setFamilies([u"Roboto Black"])
        font2.setPointSize(15)
        self.btn_intro.setFont(font2)
#if QT_CONFIG(tooltip)
        self.btn_intro.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_intro.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.btn_intro.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.btn_intro.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.btn_intro.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.btn_intro.setText(u"INTRO")
#if QT_CONFIG(shortcut)
        self.btn_intro.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.gridLayout.addWidget(self.btn_intro, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
    # retranslateUi

