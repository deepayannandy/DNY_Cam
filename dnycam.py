# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\DNYIndai\Desktop\dnycam.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
import time
import soc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import *

class Ui_DNY_Cam(object):
    def setupUi(self, DNY_Cam):
        DNY_Cam.setObjectName("DNY_Cam")
        DNY_Cam.resize(770, 501)
        self.centralwidget = QtWidgets.QWidget(DNY_Cam)
        self.centralwidget.setObjectName("centralwidget")
        self.pan = QtWidgets.QSlider(self.centralwidget)
        self.pan.setGeometry(QtCore.QRect(20, 480, 661, 19))
        self.pan.setMinimum(150)
        self.pan.setMaximum(500)
        self.pan.setSingleStep(15)
        self.pan.setSliderPosition(375)
        self.pan.setOrientation(QtCore.Qt.Horizontal)
        self.pan.setObjectName("pan")
        self.tilt = QtWidgets.QSlider(self.centralwidget)
        self.tilt.setGeometry(QtCore.QRect(740, 90, 20, 361))
        self.tilt.setMinimum(150)
        self.tilt.setMaximum(500)
        self.tilt.setSingleStep(15)
        self.tilt.setSliderPosition(375)
        self.tilt.setOrientation(QtCore.Qt.Vertical)
        self.tilt.setObjectName("tilt")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(700, 460, 51, 31))
        self.reset.setObjectName("reset")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 761, 51))
        self.groupBox.setObjectName("groupBox")
        self.ip = QtWidgets.QLabel(self.groupBox)
        self.ip.setGeometry(QtCore.QRect(10, 20, 61, 21))
        self.ip.setObjectName("ip")
        self.ipd = QtWidgets.QLineEdit(self.groupBox)
        self.ipd.setGeometry(QtCore.QRect(90, 10, 181, 31))
        self.ipd.setObjectName("ipd")
        self.port = QtWidgets.QLabel(self.groupBox)
        self.port.setGeometry(QtCore.QRect(280, 20, 51, 21))
        self.port.setObjectName("port")
        self.portd = QtWidgets.QLineEdit(self.groupBox)
        self.portd.setGeometry(QtCore.QRect(330, 10, 181, 31))
        self.portd.setObjectName("portd")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(560, 10, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.webView = QWebEngineView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(10, 60, 721, 391))
        self.webView.load(QUrl("http://www.dnyindia.com"))
        self.webView.show()
        DNY_Cam.setCentralWidget(self.centralwidget)
        self.retranslateUi(DNY_Cam)
        QtCore.QMetaObject.connectSlotsByName(DNY_Cam)
        self.pushButton.clicked.connect(self.connect)
        self.pan.valueChanged[int].connect(self.changeValuePan)
        self.tilt.valueChanged[int].connect(self.changeValueTilt)
        self.reset.clicked.connect(self.resetf)

    def retranslateUi(self, DNY_Cam):
        _translate = QtCore.QCoreApplication.translate
        DNY_Cam.setWindowTitle(_translate("DNY_Cam", "DNY_Cam"))
        self.reset.setText(_translate("DNY_Cam", "Reset"))
        self.groupBox.setTitle(_translate("DNY_Cam", "Network Data"))
        self.ip.setText(_translate("DNY_Cam", "Ip Address"))
        self.port.setText(_translate("DNY_Cam", "Port"))
        self.pushButton.setText(_translate("DNY_Cam", "Connect"))

    def connect(self):
        ipv=self.ipd.text()
        portv=self.portd.text()
        print("Connecting to "+ipv+":"+portv)
        self.webView.load(QUrl("http://"+ipv+":"+portv))
        self.webView.show()
        soc.connectw(ipv)
        
    def changeValueTilt(self, value):
        print(value)
        time.sleep(.01)
        soc.senddata('t'+str(value))
    def changeValuePan(self, value):
        print(value)
        time.sleep(.01)
        soc.senddata('p'+str(value))
    def resetf(self):
        print("re")
        soc.senddata('re')
        self.pan.setSliderPosition(375)
        self.tilt.setSliderPosition(375)
        
        
                          
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DNY_Cam = QtWidgets.QMainWindow()
    ui = Ui_DNY_Cam()
    ui.setupUi(DNY_Cam)
    DNY_Cam.show()
    sys.exit(app.exec_())

