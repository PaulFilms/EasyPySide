# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QLIST.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QListView,
    QListWidget, QListWidgetItem, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(259, 207)
        font = QFont()
        font.setFamilies([u"Roboto Black"])
        Dialog.setFont(font)
        Dialog.setWindowTitle(u"LIST FORM")
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
        Dialog.setWindowFilePath(u"")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lst = QListWidget(Dialog)
        self.lst.setObjectName(u"lst")
        self.lst.setMinimumSize(QSize(221, 0))
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(12)
        self.lst.setFont(font1)
#if QT_CONFIG(tooltip)
        self.lst.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lst.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.lst.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.lst.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.lst.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.lst.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.lst.setAlternatingRowColors(True)
        self.lst.setProperty("isWrapping", False)
        self.lst.setViewMode(QListView.ListMode)
        self.lst.setUniformItemSizes(False)
        self.lst.setWordWrap(False)
        self.lst.setSelectionRectVisible(False)

        self.gridLayout.addWidget(self.lst, 0, 0, 2, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        pass
    # retranslateUi

