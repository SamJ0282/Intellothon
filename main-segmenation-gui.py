# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'try_image.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(807, 482)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 10, 261, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(280, 40, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(280, 60, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(280, 80, 67, 17))
        self.label_4.setObjectName("label_4")
        self.inputModel = QtWidgets.QComboBox(Dialog)
        self.inputModel.setGeometry(QtCore.QRect(30, 190, 191, 25))
        self.inputModel.setObjectName("inputModel")
        self.inputModel.addItem("")
        self.inputModel.addItem("")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 150, 171, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:blue")
        self.label_5.setObjectName("label_5")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(280, 140, 241, 281))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 239, 279))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setGeometry(QtCore.QRect(50, 10, 131, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: blue")
        self.label_7.setObjectName("label_7")
        self.chooseImage = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.chooseImage.setGeometry(QtCore.QRect(50, 50, 111, 25))
        self.chooseImage.setObjectName("chooseImage")
        self.inputImage = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.inputImage.setGeometry(QtCore.QRect(30, 100, 161, 131))
        self.inputImage.setText("")
        self.inputImage.setScaledContents(True)
        self.inputImage.setObjectName("inputImage")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(640, 150, 67, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:blue")
        self.label_8.setObjectName("label_8")
        self.outputImage = QtWidgets.QLabel(Dialog)
        self.outputImage.setGeometry(QtCore.QRect(580, 240, 171, 141))
        self.outputImage.setText("")
        self.outputImage.setScaledContents(True)
        self.outputImage.setObjectName("outputImage")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 120, 791, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(10, 465, 791, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(790, 130, 20, 351))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(-20, 130, 51, 341))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(0, 120, 16, 23))
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(0, 460, 16, 23))
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(790, 120, 16, 16))
        self.radioButton_3.setText("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(790, 460, 16, 23))
        self.radioButton_4.setText("")
        self.radioButton_4.setObjectName("radioButton_4")
        self.processButton = QtWidgets.QPushButton(Dialog)
        self.processButton.setGeometry(QtCore.QRect(530, 90, 89, 25))
        self.processButton.setObjectName("processButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Welcome to Zoo of PyZoo"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.label_4.setText(_translate("Dialog", "TextLabel"))
        self.inputModel.setItemText(0, _translate("Dialog", "Instance Segmentation"))
        self.inputModel.setItemText(1, _translate("Dialog", "Object Detection"))
        self.label_5.setText(_translate("Dialog", "Choose your application"))
        self.label_7.setText(_translate("Dialog", "Select your inputs"))
        self.chooseImage.setText(_translate("Dialog", "Choose image"))
        self.label_8.setText(_translate("Dialog", "Output"))
        self.processButton.setText(_translate("Dialog", "Process"))

