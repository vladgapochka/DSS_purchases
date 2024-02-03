from PyQt5 import QtWidgets, uic
import pymysql
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from connect import Connect

class Events(QtWidgets.QDialog):
    def __init__(self, var):
        super().__init__()
        uic.loadUi('events.ui', self)
        self.setWindowTitle('СППР для закупок ресторана "Сова"')
        self.var=var
        self.pushButton.clicked.connect(self.back)
        self.pushButton_3.clicked.connect(self.insert_customer)
        self.pushButton_2.clicked.connect(self.insert_events)
        self.pushButton_5.clicked.connect(self.delete_customer)
        self.pushButton_6.clicked.connect(self.delete_events)
        Connect().customer_table()
        Connect().event_table()
        self.tabl_customer()
        self.tabl_events()



    def tabl_customer(self):
        self.initTablecustomer()
        self.writeData_customer()

    def tabl_events(self):
        self.initTable_events()
        self.writeData_events()

    def back(self):
        self.var.show()
        self.close()
    def initTablecustomer(self):
        self.tableWidget.clear()
        columns = ['Id', 'Фамилия', 'Имя', 'Отчество', 'Телефон' ]
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(len(columns))
        self.tableWidget.setHorizontalHeaderLabels(columns)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnHidden(0, True)


    def initTable_events(self):
        self.tableWidget_2.clear()
        columns = ['Id', 'Фамилия', 'Имя', 'Отчество', 'Кол-во гостей','Дата','Адрес' ]
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(len(columns))
        self.tableWidget_2.setHorizontalHeaderLabels(columns)
        self.tableWidget_2.resizeColumnsToContents()
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.setColumnHidden(0, True)


    def insert_customer(self):

        surname = self.lineEdit_4.text()
        name = self.lineEdit_5.text()
        patronymic = self.lineEdit_6.text()
        phone = self.lineEdit.text()
        sql = "INSERT INTO customer (surname, name, patronymic, phone) VALUES (%s, %s, %s, %s)"
        val = (surname, name, patronymic, phone)
        Connect().InsertUpdateData(sql,val)
        self.tabl_customer()

    def delete_customer(self):
        sql = "DELETE FROM `customer` WHERE id_customer =(%s)"
        s = self.lineEdit_8.text()
        Connect().InsertUpdateData(sql, int(s))
        self.tabl_customer()

        # print(Connect().new_connect("SELECT * FROM `dishes` WHERE 1"))
    def delete_events(self):
        sql = "DELETE FROM `events` WHERE id_events =(%s)"
        s = self.lineEdit_9.text()
        sql_s = f"SELECT `id_events` FROM `events` WHERE `date`='{s}';"
        sql_s_id = Connect().new_connect(sql_s)
        Connect().InsertUpdateData(sql, sql_s_id[0][0])
        self.tabl_events()


    def insert_events(self):
        id_customer = self.lineEdit_7.text()
        sql_customer_id = f"SELECT `id_customer` FROM `customer` WHERE `phone`='{id_customer}'"
        sql_customer = Connect().new_connect(sql_customer_id)
        number_of_persons = self.lineEdit_3.text()
        address = self.lineEdit_2.text()
        date = self.dateTimeEdit.text()
        sql = "INSERT INTO events (id_customer, number_of_persons, date, address) VALUES (%s, %s, %s, %s)"
        val = (int(sql_customer[0][0]), number_of_persons, date, address)
        Connect().InsertUpdateData(sql,val)
        self.tabl_events()

    def writeData_customer(self):
        result=Connect().customer_table()
        rows=self.tableWidget.rowCount()
        for row_num, row in enumerate(result):
            self.tableWidget.insertRow(row_num + rows)
            for col_num, col in enumerate(row):
                self.tableWidget.setItem(row_num + rows, col_num, QtWidgets.QTableWidgetItem(str(col)))


    def writeData_events(self):
        result=Connect().event_table()
        rows=self.tableWidget_2.rowCount()
        for row_num, row in enumerate(result):
            self.tableWidget_2.insertRow(row_num + rows)
            for col_num, col in enumerate(row):
                self.tableWidget_2.setItem(row_num + rows, col_num, QtWidgets.QTableWidgetItem(str(col)))