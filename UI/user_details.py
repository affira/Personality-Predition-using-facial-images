# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'User_Details.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys

import cv2
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import matplotlib.pyplot as plt
import keras
import numpy as np
import tensorflow as tf
from skimage.transform import resize
from main2 import Progress_bar
from Result_screen import Result_Screen


class ResultWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Result_Screen()
        self.ui.setupUi(self)
        self.ui.btn_submit.clicked.connect(self.close)

    def change(self, *argv):
        self.ui.changeProgress(argv[0], argv[1], argv[2], argv[3], argv[4])

class ProgressWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Progress_bar()
        self.ui.setupUi(self)



class UserDetails(object):
    path = ""

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        font = QFont()
        font.setFamily(u"Calibri Light")
        font.setPointSize(10)
        font.setItalic(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(56, 58, 89);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 10, 751, 511))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_textfields = QFrame(self.frame)
        self.frame_textfields.setObjectName(u"frame_textfields")
        self.frame_textfields.setGeometry(QRect(280, 140, 371, 171))
        self.frame_textfields.setStyleSheet(u"background-color: rgb(56, 58, 89);")
        self.frame_textfields.setFrameShape(QFrame.StyledPanel)
        self.frame_textfields.setFrameShadow(QFrame.Raised)
        self.txt_name = QTextEdit(self.frame_textfields)
        self.txt_name.setObjectName(u"txt_name")
        self.txt_name.setGeometry(QRect(10, 30, 241, 41))
        self.txt_name.setStyleSheet(u"QTextEdit{\n"
                                    "    background-color: white;\n"
                                    "    border-width: 2px;\n"
                                    "	color: #9b9bff;\n"
                                    "    border-radius: 10px;\n"
                                    "    border-color: beige;\n"
                                    "    font: Italic 14px;\n"
                                    "    min-width: 10em;\n"
                                    "    padding: 6px;\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.lbl_User_Image = QLabel(self.frame_textfields)
        self.lbl_User_Image.setObjectName(u"lbl_User_Image")
        self.lbl_User_Image.setGeometry(QRect(30, 120, 71, 31))
        font1 = QFont()
        font1.setFamily(u"Calibri Light")
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.lbl_User_Image.setFont(font1)
        self.lbl_User_Image.setStyleSheet(u"color:rgb(254, 121, 199);")
        self.frame_labels = QFrame(self.frame)
        self.frame_labels.setObjectName(u"frame_labels")
        self.frame_labels.setGeometry(QRect(60, 120, 191, 231))
        self.frame_labels.setStyleSheet(u"background-color: rgb(56, 58, 89);")
        self.frame_labels.setFrameShape(QFrame.StyledPanel)
        self.frame_labels.setFrameShadow(QFrame.Raised)
        self.lbl_User_name = QLabel(self.frame_labels)
        self.lbl_User_name.setObjectName(u"lbl_User_name")
        self.lbl_User_name.setGeometry(QRect(140, 50, 81, 31))
        font2 = QFont()
        font2.setFamily(u"Calibri Light")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setWeight(75)
        self.lbl_User_name.setFont(font2)
        self.lbl_User_name.setStyleSheet(u"color:rgb(254, 121, 199);")
        self.frame_heading = QFrame(self.frame)
        self.frame_heading.setObjectName(u"frame_heading")
        self.frame_heading.setGeometry(QRect(200, 20, 431, 80))
        self.frame_heading.setStyleSheet(u"background-color: rgb(56, 58, 89);")
        self.frame_heading.setFrameShape(QFrame.StyledPanel)
        self.frame_heading.setFrameShadow(QFrame.Raised)
        self.lbl_User_Heading = QLabel(self.frame_heading)
        self.lbl_User_Heading.setObjectName(u"lbl_User_Heading")
        self.lbl_User_Heading.setGeometry(QRect(20, 20, 371, 41))
        font3 = QFont()
        font3.setFamily(u"Calibri Light")
        font3.setPointSize(27)
        font3.setBold(True)
        font3.setItalic(True)
        font3.setWeight(75)
        self.lbl_User_Heading.setFont(font3)
        self.lbl_User_Heading.setStyleSheet(u"color:rgb(254, 121, 199);")
        self.frame_buttons = QFrame(self.frame)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setGeometry(QRect(160, 410, 391, 31))
        self.frame_buttons.setStyleSheet(u"background-color: rgb(56, 58, 89);\n"
                                         "")
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.btn_browse = QPushButton(self.frame)
        self.btn_browse.setObjectName(u"btn_browse")
        self.btn_browse.clicked.connect(self.getImage)
        self.btn_browse.setGeometry(QRect(240, 300, 182, 28))
        font4 = QFont()
        font4.setBold(False)
        font4.setItalic(True)
        font4.setWeight(50)
        self.btn_browse.setFont(font4)
        self.btn_browse.setStyleSheet(u"QPushButton{\n"
                                      "    background-color: rgb(93, 93, 154);\n"
                                      "    border-width: 2px;\n"
                                      "	color: white;\n"
                                      "    border-radius: 10px;\n"
                                      "    border-color: beige;\n"
                                      "    font: Italic 14px;\n"
                                      "    min-width: 10em;\n"
                                      "    padding: 6px;\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: #9b9bff;\n"
                                      "    border-style: inset;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "")
        self.btn_process = QPushButton(self.frame)
        self.btn_process.setObjectName(u"btn_process")
        self.btn_process.clicked.connect(self.loadmodel)
        self.btn_process.setGeometry(QRect(180, 380, 301, 31))
        font5 = QFont()
        font5.setBold(True)
        font5.setItalic(False)
        font5.setWeight(75)
        self.btn_process.setFont(font5)
        # self.btn_process.clicked.connect(self.loader)
        self.btn_process.setStyleSheet(u"QPushButton{\n"
                                       "    background-color: rgb(93, 93, 154);\n"
                                       "    border-width: 2px;\n"
                                       "	color: white;\n"
                                       "    border-radius: 10px;\n"
                                       "    border-color: beige;\n"
                                       "    font: bold  14px;\n"
                                       "    min-width: 10em;\n"
                                       "    padding: 6px;\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: #9b9bff;\n"
                                       "    border-style: inset;\n"
                                       "}\n"
                                       "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def checkImage(self):
        myImage = self.path
        faceCascade = cv2.CascadeClassifier('H:\\FYP\\UI\\venv\\haarcascade_frontalface_default.xml')
        image = cv2.imread(myImage)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(100, 100)
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print("Length Of Faces === :",len(faces))
        if len(faces) == 1 :
            print("faces found ")
            return True
        else:
            print("face not found ")
            return False

    def getImage(self):
        a = self.txt_name.toPlainText()
        if len(a) > 0:
            FileDialog = QFileDialog.getOpenFileName(self.btn_browse, "Open a file", "directoryToOpen",
                                                     "Images (*.png *.jpeg *.jpg);;Text files (*.txt);;XML files ("
                                                     "*.xml)");
            print(FileDialog[0], len(a))
            if FileDialog[0]:
                self.path = FileDialog[0]
            else:
                print('img file chk')
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setStyleSheet(
                    'QMessageBox {background-color:rgb(93, 93, 154); color: white;}\n QMessageBox {color: white;}\n'
                    ' QPushButton{color: white; font: Italic 14px; background-color: rgb(254, 121, 199); '
                    'border-radius: 10px; padding: 10px; text-align: center;}\n QPushButton:hover{color: white;}')
                msg.setText(" Choose an img !")
                msg.setWindowTitle("Error selecting img")
                # "D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\icons8-cbs-512.ico"))
                msg.exec_()
        else:
            print('text filed len check')
            msg = QMessageBox()
            msg.setStyleSheet(
                'QMessageBox {background-color:rgb(93, 93, 154); color: white;}\n QMessageBox {color: white;}\n'
                ' QPushButton{color: white; font: Italic 14px; background-color: rgb(254, 121, 199); '
                'border-radius: 10px; padding: 10px; text-align: center;}\n QPushButton:hover{color: white;}')
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Enter Name !")
            msg.setWindowTitle("Error in browsing")
            # "D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\icons8-cbs-512.ico"))
            msg.exec_()

    def loadmodel(self):
        a = self.txt_name.toPlainText()
        if len(a) > 0:
            if self.path!="" :
                faceExist = self.checkImage()
                if (faceExist):
                    model = tf.keras.models.load_model('H:\\FYP\\UI\\facemodel.h5')
                    new_image = plt.imread(self.path)
                    new_image_resized = resize(new_image, (64, 64, 3))
                    pred = model.predict(np.array([new_image_resized, ]))
                    print(pred)
                    c = list(pred[0])
                    print(max(c))
                    c = c.index(max(c))
                    # self.prg.hide()
                    if c == 0:
                        # loader(1,2,3,4,5)[agrre,opens,nue,xtro,con)
                        self.loader(0, 100, 0, 0, 0)

                    if c == 1:
                        # loader(1,2,3,4,5)[agrre,opens,nue,xtro,con)
                        self.loader(0, 0, 0, 0, 100)
                    if c == 2:
                        # loader(1,2,3,4,5)[agrre,opens,nue,xtro,con)
                        self.loader(0, 0, 0, 100, 0)
                    if c == 3:
                        # loader(1,2,3,4,5)[agrre,opens,nue,xtro,con)
                        self.loader(100, 0, 0, 0, 0)
                    if c == 4:
                        # loader(1,2,3,4,5)[agrre,opens,nue,xtro,con)
                        self.loader(0, 0, 100, 0, 0)
                else:

                    msg = QMessageBox()
                    msg.setFixedSize(500, 500);
                    msg.setStyleSheet(
                        'QMessageBox {background-color:rgb(93, 93, 154); color: white;}\n QMessageBox {color: white;}\n'
                        ' QPushButton{color: white; font: Italic 14px; background-color: rgb(254, 121, 199); '
                        'border-radius: 10px; padding: 10px; text-align: center;}\n QPushButton:hover{color: white;}')
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Face not Found")
                    msg.setWindowTitle("Error in processing")
                    msg.exec_()
            else:

                msg = QMessageBox()
                msg.setFixedSize(500, 500);
                msg.setStyleSheet(
                    'QMessageBox {background-color:rgb(93, 93, 154); color: white;}\n QMessageBox {color: white;}\n'
                    ' QPushButton{color: white; font: Italic 14px; background-color: rgb(254, 121, 199); '
                    'border-radius: 10px; padding: 10px; text-align: center;}\n QPushButton:hover{color: white;}')
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Upload Img !")
                msg.setWindowTitle("Error in processing")
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setFixedSize(500, 500);
            msg.setStyleSheet(
                'QMessageBox {background-color:rgb(93, 93, 154); color: white;}\n QMessageBox {color: white;}\n'
                ' QPushButton{color: white; font: Italic 14px; background-color: rgb(254, 121, 199); '
                'border-radius: 10px; padding: 10px; text-align: center;}\n QPushButton:hover{color: white;}')
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Enter Name!")
            msg.setWindowTitle("Error in processing")
            msg.exec_()

    def loader(self, *argv, **kwargs):
        self.main = ResultWindow()
        self.main.show()

        self.main.change(argv[0], argv[1], argv[2], argv[3], argv[4])

    # setupUi

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = Progress_bar()
        sys.exit(app.exec_())

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"User", None))
        self.lbl_User_Image.setText(QCoreApplication.translate("MainWindow", u"Image:", None))
        self.lbl_User_name.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.lbl_User_Heading.setText(QCoreApplication.translate("MainWindow", u"USER INFORMATION", None))
        # if QT_CONFIG(tooltip)
        self.btn_browse.setToolTip(QCoreApplication.translate("MainWindow",
                                                              u"QString s1 = QFileDialog::getOpenFileName(this, \"Open a file\", \"directoryToOpen\", \"Images (*.png *.xpm *.jpg);;Text files (*.txt);;XML files (*.xml)\");",
                                                              None))
        # endif // QT_CONFIG(tooltip)
        self.btn_browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.btn_browse.setProperty("QString s1", QCoreApplication.translate("MainWindow",
                                                                             u"QFileDialog::getOpenFileName(this, \"Open a file\", \"directoryToOpen\",\n"
                                                                             "        \"Images (*.png *.xpm *.jpg);;Text files (*.txt);;XML files (*.xml)\");",
                                                                             None))
        self.btn_process.setText(QCoreApplication.translate("MainWindow", u"Process Image", None))

    # retranslateUi
