from aifc import Error

import pymysql

class Connect:
    def connect(self):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="owl_restaurant"
        )
        return connection
    def InsertUpdateData(self, query,ex):
        try:
            # Создайте курсор для выполнения операций с базой данных
            connection = self.connect()
            cursor = connection.cursor()
            # SQL-запрос для создания новой таблицы

            # Выполнение команды: это создает новую таблицу
            cursor.execute(query,ex)
            connection.commit()
            print("Запись успешно добавлена")
        except(Exception, Error) as error:
            print("Ошибка при добавлении", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с БД закрыто")
    def new_connect(self,select):

        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(select)
            results = cursor.fetchall()
            return results
        except(Exception, Error) as error:
            print("Ошибка при работе с БД", error)
        finally:
            if conn:
                cursor.close()
                conn.close()

    def customer_table(self,):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM `customer` WHERE 1''')

        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    def event_table(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('''SELECT e.id_events,  c.surname,c.name, c.patronymic, e.number_of_persons, e.date, e.address FROM events e JOIN customer c ON e.id_customer = c.id_customer;''')

        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    def dishes_table(self,):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM `dishes` WHERE 1;''')

        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    def provider_table(self,):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM `manufacturer`;''')

        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    def product_table(self,):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM `product` WHERE 1''')

        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    def option_dishes_table(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('''SELECT d.name_dishes, p.name_product, cd.number_of_product, u.unit_of_measurement
                            FROM dishes d
                            JOIN composition_dish cd ON d.id_dishes = cd.id_dishes
                            JOIN product p ON cd.id_product = p.id_product
                            JOIN unit_of_measurement u ON cd.id_unit_of_measurement = u.id_unit_of_measurement;''')

        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    def option_dishes_table_vs(self,name_dishes):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(f'''SELECT d.name_dishes, p.name_product, cd.number_of_product, u.unit_of_measurement FROM dishes d 
        JOIN composition_dish cd ON d.id_dishes = cd.id_dishes JOIN product p ON cd.id_product = p.id_product 
        JOIN unit_of_measurement u ON cd.id_unit_of_measurement = u.id_unit_of_measurement WHERE d.name_dishes='{name_dishes}';''')

        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    def table_contaner(self,):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM `container`;''')

        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    def table_var_product(self,):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('''SELECT po.id_product_options, p.name_product, po.quantity, c.volume, uom.unit_of_measurement, m.name_manufacturer, po.price FROM product_options po JOIN product p ON po.id_product = p.id_product JOIN container c ON po.id_container = c.id_container JOIN unit_of_measurement uom ON po.id_unit_of_measurement = uom.id_unit_of_measurement JOIN manufacturer m ON po.id_manufacturer = m.id_manufacturer;''')

        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    def table_order(self,):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('''SELECT events.date, dishes.name_dishes, events_in_dishes.number_of_servings FROM events JOIN events_in_dishes ON events.id_events = events_in_dishes.id_events JOIN dishes ON events_in_dishes.id_dishes = dishes.id_dishes;''')

        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    def table_order_sort(self,id_events):

        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(f'''SELECT events.date, dishes.name_dishes, events_in_dishes.number_of_servings FROM events JOIN events_in_dishes ON events.id_events = events_in_dishes.id_events JOIN dishes ON events_in_dishes.id_dishes = dishes.id_dishes WHERE events.id_events = {id_events};''')

        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    def table_product_sort(self,id_events):

        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(f'''SELECT events.date, product.name_product, ROUND(SUM(composition_dish.number_of_product * events_in_dishes.number_of_servings), 2) as total_number,
         um.unit_of_measurement FROM events 
         JOIN events_in_dishes ON events.id_events = events_in_dishes.id_events 
         JOIN composition_dish ON events_in_dishes.id_dishes = composition_dish.id_dishes JOIN product ON composition_dish.id_product = product.id_product 
         JOIN unit_of_measurement AS um ON composition_dish.id_unit_of_measurement = um.id_unit_of_measurement 
         WHERE events.id_events = {id_events} GROUP BY events.date, product.name_product, um.unit_of_measurement;''')

        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    def table_product_variant(self,id_events):

        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(f'''SELECT po.id_product, p.name_product,po.quantity,um.unit_of_measurement, c.volume, po.id_container, po.price, m.name_manufacturer
FROM product_options po
JOIN product p ON po.id_product = p.id_product
JOIN container c ON po.id_container = c.id_container
JOIN manufacturer m ON po.id_manufacturer = m.id_manufacturer
JOIN unit_of_measurement AS um ON po.id_unit_of_measurement = um.id_unit_of_measurement
WHERE po.id_product IN (SELECT DISTINCT composition_dish.id_product FROM events
                         JOIN events_in_dishes ON events.id_events = events_in_dishes.id_events
                         JOIN composition_dish ON events_in_dishes.id_dishes = composition_dish.id_dishes
                         WHERE events.id_events = {id_events})
AND po.id_unit_of_measurement IN (SELECT DISTINCT composition_dish.id_unit_of_measurement FROM events
                         JOIN events_in_dishes ON events.id_events = events_in_dishes.id_events
                         JOIN composition_dish ON events_in_dishes.id_dishes = composition_dish.id_dishes
                         WHERE events.id_events = {id_events})
ORDER BY po.id_product, po.id_container;
''')

        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result