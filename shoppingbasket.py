# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re

class ShoppingBasket:
    def __init__(self, catalogue, offers, basket):
        self.catalogue = catalogue
        self.offers = offers
        self.basket = basket
        self.subtotal_counter = 0
        self.discount_counter = 0


    def subtotal(self, product):
        """ we first multiply the price of a particular product by how many there are in the basket.
        The result is then added to the subtotal counter
        """
        return self.catalogue[product]*self.basket[product]                                                                                
 
    
    def type_of_discount(self, product):
        return [int(i) for i in self.offers[product].split() if i.isdigit()]

    
    def discount(self, product):
        """ if type_of_discount is empty it means that we have a percentage off discount (e.g 25% discount).
            Otherwise we have a buy ... get ... for free discount (e.g Buy 2 get 1 free).
        """
        if product in self.offers and len(self.type_of_discount(product))>0:
            num_products_to_buy_for_offer = self.type_of_discount(product)[0] #number of products to buy for the 'buy ... get .. free' to be applicable.
            if  self.basket[product]>=num_products_to_buy_for_offer:
                return (int(self.basket[product]/num_products_to_buy_for_offer)*self.catalogue[product])-self.catalogue[product]
            else:
                print('No discount available as not enough products on offer has been selected by customer')
        elif product in self.offers and self.type_of_discount(product)==[]:
            percent_discount = re.findall(r'\d+%', self.offers[product])
            percent_discount_in_decimal = float(percent_discount[0].rstrip("%"))/100 #percentage discount in decimal number
            return percent_discount_in_decimal * self.catalogue[product] * self.basket[product]
        else:
            print('no offer!!!')


    def total(self):
        total = self.subtotal_counter - self.discount_counter
        return total

    
    def result(self):
        #Assuming that all products in basket are in catalogue
        for product in self.basket:
            if self.basket[product]<0:
                return 'Basket cannot have a negative price!'
            else:
                self.subtotal_counter += self.subtotal(product)
                #print(self.subtotal_counter)
                if product in self.offers:
                    self.discount_counter += self.discount(product)
                else:
                    pass

        subtotal = round(self.subtotal_counter, 2)
        discount = round(self.discount_counter, 2)
        total = round(self.total(), 2)
        return 'ShoppingBasket(Sub-total=%r, Discount=%r, Total=%r)'%(subtotal, discount, total)

            
            
def test_shopping_basket():
    catalogue = {'beans':0.99, 'biscuits':1.20,'sardines':1.89, 'sausage':2.00, 'meat':1.00}
    offers = {'beans':'Buy 2 get 1 free', 'sardines': '25% off'}
    basket = {'beans': 2, 'biscuits':1, 'sardines':2}

    test_shopping_baskett = ShoppingBasket(catalogue, offers, basket)
    print(test_shopping_baskett.result())

if __name__ == '__main__':
    test_shopping_basket()
    