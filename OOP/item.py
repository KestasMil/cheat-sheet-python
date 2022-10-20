import csv
import os

class Item:
    all = []
    
    def __init__(self, name: str, price: float, quantity: 0):
        self.__name = name
        self.price = price
        self.quantity = quantity
        
        Item.all.append(self)
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    def calculate_total_price(self):
        print(self.price * self.quantity)
        
    @classmethod
    def instantiate_from_csv(cls):
        # for f in os.listdir("OOP/"):
        #     print(f)

        with open('OOP/items.csv', newline='') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item['name'],
                price=float(item['price']),
                quantity=int(item['quantity'])
                )
            
        
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True