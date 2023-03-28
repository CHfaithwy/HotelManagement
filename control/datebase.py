# 开发人员 ：王阳
# 开发时间 ：2022/6/18 20:55
from PyQt5.QtWidgets import QMessageBox
from pymysql import *

db = connect(
    host = 'localhost' ,port = 3306 ,user = 'root' ,password = 'wangyang5721314' ,database = 'pyconnect'
)
cur = db.cursor()

def login():
    #(zh,pwd) = a.linelineEdit_2.text,a.lineEdit.text
    print(1)


