from PyQt5 import QtWidgets, uic
import pymysql
import sys
from menu import Menu
from events import Events
from provider_product import ProviderProduct
from order_formation import Order
from PyQt5.QtWidgets import QMessageBox
from connect import Connect
class MyWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.setWindowTitle('СППР для закупок ресторана "Сова"')

        self.events_button.clicked.connect(self.new_form)
        self.pushButton.clicked.connect(self.form_menu)
        self.push_button_2.clicked.connect(self.form_provider_product)
        self.push_button_3.clicked.connect(self.form_order_formation)


        print(Connect().new_connect("SELECT * FROM `dishes` WHERE 1"))


    def new_form(self):
        event=Events(self)
        self.hide()
        event.exec_()
        event.show()


    def form_menu(self):
        menu=Menu(self)
        self.hide()
        menu.exec_()
        menu.show()

    def form_provider_product(self):
        provider_product=ProviderProduct(self)
        self.hide()
        provider_product.exec_()
        provider_product.show()

    def form_order_formation(self):
        order_formation=Order(self)
        self.hide()
        order_formation.exec_()
        order_formation.show()





if __name__ == '__main__':

    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
