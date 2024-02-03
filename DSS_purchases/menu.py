from PyQt5 import QtWidgets, uic
import pymysql
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from connect import Connect

class Menu(QtWidgets.QDialog):
    def __init__(self, var):
        super().__init__()
        uic.loadUi('menu.ui', self)
        self.setWindowTitle('СППР для закупок ресторана "Сова"')
        self.var=var
        self.pushButton_6.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.insert_dishes)
        self.pushButton_3.clicked.connect(self.delete_dishes)
        self.pushButton_4.clicked.connect(self.insert_product)
        self.pushButton_7.clicked.connect(self.delete_product)
        self.pushButton_5.clicked.connect(self.insert_option_dishes)
        # self.pushButton_3.clicked.connect(self.insert_customer)
        # self.pushButton_2.clicked.connect(self.insert_events)
        Connect().dishes_table()
        # Connect().event_table()
        self.tabl_dishes()
        self.tabl_product()
        self.tabl_option_dishes()
        self.pushButton_8.clicked.connect(self.tabl_option_dishes_vs)
        # self.tabl_events()
    def tabl_option_dishes_vs(self):
        self.initTable_option_dishes()
        self.writeData_option_dishes_vs()
    def tabl_option_dishes(self):
        self.initTable_option_dishes()
        self.writeData_option_dishes()

    def tabl_product(self):
        self.initTable_product()
        self.writeData_product()
    def tabl_dishes(self):
        self.initTable_dishes()
        self.writeData_dishes()
    def initTable_dishes(self):
        self.tableWidget.clear()
        columns = ['Id_блюда', 'Название', 'Выход', 'Цена' ]
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(len(columns))
        self.tableWidget.setHorizontalHeaderLabels(columns)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnHidden(0, True)


    def initTable_option_dishes(self):
        self.tableWidget_3.clear()
        columns = ['Блюда', 'Продукт', 'Кол-во', 'ед.изм' ]
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.setColumnCount(len(columns))
        self.tableWidget_3.setHorizontalHeaderLabels(columns)
        self.tableWidget_3.resizeColumnsToContents()
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)


    def initTable_product(self):
        self.tableWidget_2.clear()
        columns = ['Id', 'Продукт' ]
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(len(columns))
        self.tableWidget_2.setHorizontalHeaderLabels(columns)
        self.tableWidget_2.resizeColumnsToContents()
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.setColumnHidden(0, True)




    def back(self):
        self.var.show()
        self.close()

    def insert_dishes(self):
        name_dishes = self.lineEdit.text()
        output = self.lineEdit_2.text()
        price = self.lineEdit_3.text()

        sql = "INSERT INTO dishes (name_dishes, output, price) VALUES (%s, %s, %s)"
        val = (name_dishes, output, price)
        Connect().InsertUpdateData(sql,val)
        self.tabl_dishes()

    def insert_product(self):
        name_product = self.lineEdit_4.text()

        sql = "INSERT INTO product (name_product) VALUES (%s)"
        val = (name_product)
        Connect().InsertUpdateData(sql,val)
        self.tabl_product()


    def insert_option_dishes(self):
        id_dishes = self.lineEdit_5.text()
        id_product = self.lineEdit_6.text()
        sql_id = f"SELECT id_dishes FROM dishes WHERE name_dishes = '{id_dishes}'"
        id_d = Connect().new_connect(sql_id)
        print(id_d[0][0])
        sql_id_product = f"SELECT `id_product` FROM `product` WHERE `name_product` = '{id_product}'"
        sql_product = Connect().new_connect(sql_id_product)
        quantity = self.lineEdit_7.text()
        unit = self.comboBox.currentText()
        sql_ed_izm = f"SELECT `id_unit_of_measurement` FROM `unit_of_measurement` WHERE `unit_of_measurement` = '{unit}'"
        sql_ed_izm_id = Connect().new_connect(sql_ed_izm)
        #unit = int(1)
        # if unit == "Кг":
        #     unit = 1
        sql = "INSERT INTO composition_dish (id_dishes, id_product, number_of_product,id_unit_of_measurement) VALUES ( %s, %s,%s,%s)"
        val = (int(id_d[0][0]),int(sql_product[0][0]),float(quantity),int(sql_ed_izm_id[0][0]))
        Connect().InsertUpdateData(sql,val)
        self.tabl_option_dishes()

    def delete_product(self):
        sql = "DELETE FROM `product` WHERE id_product =(%s)"
        s = self.lineEdit_9.text()
        Connect().InsertUpdateData(sql, int(s))
        self.tabl_product()

    def delete_dishes(self):
        sql = "DELETE FROM `dishes` WHERE id_dishes =(%s)"
        s = self.lineEdit_8.text()
        Connect().InsertUpdateData(sql, int(s))
        self.tabl_dishes()


    def writeData_dishes(self):
        result=Connect().dishes_table()
        rows=self.tableWidget.rowCount()
        for row_num, row in enumerate(result):
            self.tableWidget.insertRow(row_num + rows)
            for col_num, col in enumerate(row):
                self.tableWidget.setItem(row_num + rows, col_num, QtWidgets.QTableWidgetItem(str(col)))

    def writeData_product(self):
        result=Connect().product_table()
        rows=self.tableWidget_2.rowCount()
        for row_num, row in enumerate(result):
            self.tableWidget_2.insertRow(row_num + rows)
            for col_num, col in enumerate(row):
                self.tableWidget_2.setItem(row_num + rows, col_num, QtWidgets.QTableWidgetItem(str(col)))

    def writeData_option_dishes(self):
        result=Connect().option_dishes_table()
        rows=self.tableWidget_3.rowCount()
        for row_num, row in enumerate(result):
            self.tableWidget_3.insertRow(row_num + rows)
            for col_num, col in enumerate(row):
                self.tableWidget_3.setItem(row_num + rows, col_num, QtWidgets.QTableWidgetItem(str(col)))

    def writeData_option_dishes_vs(self):
        name_dishes = self.lineEdit_10.text()
        result=Connect().option_dishes_table_vs(name_dishes)
        rows=self.tableWidget_3.rowCount()
        for row_num, row in enumerate(result):
            self.tableWidget_3.insertRow(row_num + rows)
            for col_num, col in enumerate(row):
                self.tableWidget_3.setItem(row_num + rows, col_num, QtWidgets.QTableWidgetItem(str(col)))