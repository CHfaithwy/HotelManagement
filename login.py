# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'

# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from pymysql import *
import admin
import customer
class guanli(QtWidgets.QMainWindow,admin.Ui_Form):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        admin.Ui_Form.__init__(self)
        self.setupUi(self)


class guke(QtWidgets.QMainWindow, customer.Ui_Form):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        customer.Ui_Form.__init__(self)
        self.setupUi(self)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(395, 278)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(140, 40, 160, 181))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 61, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 50, 61, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 0, 331, 31))
        self.label_4.setObjectName("label_4")
        self.radioButton.toggled.connect(lambda : self.get(self.radioButton))
        self.radioButton_2.toggled.connect(lambda : self.get(self.radioButton_2))
        self.pushButton.clicked.connect(lambda : self.login(self.txt))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def login(self,bnt):

        print(bnt)
        if bnt == '管理员' :
            if self.lineEdit_2.text() != 'root' or self.lineEdit.text() != 'root':
                QMessageBox.warning(self, "警告信息", "密码或账号不正确", QMessageBox.Yes, QMessageBox.Yes)
            Ui_Form.guan_win.show()
        else :
            cur.execute('select * from customer where phone={};'.format(self.lineEdit_2.text()))
            last = cur.fetchone()
            (phone,pwd) = last[2],last[5]
            if pwd != self.lineEdit.text():
                QMessageBox.information(self.pushButton, "提示", "密码或账号不正确")
                return -1
            Ui_Form.customer_win.show()
            print(last)
            Ui_Form.customer_win.lineEdit.setText(last[0])
            Ui_Form.customer_win.lineEdit_6.setText(last[1])
            Ui_Form.customer_win.lineEdit_2.setText(last[2])
            Ui_Form.customer_win.lineEdit_3.setText(last[3])
            Ui_Form.customer_win.lineEdit_4.setText(last[4])
            Ui_Form.customer_win.lineEdit_5.setText(last[5])
        Main.close()
    def get(self,btn):
        if btn.text() == '管理员' :
            self.txt = '管理员'
        else :
            self.txt = '用户'
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "酒店登录"))
        self.pushButton.setText(_translate("Form", "登录"))
        self.radioButton.setText(_translate("Form", "管理员"))
        self.radioButton_2.setText(_translate("Form", "用户"))
        self.label_2.setText(_translate("Form", "密码 ："))
        self.label_3.setText(_translate("Form", "账号："))
        self.label_4.setText(_translate("Form", "                  欢迎使用酒店管理系统"))


db = connect(
    host='localhost', port=3306, user='root', password='', database='pyconnect'
)

cur = db.cursor()
app = QApplication(sys.argv)
Main = QMainWindow()
Ui_Form.customer_win = guke()
Ui_Form.guan_win = guanli()
ui = Ui_Form()
ui.setupUi(Main)
Main.show()
sys.exit(app.exec_())