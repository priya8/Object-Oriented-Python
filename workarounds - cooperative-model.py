# -*- coding: utf-8 -*-
"""

@author: priyanka
"""
print("---------------------------------")
from abc import ABC, abstractmethod 
class trialAddon():
    def __init__(self,val1,val2):
        self.constant_val1 = val1
        self.val2 = val2
        
    def __setattr__ (self, attr, value):
        #if hasattr (self, attr):
        if attr[:9] == 'constant_' and hasattr (self, attr): 
            raise Exception ("Attempting to alter read-only value")
        self.__dict__[attr] = value
        
class Polygon(ABC): 
	# abstract method 
	def noSides(self): 
		pass

class Triangle(Polygon): 
	# overriding noSides abstract method 
	def noSides(self): 
		print("I have 3 sides") 

class Pentagon(Polygon): 
	# overriding abstract method 
	def noSides(self): 
		print("I have 5 sides") 


# Driver code 
print("Code snippets for add-ons - Abstract Methods/Classes - Cooperative Object Oriented Model")
print("------------")
print("From Python 2.6 developers introduced abstractmethod package to define abstract class")
print("Triangle inherits polygon and overrides the noSides Method")
R = Triangle() 
R.noSides() 
print("------------")
print("Pentagon inherits polygon and overrides the noSides Method")
R = Pentagon() 
R.noSides()  
print("------------")
print("Code snippets for add-ons - Named Constants - Cooperative Object-Oriented Model")
print("Error in setting ta.constant_val1 = 17. Attempting to alter read only values")
print("-------------")
print("This makes all variables of the class as write once only. We can name all constant variables as 'constant_'+ variable name and put that condition in set_attr")
ta = trialAddon(12,13)
print("Original Value of constant_val1 " +str(ta.constant_val1))
print("Original Value of val2 " + str(ta.val2))
#ta.constant_val = 17
ta.val2 = 20
print("Changed Value of constant_val1 " + str(ta.constant_val1))
print("Changed Value of val2 " + str(ta.val2))

print("--------------------")