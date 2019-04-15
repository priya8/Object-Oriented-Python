# -*- coding: utf-8 -*-
"""
@author: priyanka
"""

def addNumbers(x, y, z = 0):  
    return x + y+z 
  
print("Polymorphism - Method Overloading") 
print(addNumbers(8, 3)) 
print(addNumbers(8, 3, 1)) 

print("--------------")
print("Polymorphism - Main Function is not aware of type of classes in the for loop")
class India(): 
    def capital(self): 
        print("New Delhi") 
  
  
class USA(): 
    def capital(self): 
        print("Washington, D.C.") 
  
  
ind = India() 
usa = USA() 
for country in (ind, usa): 
    country.capital() 
print("------------")
print("Polymorphism - Method Overriding by Child Class")
class Bird: 
  def fly(self): 
    print("General") 
    
class crow(Bird): 
  def fly(self): 
    print("Crow can fly") 
      
bird = Bird() 
cr = crow() 
bird.fly()
cr.fly()
