#!/usr/bin/env python3

import ipdb

class CashRegister:
  
    def __init__ (self, discount = 0):
        
        self.total = 0
        self.discount = discount
        self.items = []
        self.price_list = []
        
    def add_item(self, title, price, quantity = 1):

        self.title = title
        self.price = price

        i = 1
        while i <= quantity:
          self.items.append(title)
          i += 1
          
        total_transaction_price = self.price*quantity

        self.price_list.append(total_transaction_price)

        self.total += (price*quantity)

    def apply_discount(self):
        
        if(self.discount != 0):
          self.total = int(self.total- self.discount/100*self.total)
          print(f"After the discount, the total comes to ${self.total}.")
        else:
          print("There is no discount to apply.")
    
    def void_last_transaction(self):

        self.total = self.total - self.price_list[-1]
      
        

# PriceCX is paying = Total Price of the item - discount*Total Price    

# Assume discounts are percents

# sampleObj.add_item("eggs", 100)
