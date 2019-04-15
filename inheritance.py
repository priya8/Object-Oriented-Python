# -*- coding: utf-8 -*-
"""
@author: priyanka
"""

class person:
    def __init__(self,name):
        self.name = name
    
    def printName(self):
        print("My name is " + self.name)
        
class employee(person):
    pass

print("Create object of type person")
p1 = person("Harry")
p1.printName()
print("----------")

print("Create object of type employee")
e1 = employee("Potter")
print("Employee object takes all functions from person class and uses it")
e1.printName()
print("----------")