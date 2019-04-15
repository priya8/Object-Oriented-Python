# -*- coding: utf-8 -*-
"""
@author: priyanka
"""

class person:
    def __init__(self,name):
        self.name = name
    
    def printName(self):
        print("My name is " + self.name)
        
p1 = person("Harry")
print("Main Program creates a person object called p1")
print("Constructor is called first and object is initialized")
print("p1 is referenced as self in methods of classes")
print("-------------")
print("Method - printName is called which is used to access property called name")
p1.printName()
print("-------------")