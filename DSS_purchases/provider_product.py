from PyQt5 import QtWidgets, uic
import pymysql
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from connect import Connect


class ProviderProduct(QtWidgets.QDialog):
    def __init__(self, var):
        super().__init__()
        uic.loadUi('option_product.ui', self)
        self.setWindowTitle('СППР для закупок ресторана "Сова"')
        self.var = var
        self.pushButton_3.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.insert_provider)
        self.pushButton_2.clicked.connect(self.insert_contaner)
        self.pushButton_4.clicked.connect(self.insert_var_provider)
        self.tabl_provider()
        self.tabl_product()
        self.tabl_contaner()
        self.tabl_var_product()


    def tabl_product(self):
        self.initTable_product()
        self.writeData_product()

    def tabl_var_product(self):
        self.initTable_var_provider()
        self.writeData_var_product()


    def tabl_contaner(self):
        self.initTable_contaner()
        self.writeData_contaner()



    def back(self):
        self.var.show()
        self.close()

    def tabl_provider(self):
        self.initTable_provider()
        self.writeData_provider()


    def insert_provider(self):
        name_provider = self.lineEdit.text()
        # output = self.lineEdit_2.text()
        # price = self.lineEdit_3.text()

        sql = "INSERT INTO manufacturer (name_manufacturer) VALUES (%s)"
        val = (name_provider)
        Connect().InsertUpdateData(sql,val)
        self.tabl_provider()

    def initTable_provider(self):
        self.tableWidget.clear()
        columns = ['Id_Производителя', 'Наименование производителя']
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(len(columns))
        self.tableWidget.setHorizontalHeaderLabels(columns)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnHidden(0, True)

    def writeData_provider(self):
        result=Connect().provider_table()
        rows=self.tableWidget.rowCount()
        for row_num, row in enumerate(result):
            self.tableWidget.insertRow(row_num + rows)
            for col_num, col in enumerate(row):
                self.tableWidget.setItem(row_num + rows, col_num, QtWidgets.QTableWidgetItem(str(col)))

    def initTable_product(self):
        self.tableWidget_2.clear()
        columns = ['Id', 'Продукт' ]
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(len(columns))
        self.tableWidget_2.setHorizontalHeaderLabels(columns)
        self.tableWidget_2.resizeColumnsToContents()
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.setColumnHidden(0, True)

    def writeData_product(self):
        result=Connect().product_table()
        rows=self.tableWidget_2.rowCount()
        for row_num, row in enumerate(result):
            self.tableWidget_2.insertRow(row_num + rows)
            for col_num, col in enumerate(row):
                self.tableWidget_2.setItem(row_num + rows, col_num, QtWidgets.QTableWidgetItem(str(col)))

    def insert_contaner(self):
        contaner = self.lineEdit_2.text()
        # output = self.lineEdit_2.text()
        # price = self.lineEdit_3.text()

        sql = "INSERT INTO container (volume) VALUES (%s)"
        val = (contaner)
        Connect().InsertUpdateData(sql,val)
        self.tabl_contaner()

    def initTable_contaner(self):
        self.tableWidget_3.clear()
        columns = ['Id', 'Объем' ]
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.setColumnCount(len(columns))
        self.tableWidget_3.setHorizontalHeaderLabels(columns)
        self.tableWidget_3.resizeColumnsToContents()
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.setColumnHidden(0, True)


    def writeData_contaner(self):
        result=Connect().table_contaner()
        rows=self.tableWidget_3.rowCount()
        for row_num, row in enumerate(result):
            self.tableWidget_3.insertRow(row_num + rows)
            for col_num, col in enumerate(row):
                self.tableWidget_3.setItem(row_num + rows, col_num, QtWidgets.QTableWidgetItem(str(col)))


    def insert_var_provider(self):
        id_product = self.lineEdit_3.text()
        tara = self.lineEdit_4.text()
        provider = self.lineEdit_5.text()
        quenty = self.lineEdit_6.text()
        price = self.lineEdit_7.text()
        ed_izm = self.comboBox.currentText()
        #ed_izm = 1
        # if ed_izm == "Кг":
        #     ed_izm = 1
        sql_ed_izm = f"SELECT `id_unit_of_measurement` FROM `unit_of_measurement` WHERE `unit_of_measurement` = '{ed_izm}'"
        sql_ed_izm_id = Connect().new_connect(sql_ed_izm)
        print(sql_ed_izm_id[0][0])
        sql_id_product = f"SELECT `id_product` FROM `product` WHERE `name_product` = '{id_product}'"
        sql_product = Connect().new_connect(sql_id_product)
        print(sql_product[0][0])
        sql_tara = f"SELECT `id_container` FROM `container` WHERE `volume` = '{tara}'"
        sql_tara_id = Connect().new_connect(sql_tara)
        print(sql_tara_id[0][0])
        sql_provider =f"SELECT `id_manufacturer` FROM `manufacturer` WHERE `name_manufacturer` = '{provider}'"
        sql_provider_id = Connect().new_connect(sql_provider)
        print(sql_provider_id[0][0])
        sql = "INSERT INTO product_options (id_product, id_container, id_unit_of_measurement, id_manufacturer, quantity, price) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (int(sql_product[0][0]),int(sql_tara_id[0][0]),int(sql_ed_izm_id[0][0]),int(sql_provider_id[0][0]),float(quenty),float(price))
        Connect().InsertUpdateData(sql,val)
        self.tabl_var_product()

    def initTable_var_provider(self):
        self.tableWidget_4.clear()
        columns = ['Id', 'Продукт','Количество', 'Тара','Ед.из','Поставщик','Цена' ]
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.setColumnCount(len(columns))
        self.tableWidget_4.setHorizontalHeaderLabels(columns)
        self.tableWidget_4.resizeColumnsToContents()
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_4.setColumnHidden(0, True)

    def writeData_var_product(self):
        result=Connect().table_var_product()
        rows=self.tableWidget_4.rowCount()
        for row_num, row in enumerate(result):
            self.tableWidget_4.insertRow(row_num + rows)
            for col_num, col in enumerate(row):
                self.tableWidget_4.setItem(row_num + rows, col_num, QtWidgets.QTableWidgetItem(str(col)))