from PyQt5 import QtWidgets, uic
import pymysql
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QComboBox
from connect import Connect
import pandas as pd
from pulp import *
class Order(QtWidgets.QDialog):
    def __init__(self, var):
        super().__init__()
        uic.loadUi('order_formation.ui', self)
        self.setWindowTitle('СППР для закупок ресторана "Сова"')
        self.var=var
        self.pushButton.clicked.connect(self.back)
        self.pushButton_2.clicked.connect(self.insert_order)
        self.pushButton_3.clicked.connect(self.tabl_order_sort)
        self.pushButton_4.clicked.connect(self.tabl_product_sort)
        self.pushButton_4.clicked.connect(self.tabl_product_variant)
        self.pushButton_4.clicked.connect(self.wwww)
        self.pushButton_4.clicked.connect(self.fillTable)
        # self.pushButton_4.clicked.connect(self.zzzz)
        self.combo_events()
        self.combo_dishes()
        self.tabl_order()
        self.combo_events_sort()
    # def tabl_product_optimize(self):
    #     self.initTable_product_optimize()
    #     self.writeData_product_optimize()
    def tabl_product_variant(self):
        self.initTable_product_variant()
        self.writeData_product_variant()
    def tabl_product_sort(self):
        self.initTable_product_sort()
        self.writeData_product_sort()


    def tabl_order_sort(self):
        self.initTable_order_sort()
        self.writeData_oreder_sort()
    def tabl_order(self):
        self.initTable_order()
        self.writeData_oreder()
    def back(self):
        self.var.show()
        self.close()


    def combo_events_sort(self):
        #combo_box = self.comboBox.currentText()
        sql_combo_events = f"SELECT `date` FROM `events`"
        sql_combo_events_data = Connect().new_connect(sql_combo_events)
        # print(sql_combo_events_data)
        my_tuple = sql_combo_events_data
        my_list = [x[0] for x in my_tuple]
        my_str = ','.join(my_list)
        # print(my_str)
        my_list = my_str.split(',')
        for i in my_list:
            self.comboBox_3.addItem(i)
            self.comboBox_4.addItem(i)
    def combo_events(self):
        #combo_box = self.comboBox.currentText()
        sql_combo_events = f"SELECT `date` FROM `events`"
        sql_combo_events_data = Connect().new_connect(sql_combo_events)
        # print(sql_combo_events_data)
        my_tuple = sql_combo_events_data
        my_list = [x[0] for x in my_tuple]
        my_str = ','.join(my_list)
        # print(my_str)
        my_list = my_str.split(',')
        for i in my_list:
            self.comboBox.addItem(i)

    def combo_dishes(self):
        #combo_box = self.comboBox.currentText()
        sql_combo_events = f"SELECT `name_dishes` FROM `dishes`;"
        sql_combo_events_data = Connect().new_connect(sql_combo_events)
        # print(sql_combo_events_data)
        my_tuple = sql_combo_events_data
        my_list = [x[0] for x in my_tuple]
        my_str = ','.join(my_list)
        # print(my_str)
        my_list = my_str.split(',')
        for i in my_list:
            self.comboBox_2.addItem(i)

    def insert_order(self):
        evwnts = self.comboBox.currentText()

        name_dishes = self.comboBox_2.currentText()

        quality = self.lineEdit.text()

        sql_id = f"SELECT id_dishes FROM dishes WHERE name_dishes = '{name_dishes}'"
        id_d = Connect().new_connect(sql_id)

        sql_events = f"SELECT `id_events` FROM `events` WHERE `date`='{evwnts}'"
        id_events = Connect().new_connect(sql_events)


        sql = "INSERT INTO events_in_dishes (id_events, id_dishes, number_of_servings) VALUES (%s, %s, %s)"
        val = (int(id_events[0][0]), int(id_d[0][0]), int(quality))
        Connect().InsertUpdateData(sql,val)
        self.tabl_order()
    def initTable_order_sort(self):
        self.tableWidget.clear()
        columns = ['Дата мероприятия', 'Блюдо', 'Количество' ]
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(len(columns))
        self.tableWidget.setHorizontalHeaderLabels(columns)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnHidden(0, True)
    def initTable_order(self):
        self.tableWidget.clear()
        columns = ['Дата мероприятия', 'Блюдо', 'Количество' ]
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(len(columns))
        self.tableWidget.setHorizontalHeaderLabels(columns)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnHidden(0, True)

    def writeData_oreder(self):

        result=Connect().table_order()
        rows=self.tableWidget.rowCount()
        for row_num, row in enumerate(result):
            self.tableWidget.insertRow(row_num + rows)
            for col_num, col in enumerate(row):
                self.tableWidget.setItem(row_num + rows, col_num, QtWidgets.QTableWidgetItem(str(col)))

    def writeData_oreder_sort(self):
        evwnts = self.comboBox_3.currentText()
        sql_events = f"SELECT `id_events` FROM `events` WHERE `date`='{evwnts}'"
        id_events = Connect().new_connect(sql_events)
        result=Connect().table_order_sort(int(id_events[0][0]))
        rows=self.tableWidget.rowCount()
        for row_num, row in enumerate(result):
            self.tableWidget.insertRow(row_num + rows)
            for col_num, col in enumerate(row):
                self.tableWidget.setItem(row_num + rows, col_num, QtWidgets.QTableWidgetItem(str(col)))

    def writeData_product_sort(self):
        evwnts = self.comboBox_4.currentText()
        sql_events = f"SELECT `id_events` FROM `events` WHERE `date`='{evwnts}'"
        id_events = Connect().new_connect(sql_events)
        result=Connect().table_product_sort(int(id_events[0][0]))
        rows=self.tableWidget_2.rowCount()
        for row_num, row in enumerate(result):
            self.tableWidget_2.insertRow(row_num + rows)
            for col_num, col in enumerate(row):
                self.tableWidget_2.setItem(row_num + rows, col_num, QtWidgets.QTableWidgetItem(str(col)))

    def initTable_product_sort(self):
        self.tableWidget_2.clear()
        columns = ['Дата мероприятия', 'Продукт', 'Количество','Ед.Из' ]
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(len(columns))
        self.tableWidget_2.setHorizontalHeaderLabels(columns)
        self.tableWidget_2.resizeColumnsToContents()
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.setColumnHidden(0, True)

    def writeData_product_variant(self):
        evwnts = self.comboBox_4.currentText()
        sql_events = f"SELECT `id_events` FROM `events` WHERE `date`='{evwnts}'"
        id_events = Connect().new_connect(sql_events)
        result=Connect().table_product_variant(int(id_events[0][0]))
        rows=self.tableWidget_3.rowCount()
        for row_num, row in enumerate(result):
            self.tableWidget_3.insertRow(row_num + rows)
            for col_num, col in enumerate(row):
                self.tableWidget_3.setItem(row_num + rows, col_num, QtWidgets.QTableWidgetItem(str(col)))

    def fillTable(self):
        # Получаем список значений из функции www()
        data = self.wwww()

        # Очищаем таблицу перед заполнением
        self.tableWidget_4.clear()

        # Задаем заголовки столбцов
        headers = ['Id_продукта', 'Продукт', 'Id_Тары', 'Тара', 'Ед.Из','Объем', 'Цена', 'Поставщик', 'Купить']
        self.tableWidget_4.setColumnCount(len(headers))
        self.tableWidget_4.setHorizontalHeaderLabels(headers)

        # Заполняем таблицу данными из списка
        for i, row in enumerate(data):
            self.tableWidget_4.insertRow(i)
            for j, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget_4.setItem(i, j, item)

        # Размеры таблицы подстраиваются под содержимое
        # self.tableWidget_4.resizeColumnsToContents()
        self.tableWidget_4.setColumnHidden(0, True)
        self.tableWidget_4.setColumnHidden(2, True)

    def initTable_product_variant(self):
        self.tableWidget_3.clear()
        columns = ['Id_продукта', 'Продукт','Объем','Ед.Из' , 'Тара', 'Id_Тары', 'Цена','Поставщик' ]
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.setColumnCount(len(columns))
        self.tableWidget_3.setHorizontalHeaderLabels(columns)
        self.tableWidget_3.resizeColumnsToContents()
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.setColumnHidden(0, True)
        self.tableWidget_3.setColumnHidden(5, True)
    def wwww(self):
        id_events = self.comboBox_4.currentText()
        sql_events = f"SELECT `id_events` FROM `events` WHERE `date`='{id_events}'"
        id_events_sql = Connect().new_connect(sql_events)
        products_sql = (f"""SELECT po.id_product, p.name_product, po.id_container, c.volume, um.unit_of_measurement, po.quantity, po.price, m.name_manufacturer
                     FROM product_options po
                     JOIN product p ON po.id_product = p.id_product
                     JOIN container c ON po.id_container = c.id_container
                  JOIN manufacturer m ON po.id_manufacturer = m.id_manufacturer
                     JOIN unit_of_measurement AS um ON po.id_unit_of_measurement = um.id_unit_of_measurement
                    WHERE po.id_product IN (SELECT DISTINCT composition_dish.id_product FROM events
                                             JOIN events_in_dishes ON events.id_events = events_in_dishes.id_events
                                             JOIN composition_dish ON events_in_dishes.id_dishes = composition_dish.id_dishes
                                             WHERE events.id_events = {id_events_sql[0][0]})
                     AND po.id_unit_of_measurement IN (SELECT DISTINCT composition_dish.id_unit_of_measurement FROM events
                                             JOIN events_in_dishes ON events.id_events = events_in_dishes.id_events
                                             JOIN composition_dish ON events_in_dishes.id_dishes = composition_dish.id_dishes
                                             WHERE events.id_events = {id_events_sql[0][0]})
                     ORDER BY po.id_product, po.id_container;""")
        products = Connect().new_connect(products_sql)
        products = list(products)
        print(products)
        quantities = (f"""SELECT composition_dish.id_product,
       ROUND(SUM(composition_dish.number_of_product * events_in_dishes.number_of_servings), 2) AS total_quantity
FROM events
JOIN events_in_dishes ON events.id_events = events_in_dishes.id_events
JOIN composition_dish ON events_in_dishes.id_dishes = composition_dish.id_dishes
WHERE events.id_events = {id_events_sql[0][0]}
GROUP BY composition_dish.id_product;
""")
        required_products = Connect().new_connect(quantities)
        required_products = list(required_products)
        print(required_products)
        # Инициализация модели линейного программирования
        model = LpProblem("Purchase Optimization", LpMinimize)

        # Создание переменных решения
        product_vars = LpVariable.dicts("product", products, lowBound=0, cat='Continuous')


        # Создание функции стоимости (целевой функции)
        model += lpSum([product_vars[p] * p[6] for p in products])

        # Создание ограничений по необходимым количествам
        for p in required_products:
            model += lpSum([product_vars[pd] for pd in products if pd[0] == p[0]]) >= p[1]

        # Решение модели
        model.solve()

        # Проверка результата
        print("Статус решения:", LpStatus[model.status])

        # Создание списка для хранения результатов
        result = []

        # Решение модели
        model.solve()

        # Проверка результата
        print("Статус решения:", LpStatus[model.status])

        # Вывод результатов
        if model.status == LpStatusOptimal:
            result = []
            for p in products:
                if product_vars[p].value() > 0:
                    quantity = max(round(product_vars[p].value() / p[5]), 1)
                    result.append(p + (quantity,))
            for r in result:
                print(r)
        else:
            print("Решение не найдено")
        print("Вот наш результат")
        print(result)
        return result

    # def aaae(self):
    #
    #     id_events = self.comboBox_4.currentText()
    #     sql_events = f"SELECT `id_events` FROM `events` WHERE `date`='{id_events}'"
    #     id_events_sql = Connect().new_connect(sql_events)
    #     # Считываем данные из БД
    #     products_sql = (f"""SELECT po.id_product, p.name_product, po.id_container, c.volume, um.unit_of_measurement, po.quantity, po.price, m.name_manufacturer
    #         FROM product_options po
    #         JOIN product p ON po.id_product = p.id_product
    #         JOIN container c ON po.id_container = c.id_container
    #       JOIN manufacturer m ON po.id_manufacturer = m.id_manufacturer
    #         JOIN unit_of_measurement AS um ON po.id_unit_of_measurement = um.id_unit_of_measurement
    #         WHERE po.id_product IN (SELECT DISTINCT composition_dish.id_product FROM events
    #                                 JOIN events_in_dishes ON events.id_events = events_in_dishes.id_events
    #                                 JOIN composition_dish ON events_in_dishes.id_dishes = composition_dish.id_dishes
    #                                 WHERE events.id_events = {id_events_sql})
    #         AND po.id_unit_of_measurement IN (SELECT DISTINCT composition_dish.id_unit_of_measurement FROM events
    #                                 JOIN events_in_dishes ON events.id_events = events_in_dishes.id_events
    #                                 JOIN composition_dish ON events_in_dishes.id_dishes = composition_dish.id_dishes
    #                                 WHERE events.id_events = {id_events_sql})
    #         ORDER BY po.id_product, po.id_container;""")
    #     products = Connect().new_connect(products_sql)
    #
    #     # Получаем количество продуктов для закупки
    #     quantities = (f"""SELECT composition_dish.id_product,
    #      SUM(composition_dish.number_of_product * events_in_dishes.number_of_servings) AS total_quantity FROM events
    #      JOIN events_in_dishes ON events.id_events = events_in_dishes.id_events
    #      JOIN composition_dish ON events_in_dishes.id_dishes = composition_dish.id_dishes
    #      WHERE events.id_events = {id_events_sql} GROUP BY composition_dish.id_product;""")
    #     product_quantities = Connect().new_connect(quantities)
    #     # Создаем оптимизационную задачу
    #     prob = LpProblem("Product Purchase Problem", LpMinimize)
    #
    #     # Создаем переменные решения - количество единиц каждого продукта, которые необходимо закупить
    #     product_vars = LpVariable.dicts("Product", products.index, lowBound=0, cat="Integer")
    #
    #     # Определяем целевую функцию - минимизация общей стоимости закупок
    #     prob += lpSum([product_vars[i] * products.loc[i, "price"] for i in products.index]), "Total Cost"
    #
    #     # Ограничения на количество закупаемых продуктов
    #     for i in product_quantities.index:
    #         prob += lpSum([product_vars[j] for j in
    #                        products[products["id_product"] == product_quantities.loc[i, "id_product"]].index]) >= \
    #                 product_quantities.loc[i, "total_quantity"], \
    #             f"Quantity of product {product_quantities.loc[i, 'id_product']}"
    #
    #     # Решаем задачу
    #     prob.solve()
    #
    #     # Выводим результаты
    #     print("Status:", LpStatus[prob.status])
    #     for v in prob.variables():
    #         if v.varValue > 0:
    #             print(v.name, "=", v.varValue)
    #     print("Total Cost =", value(prob.objective))



