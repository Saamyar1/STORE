# This file will contains classes related to product management, such as Product and Inventory, which handle product information, stock, and out-of-stock notifications.

# Product class
# import what needed from other files
from core import *


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
            
        def __str__(self):
            return self.name
    
        def get_name(self):
            return self.name
    
        def get_price(self):
            return self.price
    
        def get_stock(self):
            return self.stock
    
        def set_stock(self, stock):
            self.stock = stock
    
        def add_stock(self, stock):
            self.stock += stock
    
        def remove_stock(self, stock):
            self.stock -= stock

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.get_name()] = product

    def get_product(self, name):
        return self.products[name]
    
    def get_all_products(self):
        return self.products
    
    def remove_product(self, name):
        del self.products[name]

    def get_product_names(self):
        return self.products.keys()
    
    def get_product_prices(self):
        return self.products.values()
    
    def get_product_stocks(self):
        return self.products.values()
    
    def get_product_stock(self, name):
        return self.products[name].get_stock()
    
    def set_product_stock(self, name, stock):
        self.products[name].set_stock(stock)
        
    def add_product_stock(self, name, stock):
        self.products[name].add_stock(stock)

    def remove_product_stock(self, name, stock):
        self.products[name].remove_stock(stock)

    def get_out_of_stock(self):
        out_of_stock = []
        for product in self.products.values():
            if product.get_stock() == 0:
                out_of_stock.append(product)
        return out_of_stock
    
    def get_low_stock(self):
        low_stock = []
        for product in self.products.values():
            if product.get_stock() <= 5:
                low_stock.append(product)
        return low_stock
    
    def get_all_stock(self):
        all_stock = []
        for product in self.products.values():
            all_stock.append(product)
        return all_stock
    
    def get_all_stock_names(self):
        all_stock_names = []
        for product in self.products.values():
            all_stock_names.append(product.get_name())
        return all_stock_names
    
    def get_all_stock_prices(self):
        all_stock_prices = []
        for product in self.products.values():
            all_stock_prices.append(product.get_price())
        return all_stock_prices
    
    def get_all_stock_stocks(self):
        all_stock_stocks = []
        for product in self.products.values():
            all_stock_stocks.append(product.get_stock())
        return all_stock_stocks
    
    def get_all_stock_stock(self, name):
        return self.products[name].get_stock()
    
    def set_all_stock_stock(self, name, stock):
        self.products[name].set_stock(stock)

    def add_all_stock_stock(self, name, stock):
        self.products[name].add_stock(stock)

    def remove_all_stock_stock(self, name, stock):
        self.products[name].remove_stock(stock)
        
    def get_all_out_of_stock(self):
        out_of_stock = []
        for product in self.products.values():
            if product.get_stock() == 0:
                out_of_stock.append(product)
        return out_of_stock
    
    def get_all_low_stock(self):
        low_stock = []
        for product in self.products.values():
            if product.get_stock() <= 5:
                low_stock.append(product)
        return low_stock
    
    def get_all_all_stock(self):
        all_stock = []
        for product in self.products.values():
            all_stock.append(product)
        return all_stock
    
    def get_all_all_stock_names(self):
        all_stock_names = []
        for product in self.products.values():
            all_stock_names.append(product.get_name())
        return all_stock_names
    
    def get_all_all_stock_prices(self):
        all_stock_prices = []
        for product in self.products.values():
            all_stock_prices.append(product.get_price())
        return all_stock_prices
    
    def get_all_all_stock_stocks(self):
        all_stock_stocks = []
        for product in self.products.values():
            all_stock_stocks.append(product.get_stock())
        return all_stock_stocks
    
    def get_all_all_stock_stock(self, name):
        return self.products[name].get_stock()  
    
    def set_all_all_stock_stock(self, name, stock):
        self.products[name].set_stock(stock)

    def add_all_all_stock_stock(self, name, stock):
        self.products[name].add_stock(stock)

    def remove_all_all_stock_stock(self, name, stock):
        self.products[name].remove_stock(stock)

