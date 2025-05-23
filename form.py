# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QToolBar,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(532, 457)
        MainWindow.setMaximumSize(QSize(532, 457))
        icon = QIcon()
        icon.addFile(u":/images/pil.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(32, 32))
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.actionAfsluiten = QAction(MainWindow)
        self.actionAfsluiten.setObjectName(u"actionAfsluiten")
        icon1 = QIcon()
        icon1.addFile(u":/images/shutdown-icon-11830.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAfsluiten.setIcon(icon1)
        self.actionAfsluiten.setMenuRole(QAction.MenuRole.NoRole)
        self.actionBestellen = QAction(MainWindow)
        self.actionBestellen.setObjectName(u"actionBestellen")
        icon2 = QIcon()
        icon2.addFile(u":/images/buy-icon-png-31616.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionBestellen.setIcon(icon2)
        self.actionBestellen.setMenuRole(QAction.MenuRole.NoRole)
        self.actionUpdate = QAction(MainWindow)
        self.actionUpdate.setObjectName(u"actionUpdate")
        icon3 = QIcon()
        icon3.addFile(u":/images/update-icon-png-25.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionUpdate.setIcon(icon3)
        self.actionUpdate.setMenuRole(QAction.MenuRole.NoRole)
        self.actionToevoegen = QAction(MainWindow)
        self.actionToevoegen.setObjectName(u"actionToevoegen")
        icon4 = QIcon()
        icon4.addFile(u":/images/plus-icon-13091.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionToevoegen.setIcon(icon4)
        self.actionToevoegen.setMenuRole(QAction.MenuRole.NoRole)
        self.actionVerwijderen = QAction(MainWindow)
        self.actionVerwijderen.setObjectName(u"actionVerwijderen")
        icon5 = QIcon()
        icon5.addFile(u":/images/delete-button-png-28554.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionVerwijderen.setIcon(icon5)
        self.actionVerwijderen.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/images/pillen.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.page_3)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_5 = QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(181, 331))
        self.frame.setMaximumSize(QSize(181, 331))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lwPillen = QListWidget(self.frame)
        self.lwPillen.setObjectName(u"lwPillen")

        self.verticalLayout_3.addWidget(self.lwPillen)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(120, 331))
        self.frame_3.setMaximumSize(QSize(120, 331))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(20, 121, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.btnNaarRechts = QPushButton(self.frame_3)
        self.btnNaarRechts.setObjectName(u"btnNaarRechts")

        self.verticalLayout_4.addWidget(self.btnNaarRechts)

        self.btnNaarLinks = QPushButton(self.frame_3)
        self.btnNaarLinks.setObjectName(u"btnNaarLinks")

        self.verticalLayout_4.addWidget(self.btnNaarLinks)

        self.verticalSpacer_2 = QSpacerItem(20, 120, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(181, 331))
        self.frame_2.setMaximumSize(QSize(181, 331))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lwBestellen = QListWidget(self.frame_2)
        self.lwBestellen.setObjectName(u"lwBestellen")

        self.verticalLayout_2.addWidget(self.lwBestellen)

        self.btnBestellen = QPushButton(self.frame_2)
        self.btnBestellen.setObjectName(u"btnBestellen")

        self.verticalLayout_2.addWidget(self.btnBestellen)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.frame_4 = QFrame(self.page_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 20, 181, 311))
        self.frame_4.setMinimumSize(QSize(181, 311))
        self.frame_4.setMaximumSize(QSize(181, 311))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.plainTextEdit = QPlainTextEdit(self.frame_4)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_6.addWidget(self.plainTextEdit)

        self.frame_5 = QFrame(self.page_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(240, 20, 171, 311))
        self.frame_5.setMinimumSize(QSize(171, 311))
        self.frame_5.setMaximumSize(QSize(171, 311))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_3 = QSpacerItem(20, 35, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(131, 26))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label)

        self.verticalSpacer_4 = QSpacerItem(20, 35, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.lineEditTotPrijs = QLineEdit(self.frame_5)
        self.lineEditTotPrijs.setObjectName(u"lineEditTotPrijs")
        self.lineEditTotPrijs.setMinimumSize(QSize(50, 22))
        self.lineEditTotPrijs.setMaximumSize(QSize(50, 22))
        self.lineEditTotPrijs.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEditTotPrijs.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEditTotPrijs)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer = QSpacerItem(148, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_7.addItem(self.horizontalSpacer)

        self.verticalSpacer_5 = QSpacerItem(20, 36, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)

        self.btnPrintBestelling = QPushButton(self.frame_5)
        self.btnPrintBestelling.setObjectName(u"btnPrintBestelling")
        self.btnPrintBestelling.setMinimumSize(QSize(121, 23))

        self.verticalLayout_7.addWidget(self.btnPrintBestelling)

        self.verticalSpacer_6 = QSpacerItem(20, 35, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_6)

        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_16 = QVBoxLayout(self.page_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.groupBox = QGroupBox(self.page_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(201, 341))
        self.groupBox.setMaximumSize(QSize(201, 341))
        self.verticalLayout_9 = QVBoxLayout(self.groupBox)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lwUpdaten = QListWidget(self.groupBox)
        self.lwUpdaten.setObjectName(u"lwUpdaten")

        self.verticalLayout_9.addWidget(self.lwUpdaten)


        self.horizontalLayout_8.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.page_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(250, 280))
        self.groupBox_2.setMaximumSize(QSize(250, 280))
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(44, 41))
        self.label_3.setMaximumSize(QSize(44, 41))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEditUpdateID = QLineEdit(self.groupBox_2)
        self.lineEditUpdateID.setObjectName(u"lineEditUpdateID")
        self.lineEditUpdateID.setMinimumSize(QSize(51, 22))
        self.lineEditUpdateID.setMaximumSize(QSize(51, 22))
        self.lineEditUpdateID.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEditUpdateID.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEditUpdateID)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_10.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(44, 41))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEditUpdateNaam = QLineEdit(self.groupBox_2)
        self.lineEditUpdateNaam.setObjectName(u"lineEditUpdateNaam")
        self.lineEditUpdateNaam.setMinimumSize(QSize(120, 22))
        self.lineEditUpdateNaam.setMaximumSize(QSize(120, 22))

        self.horizontalLayout_4.addWidget(self.lineEditUpdateNaam)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(44, 41))
        self.label_5.setMaximumSize(QSize(44, 41))

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEditUpdateVolume = QLineEdit(self.groupBox_2)
        self.lineEditUpdateVolume.setObjectName(u"lineEditUpdateVolume")
        self.lineEditUpdateVolume.setMinimumSize(QSize(120, 22))
        self.lineEditUpdateVolume.setMaximumSize(QSize(120, 22))

        self.horizontalLayout_5.addWidget(self.lineEditUpdateVolume)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(44, 41))
        self.label_6.setMaximumSize(QSize(44, 41))

        self.horizontalLayout_6.addWidget(self.label_6)

        self.lineEditUpdatePrijs = QLineEdit(self.groupBox_2)
        self.lineEditUpdatePrijs.setObjectName(u"lineEditUpdatePrijs")
        self.lineEditUpdatePrijs.setMinimumSize(QSize(51, 22))
        self.lineEditUpdatePrijs.setMaximumSize(QSize(51, 22))
        self.lineEditUpdatePrijs.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEditUpdatePrijs.setReadOnly(False)

        self.horizontalLayout_6.addWidget(self.lineEditUpdatePrijs)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.btnUpdaten = QPushButton(self.groupBox_2)
        self.btnUpdaten.setObjectName(u"btnUpdaten")
        self.btnUpdaten.setMinimumSize(QSize(84, 23))
        self.btnUpdaten.setMaximumSize(QSize(84, 23))

        self.horizontalLayout_7.addWidget(self.btnUpdaten)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_8.addWidget(self.groupBox_2)


        self.verticalLayout_16.addLayout(self.horizontalLayout_8)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_12 = QVBoxLayout(self.page_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_17)

        self.groupBox_3 = QGroupBox(self.page_5)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(271, 281))
        self.groupBox_3.setMaximumSize(QSize(271, 281))
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)

        self.lineEditToevoegenNaam = QLineEdit(self.groupBox_3)
        self.lineEditToevoegenNaam.setObjectName(u"lineEditToevoegenNaam")
        self.lineEditToevoegenNaam.setMinimumSize(QSize(171, 22))
        self.lineEditToevoegenNaam.setMaximumSize(QSize(171, 22))

        self.horizontalLayout_12.addWidget(self.lineEditToevoegenNaam)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_13)


        self.verticalLayout_11.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)

        self.lineEditToevoegenVolume = QLineEdit(self.groupBox_3)
        self.lineEditToevoegenVolume.setObjectName(u"lineEditToevoegenVolume")
        self.lineEditToevoegenVolume.setMinimumSize(QSize(171, 22))
        self.lineEditToevoegenVolume.setMaximumSize(QSize(171, 22))

        self.horizontalLayout_11.addWidget(self.lineEditToevoegenVolume)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_14)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_11)

        self.lineEditToevoegenPrijs = QLineEdit(self.groupBox_3)
        self.lineEditToevoegenPrijs.setObjectName(u"lineEditToevoegenPrijs")
        self.lineEditToevoegenPrijs.setMinimumSize(QSize(71, 22))
        self.lineEditToevoegenPrijs.setMaximumSize(QSize(71, 22))

        self.horizontalLayout_10.addWidget(self.lineEditToevoegenPrijs)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_15)


        self.verticalLayout_11.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_12)

        self.btnToevoegenDatabase = QPushButton(self.groupBox_3)
        self.btnToevoegenDatabase.setObjectName(u"btnToevoegenDatabase")
        self.btnToevoegenDatabase.setMinimumSize(QSize(111, 23))
        self.btnToevoegenDatabase.setMaximumSize(QSize(111, 23))

        self.horizontalLayout_9.addWidget(self.btnToevoegenDatabase)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_16)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_13.addWidget(self.groupBox_3)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_18)


        self.verticalLayout_12.addLayout(self.horizontalLayout_13)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_15 = QVBoxLayout(self.page_6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.groupBox_4 = QGroupBox(self.page_6)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(201, 341))
        self.groupBox_4.setMaximumSize(QSize(201, 341))
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.lwVerwijderen = QListWidget(self.groupBox_4)
        self.lwVerwijderen.setObjectName(u"lwVerwijderen")

        self.verticalLayout_13.addWidget(self.lwVerwijderen)


        self.horizontalLayout_14.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.page_6)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(250, 280))
        self.groupBox_5.setMaximumSize(QSize(250, 280))
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(44, 41))
        self.label_7.setMaximumSize(QSize(44, 41))

        self.horizontalLayout_15.addWidget(self.label_7)

        self.lineEditVerwijderID = QLineEdit(self.groupBox_5)
        self.lineEditVerwijderID.setObjectName(u"lineEditVerwijderID")
        self.lineEditVerwijderID.setMinimumSize(QSize(51, 22))
        self.lineEditVerwijderID.setMaximumSize(QSize(51, 22))
        self.lineEditVerwijderID.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEditVerwijderID.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.lineEditVerwijderID)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_19)


        self.verticalLayout_14.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(44, 41))

        self.horizontalLayout_16.addWidget(self.label_8)

        self.lineEditVerwijderNaam = QLineEdit(self.groupBox_5)
        self.lineEditVerwijderNaam.setObjectName(u"lineEditVerwijderNaam")
        self.lineEditVerwijderNaam.setMinimumSize(QSize(120, 22))
        self.lineEditVerwijderNaam.setMaximumSize(QSize(120, 22))

        self.horizontalLayout_16.addWidget(self.lineEditVerwijderNaam)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_20)


        self.verticalLayout_14.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_9 = QLabel(self.groupBox_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(44, 41))
        self.label_9.setMaximumSize(QSize(44, 41))

        self.horizontalLayout_17.addWidget(self.label_9)

        self.lineEditVerwijderVolume = QLineEdit(self.groupBox_5)
        self.lineEditVerwijderVolume.setObjectName(u"lineEditVerwijderVolume")
        self.lineEditVerwijderVolume.setMinimumSize(QSize(120, 22))
        self.lineEditVerwijderVolume.setMaximumSize(QSize(120, 22))

        self.horizontalLayout_17.addWidget(self.lineEditVerwijderVolume)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_21)


        self.verticalLayout_14.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(44, 41))
        self.label_10.setMaximumSize(QSize(44, 41))

        self.horizontalLayout_18.addWidget(self.label_10)

        self.lineEditVerwijderPrijs = QLineEdit(self.groupBox_5)
        self.lineEditVerwijderPrijs.setObjectName(u"lineEditVerwijderPrijs")
        self.lineEditVerwijderPrijs.setMinimumSize(QSize(51, 22))
        self.lineEditVerwijderPrijs.setMaximumSize(QSize(51, 22))
        self.lineEditVerwijderPrijs.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEditVerwijderPrijs.setReadOnly(False)

        self.horizontalLayout_18.addWidget(self.lineEditVerwijderPrijs)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_22)


        self.verticalLayout_14.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_23)

        self.btnVerwijderen = QPushButton(self.groupBox_5)
        self.btnVerwijderen.setObjectName(u"btnVerwijderen")
        self.btnVerwijderen.setMinimumSize(QSize(84, 23))
        self.btnVerwijderen.setMaximumSize(QSize(84, 23))

        self.horizontalLayout_19.addWidget(self.btnVerwijderen)


        self.verticalLayout_14.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_14.addWidget(self.groupBox_5)


        self.verticalLayout_15.addLayout(self.horizontalLayout_14)

        self.stackedWidget.addWidget(self.page_6)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionAfsluiten)
        self.toolBar.addAction(self.actionBestellen)
        self.toolBar.addAction(self.actionUpdate)
        self.toolBar.addAction(self.actionToevoegen)
        self.toolBar.addAction(self.actionVerwijderen)

        self.retranslateUi(MainWindow)
        self.actionAfsluiten.triggered.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAfsluiten.setText(QCoreApplication.translate("MainWindow", u"Afsluiten", None))
#if QT_CONFIG(tooltip)
        self.actionAfsluiten.setToolTip(QCoreApplication.translate("MainWindow", u"Afsluiten", None))
#endif // QT_CONFIG(tooltip)
        self.actionBestellen.setText(QCoreApplication.translate("MainWindow", u"Bestellen", None))
#if QT_CONFIG(tooltip)
        self.actionBestellen.setToolTip(QCoreApplication.translate("MainWindow", u"Pillen Bestellen", None))
#endif // QT_CONFIG(tooltip)
        self.actionUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
#if QT_CONFIG(tooltip)
        self.actionUpdate.setToolTip(QCoreApplication.translate("MainWindow", u"Pillen Opwaarderen", None))
#endif // QT_CONFIG(tooltip)
        self.actionToevoegen.setText(QCoreApplication.translate("MainWindow", u"Toevoegen", None))
#if QT_CONFIG(tooltip)
        self.actionToevoegen.setToolTip(QCoreApplication.translate("MainWindow", u"Pillen toevoegen", None))
#endif // QT_CONFIG(tooltip)
        self.actionVerwijderen.setText(QCoreApplication.translate("MainWindow", u"Verwijderen", None))
#if QT_CONFIG(tooltip)
        self.actionVerwijderen.setToolTip(QCoreApplication.translate("MainWindow", u"Pillen verwijderen", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText("")
        self.btnNaarRechts.setText(QCoreApplication.translate("MainWindow", u">>>", None))
        self.btnNaarLinks.setText(QCoreApplication.translate("MainWindow", u"<<<", None))
        self.btnBestellen.setText(QCoreApplication.translate("MainWindow", u"Bestelling maken", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Prijs totale bestelling", None))
        self.btnPrintBestelling.setText(QCoreApplication.translate("MainWindow", u"Print Bestelling", None))
        self.groupBox.setTitle("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Updaten", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"id:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"naam", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"volume", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"prijs", None))
        self.btnUpdaten.setText(QCoreApplication.translate("MainWindow", u"Updaten", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Toevoegen", None))
        self.lineEditToevoegenNaam.setPlaceholderText(QCoreApplication.translate("MainWindow", u"naam", None))
        self.lineEditToevoegenVolume.setPlaceholderText(QCoreApplication.translate("MainWindow", u"volume", None))
        self.lineEditToevoegenPrijs.setPlaceholderText(QCoreApplication.translate("MainWindow", u"prijs", None))
        self.btnToevoegenDatabase.setText(QCoreApplication.translate("MainWindow", u"Toevoegen", None))
        self.groupBox_4.setTitle("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Verwijderen", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"id:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"naam", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"volume", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"prijs", None))
        self.btnVerwijderen.setText(QCoreApplication.translate("MainWindow", u"Verwijderen", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

