# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Result.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Result_Screen(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
                                 "	background-color:rgb(56, 58, 89);\n"
                                 "	color:rgb(220, 220, 220);\n"
                                 "	border-radius:10px;\n"
                                 "}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lbl_User_Heading = QLabel(self.frame)
        self.lbl_User_Heading.setObjectName(u"lbl_User_Heading")
        self.lbl_User_Heading.setGeometry(QRect(240, 30, 100, 40))
        font = QFont()
        font.setFamily(u"Calibri Light")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_User_Heading.setFont(font)
        self.lbl_User_Heading.setStyleSheet(u"color:rgb(254, 121, 199);")
        self.btn_submit = QPushButton(self.frame)
        self.btn_submit.setObjectName(u"btn_submit")
        self.btn_submit.clicked.connect(self.closeScreen)
        self.btn_submit.setGeometry(QRect(180, 430, 182, 30))
        font1 = QFont()
        font1.setFamily(u"Calibri Light")
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.btn_submit.setFont(font1)
        self.btn_submit.setStyleSheet(u"QPushButton{\n"
                                      "    background-color:rgb(93, 93, 154);\n"
                                      "    border-width: 2px;\n"
                                      "	color: white;\n"
                                      "    border-radius: 10px;\n"
                                      "    border-color: beige;\n"
                                      "    font: bold italic 14px;\n"
                                      "    min-width: 10em;\n"
                                      "    padding: 6px;\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color:  #06beb6;\n"
                                      "    border-style: inset;\n"
                                      "}\n"
                                      "")
        self.progrs_agreeableness = QProgressBar(self.frame)
        self.progrs_agreeableness.setObjectName(u"progrs_agreeableness")
        self.progrs_agreeableness.setGeometry(QRect(110, 310, 291, 22))
        font2 = QFont()
        font2.setFamily(u"Calibri Light")
        font2.setItalic(True)
        self.progrs_agreeableness.setFont(font2)
        self.progrs_agreeableness.setStyleSheet(u"QProgressBar {\n"
                                                "\n"
                                                "	background-color:rgb(98, 114, 164);\n"
                                                "	color:rgb(200,200,200);\n"
                                                "	border-style:none;\n"
                                                "	border-radius:10px;\n"
                                                "	text-align:center;\n"
                                                "\n"
                                                "}\n"
                                                "QProgressBar::chunk{\n"
                                                "	border-radius:10px;\n"
                                                "	background-color:qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523,stop:0 #de6262,stop:1 #ffb88c);\n"
                                                "}")
        self.progrs_agreeableness.setValue(0)
        self.progrs_extraversion = QProgressBar(self.frame)
        self.progrs_extraversion.setObjectName(u"progrs_extraversion")
        self.progrs_extraversion.setGeometry(QRect(110, 250, 291, 22))
        self.progrs_extraversion.setFont(font2)
        self.progrs_extraversion.setStyleSheet(u"QProgressBar {\n"
                                               "\n"
                                               "	background-color:rgb(98, 114, 164);\n"
                                               "	color:rgb(200,200,200);\n"
                                               "	border-style:none;\n"
                                               "	border-radius:10px;\n"
                                               "	text-align:center;\n"
                                               "\n"
                                               "}\n"
                                               "QProgressBar::chunk{\n"
                                               "	border-radius:10px;\n"
                                               "	background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #F55887, stop:1 #FF759F)\n"
                                               "}")
        self.progrs_extraversion.setValue(0)
        self.progrs_neuroticism = QProgressBar(self.frame)
        self.progrs_neuroticism.setObjectName(u"progrs_neuroticism")
        self.progrs_neuroticism.setGeometry(QRect(110, 370, 291, 22))
        self.progrs_neuroticism.setFont(font2)
        self.progrs_neuroticism.setStyleSheet(u"QProgressBar {\n"
                                              "\n"
                                              "	background-color:rgb(98, 114, 164);\n"
                                              "	color:rgb(200,200,200);\n"
                                              "	border-style:none;\n"
                                              "	border-radius:10px;\n"
                                              "	text-align:center;\n"
                                              "\n"
                                              "}\n"
                                              "QProgressBar::chunk{\n"
                                              "	border-radius:10px;\n"
                                              "	background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #eacda3, stop:1 #d6ae7b);\n"
                                              "}")
        self.progrs_neuroticism.setValue(0)
        self.progrs_conscientiousness = QProgressBar(self.frame)
        self.progrs_conscientiousness.setObjectName(u"progrs_conscientiousness")
        self.progrs_conscientiousness.setGeometry(QRect(110, 190, 291, 22))
        self.progrs_conscientiousness.setFont(font2)
        self.progrs_conscientiousness.setStyleSheet(u"QProgressBar {\n"
                                                    "	background-color:rgb(98, 114, 164);\n"
                                                    "	color:rgb(200,200,200);\n"
                                                    "	border-style:none;\n"
                                                    "	border-radius:10px;\n"
                                                    "	text-align:center;\n"
                                                    "\n"
                                                    "}\n"
                                                    "QProgressBar::chunk{\n"
                                                    "	border-radius:10px;\n"
                                                    "	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(93, 242, 168, 255), stop:1 rgba(171, 171, 171, 255));\n"
                                                    "}")
        self.progrs_conscientiousness.setValue(0)
        self.progrs_oppeness = QProgressBar(self.frame)
        self.progrs_oppeness.setObjectName(u"progrs_oppeness")
        self.progrs_oppeness.setGeometry(QRect(110, 130, 291, 22))
        self.progrs_oppeness.setFont(font2)
        self.progrs_oppeness.setStyleSheet(u"QProgressBar {\n"
                                           "	background-color:rgb(98, 114, 164);\n"
                                           "	color:rgb(200,200,200);\n"
                                           "	border-style:none;\n"
                                           "	border-radius:10px;\n"
                                           "	text-align:center;\n"
                                           "    Opacity:0.5;\n"
                                           "\n"
                                           "}\n"
                                           "QProgressBar::chunk{\n"
                                           "	border-radius:10px;\n"
                                           "	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #06beb6, stop: 1 #48b1bf);\n"
                                           "setVisible: False;\n"
                                           "}")
        self.progrs_oppeness.setMaximum(100)
        self.progrs_oppeness.setValue(0)
        self.progrs_oppeness.setTextVisible(False)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 100, 71, 21))
        font3 = QFont()
        font3.setPointSize(13)
        self.label.setFont(font3)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 160, 136, 21))
        self.label_2.setFont(font3)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 220, 101, 21))
        self.label_3.setFont(font3)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 280, 111, 21))
        self.label_4.setFont(font3)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 340, 91, 21))
        self.label_5.setFont(font3)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi




    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_User_Heading.setText(QCoreApplication.translate("MainWindow", u"RESULT", None))
        self.btn_submit.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.progrs_agreeableness.setFormat("")
        self.progrs_extraversion.setFormat("")
        self.progrs_neuroticism.setFormat("")
        self.progrs_conscientiousness.setFormat("")
        self.progrs_oppeness.setFormat("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Openess", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Conscientiousness", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Extraversion", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Agreeableness", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Neuroticism", None))

    # retranslateUi
    # loader(1,2,3,4,5)[agrre,opens,nue,xtro,con)
    # loader(0,1,2,3,4)[agrre,opens,nue,xtro,con)
    def changeProgress(self, *argv):

        self.progrs_agreeableness.setValue(argv[0])
        self.progrs_extraversion.setValue(argv[3])
        self.progrs_neuroticism.setValue(argv[2])
        self.progrs_conscientiousness.setValue(argv[4])
        self.progrs_oppeness.setValue(argv[1])
        print("Progress Bars valued changed ")
    def closeScreen(self):
        print("closing")



