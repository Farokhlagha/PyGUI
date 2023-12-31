# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(474, 462)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(14, 71, 71);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy1)
        self.groupBox_5.setMinimumSize(QSize(0, 50))
        self.groupBox_5.setStyleSheet(u"background-color: rgb(40, 100, 71);\n"
"border: none;")
        self.rb_player = QRadioButton(self.groupBox_5)
        self.rb_player.setObjectName(u"rb_player")
        self.rb_player.setGeometry(QRect(10, 25, 131, 20))
        font = QFont()
        font.setPointSize(12)
        self.rb_player.setFont(font)
        self.rb_player.setStyleSheet(u"background-color: transparent;")
        self.rb_cpu = QRadioButton(self.groupBox_5)
        self.rb_cpu.setObjectName(u"rb_cpu")
        self.rb_cpu.setGeometry(QRect(10, 5, 121, 20))
        self.rb_cpu.setFont(font)
        self.rb_cpu.setStyleSheet(u"background-color: transparent;")
        self.rb_cpu.setChecked(True)

        self.gridLayout.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.btn_newgame = QPushButton(self.centralwidget)
        self.btn_newgame.setObjectName(u"btn_newgame")
        sizePolicy1.setHeightForWidth(self.btn_newgame.sizePolicy().hasHeightForWidth())
        self.btn_newgame.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.btn_newgame.setFont(font1)
        self.btn_newgame.setStyleSheet(u"background-color: rgb(40, 71, 100);")

        self.gridLayout.addWidget(self.btn_newgame, 0, 1, 1, 1)

        self.btn_about = QPushButton(self.centralwidget)
        self.btn_about.setObjectName(u"btn_about")
        sizePolicy1.setHeightForWidth(self.btn_about.sizePolicy().hasHeightForWidth())
        self.btn_about.setSizePolicy(sizePolicy1)
        self.btn_about.setFont(font1)
        self.btn_about.setStyleSheet(u"background-color: rgb(40, 100, 71);")

        self.gridLayout.addWidget(self.btn_about, 0, 2, 1, 1)

        self.btn1 = QPushButton(self.centralwidget)
        self.btn1.setObjectName(u"btn1")
        sizePolicy1.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(40)
        font2.setBold(True)
        self.btn1.setFont(font2)
        self.btn1.setStyleSheet(u"background-color: rgb(50, 100, 110);")

        self.gridLayout.addWidget(self.btn1, 1, 0, 1, 1)

        self.btn2 = QPushButton(self.centralwidget)
        self.btn2.setObjectName(u"btn2")
        sizePolicy1.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy1)
        self.btn2.setFont(font2)
        self.btn2.setStyleSheet(u"background-color: rgb(50, 100, 110);")

        self.gridLayout.addWidget(self.btn2, 1, 1, 1, 1)

        self.btn3 = QPushButton(self.centralwidget)
        self.btn3.setObjectName(u"btn3")
        sizePolicy1.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy1)
        self.btn3.setFont(font2)
        self.btn3.setStyleSheet(u"background-color: rgb(50, 100, 110);")

        self.gridLayout.addWidget(self.btn3, 1, 2, 1, 1)

        self.btn4 = QPushButton(self.centralwidget)
        self.btn4.setObjectName(u"btn4")
        sizePolicy1.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy1)
        self.btn4.setFont(font2)
        self.btn4.setStyleSheet(u"background-color: rgb(50, 100, 110);")

        self.gridLayout.addWidget(self.btn4, 2, 0, 1, 1)

        self.btn5 = QPushButton(self.centralwidget)
        self.btn5.setObjectName(u"btn5")
        sizePolicy1.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy1)
        self.btn5.setMinimumSize(QSize(148, 0))
        self.btn5.setFont(font2)
        self.btn5.setStyleSheet(u"background-color: rgb(50, 100, 110);")

        self.gridLayout.addWidget(self.btn5, 2, 1, 1, 1)

        self.btn6 = QPushButton(self.centralwidget)
        self.btn6.setObjectName(u"btn6")
        sizePolicy1.setHeightForWidth(self.btn6.sizePolicy().hasHeightForWidth())
        self.btn6.setSizePolicy(sizePolicy1)
        self.btn6.setMinimumSize(QSize(148, 0))
        self.btn6.setFont(font2)
        self.btn6.setStyleSheet(u"background-color: rgb(50, 100, 110);")

        self.gridLayout.addWidget(self.btn6, 2, 2, 1, 1)

        self.btn7 = QPushButton(self.centralwidget)
        self.btn7.setObjectName(u"btn7")
        sizePolicy1.setHeightForWidth(self.btn7.sizePolicy().hasHeightForWidth())
        self.btn7.setSizePolicy(sizePolicy1)
        self.btn7.setFont(font2)
        self.btn7.setStyleSheet(u"background-color: rgb(50, 100, 110);")

        self.gridLayout.addWidget(self.btn7, 3, 0, 1, 1)

        self.btn8 = QPushButton(self.centralwidget)
        self.btn8.setObjectName(u"btn8")
        sizePolicy1.setHeightForWidth(self.btn8.sizePolicy().hasHeightForWidth())
        self.btn8.setSizePolicy(sizePolicy1)
        self.btn8.setFont(font2)
        self.btn8.setStyleSheet(u"background-color: rgb(50, 100, 110);")

        self.gridLayout.addWidget(self.btn8, 3, 1, 1, 1)

        self.btn9 = QPushButton(self.centralwidget)
        self.btn9.setObjectName(u"btn9")
        sizePolicy1.setHeightForWidth(self.btn9.sizePolicy().hasHeightForWidth())
        self.btn9.setSizePolicy(sizePolicy1)
        self.btn9.setFont(font2)
        self.btn9.setStyleSheet(u"background-color: rgb(50, 100, 110);")

        self.gridLayout.addWidget(self.btn9, 3, 2, 1, 1)

        self.gb_x = QGroupBox(self.centralwidget)
        self.gb_x.setObjectName(u"gb_x")
        sizePolicy1.setHeightForWidth(self.gb_x.sizePolicy().hasHeightForWidth())
        self.gb_x.setSizePolicy(sizePolicy1)
        self.gb_x.setMinimumSize(QSize(0, 90))
        self.gb_x.setStyleSheet(u"background-color: gray; border: none;")
        self.gb_x.setTitle(u"")
        self.tb_x = QLineEdit(self.gb_x)
        self.tb_x.setObjectName(u"tb_x")
        self.tb_x.setGeometry(QRect(40, 30, 61, 55))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tb_x.sizePolicy().hasHeightForWidth())
        self.tb_x.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setPointSize(30)
        font3.setBold(True)
        self.tb_x.setFont(font3)
        self.tb_x.setStyleSheet(u"background-color: transparent; border: none;")
        self.tb_x.setAlignment(Qt.AlignCenter)
        self.tb_x.setReadOnly(True)
        self.textbox_11 = QLineEdit(self.gb_x)
        self.textbox_11.setObjectName(u"textbox_11")
        self.textbox_11.setGeometry(QRect(30, 0, 81, 41))
        sizePolicy2.setHeightForWidth(self.textbox_11.sizePolicy().hasHeightForWidth())
        self.textbox_11.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(True)
        self.textbox_11.setFont(font4)
        self.textbox_11.setStyleSheet(u"background-color: transparent; border: none;")
        self.textbox_11.setAlignment(Qt.AlignCenter)
        self.textbox_11.setReadOnly(True)

        self.gridLayout.addWidget(self.gb_x, 4, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.groupBox_3.setMinimumSize(QSize(0, 90))
        self.groupBox_3.setStyleSheet(u"background-color: gray; border: none;")
        self.tb_t = QLineEdit(self.groupBox_3)
        self.tb_t.setObjectName(u"tb_t")
        self.tb_t.setGeometry(QRect(40, 30, 61, 55))
        sizePolicy2.setHeightForWidth(self.tb_t.sizePolicy().hasHeightForWidth())
        self.tb_t.setSizePolicy(sizePolicy2)
        self.tb_t.setFont(font3)
        self.tb_t.setStyleSheet(u"background-color: transparent; border: none;")
        self.tb_t.setCursorPosition(1)
        self.tb_t.setAlignment(Qt.AlignCenter)
        self.tb_t.setReadOnly(True)
        self.textbox_12 = QLineEdit(self.groupBox_3)
        self.textbox_12.setObjectName(u"textbox_12")
        self.textbox_12.setGeometry(QRect(30, 0, 81, 41))
        sizePolicy2.setHeightForWidth(self.textbox_12.sizePolicy().hasHeightForWidth())
        self.textbox_12.setSizePolicy(sizePolicy2)
        self.textbox_12.setFont(font4)
        self.textbox_12.setStyleSheet(u"background-color: transparent; border: none;")
        self.textbox_12.setAlignment(Qt.AlignCenter)
        self.textbox_12.setReadOnly(True)

        self.gridLayout.addWidget(self.groupBox_3, 4, 1, 1, 1)

        self.gb_o = QGroupBox(self.centralwidget)
        self.gb_o.setObjectName(u"gb_o")
        sizePolicy1.setHeightForWidth(self.gb_o.sizePolicy().hasHeightForWidth())
        self.gb_o.setSizePolicy(sizePolicy1)
        self.gb_o.setMinimumSize(QSize(0, 90))
        self.gb_o.setStyleSheet(u"background-color: gray; border: none;")
        self.tb_o = QLineEdit(self.gb_o)
        self.tb_o.setObjectName(u"tb_o")
        self.tb_o.setGeometry(QRect(40, 30, 61, 55))
        sizePolicy2.setHeightForWidth(self.tb_o.sizePolicy().hasHeightForWidth())
        self.tb_o.setSizePolicy(sizePolicy2)
        self.tb_o.setFont(font3)
        self.tb_o.setStyleSheet(u"background-color: transparent; border: none;")
        self.tb_o.setAlignment(Qt.AlignCenter)
        self.tb_o.setReadOnly(True)
        self.tb_another = QLineEdit(self.gb_o)
        self.tb_another.setObjectName(u"tb_another")
        self.tb_another.setGeometry(QRect(20, 0, 111, 41))
        sizePolicy2.setHeightForWidth(self.tb_another.sizePolicy().hasHeightForWidth())
        self.tb_another.setSizePolicy(sizePolicy2)
        self.tb_another.setFont(font4)
        self.tb_another.setStyleSheet(u"background-color: transparent; border: none;")
        self.tb_another.setAlignment(Qt.AlignCenter)
        self.tb_another.setReadOnly(True)

        self.gridLayout.addWidget(self.gb_o, 4, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 474, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_5.setTitle("")
        self.rb_player.setText(QCoreApplication.translate("MainWindow", u"player vs player", None))
        self.rb_cpu.setText(QCoreApplication.translate("MainWindow", u"player vs cpu", None))
        self.btn_newgame.setText(QCoreApplication.translate("MainWindow", u"new game", None))
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"about", None))
        self.btn1.setText("")
        self.btn2.setText("")
        self.btn3.setText("")
        self.btn4.setText("")
        self.btn5.setText("")
        self.btn6.setText("")
        self.btn7.setText("")
        self.btn8.setText("")
        self.btn9.setText("")
        self.tb_x.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.textbox_11.setText(QCoreApplication.translate("MainWindow", u"X (YOU)", None))
        self.groupBox_3.setTitle("")
        self.tb_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.textbox_12.setText(QCoreApplication.translate("MainWindow", u"TIES", None))
        self.gb_o.setTitle("")
        self.tb_o.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tb_another.setText(QCoreApplication.translate("MainWindow", u"O (CPU)", None))
    # retranslateUi
