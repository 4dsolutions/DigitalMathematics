# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:10:41 2016

@author: Kirby Urner

Show some types working together to simulate a shopper
in a Supermarket, with a fixed starting amount of money.

Inventory keeps track of how much of a product remains.

Supermarket keeps track of income, should equal sum of purchases.
"""

import json

class NoMoney(Exception):
    pass

class OutOfStock(Exception):
    pass

class SuperMarket:
    """
    Persists buyable items in a json file.
    Initializes with 0 cash
    """
    def __init__(self, source):
        self.source = source
    
    def __enter__(self):
        self.inventory = Inventory(self.source)
        self.cash = 0
        return self
        
    def buy(self, shopper, item, how_many):
        """
        remove money from shopper wallet, add qty of item
        to basket, abort if customer short on cash
        """
        if item in self.inventory.wares: # check keys
            price = self.inventory.wares[item][0]
            try:
                self.inventory.remove_item(item, how_many)
                shopper.add_item(item, price, how_many)
                self.cash += price * how_many
            except NoMoney:
                # print("Customer out of money")
                raise  # re-raise exception
            except OutOfStock:
                # print("Don't have enough in stock")
                raise

    def __exit__(self, *oops):
        """
        write json file
        """
        self.inventory.save_items()
        
    def __repr__(self):
        return "SuperMarket with cash: {}".format(self.cash)
          
class Shopper:
    
    def __init__(self, name, budget):
        self.name = name
        self.basket = { }
        self.wallet = budget # budgeted allowance

    def add_item(self, item, price, qty):
        """
        add qty of item to basket and pay, if money available
        """
        if self.wallet - qty * price < 0:
            raise NoMoney
        self.basket[item] = self.basket.get(item, 0) + qty
        self.wallet -= qty * price
        
    def __repr__(self):
        return "{}: {}; {}".format(self.name, self.wallet, self.basket)
        
class Inventory:
    """
    Supermarket brings inventory instance on board upon
    initialization, increments / decrements items, reads
    and writes to json file.  Does not track cash.
    """
    
    def __init__(self, the_file):
        print("Loading inventory...")
        self.storage = the_file
        with open(the_file, 'r') as warehouse:
            self.wares = json.load(warehouse)
            
    def save_items(self):    
        print("Saving inventory...")
        with open(self.storage, 'w') as warehouse:
            json.dump(self.wares, warehouse)
            
    def remove_item(self, item, qty):
        if qty > self.wares[item][1]:
            raise OutOfStock
        self.wares[item][1] -= qty
        
    def add_item(self, item, qty):
        self.wares[item][1] += qty

def test_data():
    stuff = {
       "Snicker-Snacks": [5.99, 10],
       "Polly's Peanuts": [3.99, 10],
       "Dr. Soap": [4.99, 10]}
    with open("the_stuff.json", 'w') as warehouse:  
        json.dump(stuff, warehouse, indent=4)
            
def simulation():
    
    test_data()  # initialize the_stuff.json
    kirby = Shopper("Kirby", 1000)
    
    with SuperMarket("the_stuff.json") as market:
        try:
            market.buy(kirby, "Snicker-Snacks", 2)
            market.buy(kirby, "Polly's Peanuts", 2)
            market.buy(kirby, "Dr. Soap", 2)  # triggers exception
        except NoMoney:
            print("Uh oh, out of money!")
        except OutOfStock:
            print("Uh oh, out of stock!")
        else:
            print(kirby)
            print(market.inventory.wares)
            print(market)

if __name__ == "__main__":
    simulation()