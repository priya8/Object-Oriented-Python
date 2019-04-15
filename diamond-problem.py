# -*- coding: utf-8 -*-
"""
@author: priyanka
"""

class A:
  def call(self):
    pass
 
class B1(A):
  def call(self):
    print("I am B1 - Parent")
 
class B2(A):
  def call(self):
    print("I am B2 - Parent")
 

 
class D(B2, B1):
  def whoCalled(self):
    print(self.call())
    
  def restructure(self, parent1, parent2):
    self.__class__.__bases__ = (parent1, parent2,)  

Dobject = D()
Dobject.whoCalled()
print("whoCalled() method appears in both B1,B2. To solve this diamond problem Python gives priority to the class that appears first in list of inheritance. So B2 is called")
print("------------")
print("Order of classes can be changed using restructure")
Dobject.restructure(B1,B2)
Dobject.whoCalled()