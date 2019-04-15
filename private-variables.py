# -*- coding: utf-8 -*-
"""
@author: priyanka
"""

class employee:
    def __init__(self, name):
        self.__name=name #private member
    
e1 = employee("Harry")
print("print(e1.__name) -> Throws error")
print("-----------")   
print("Name Mangling done by Python.Not recommended")
print(e1._employee__name)
