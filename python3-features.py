# -*- coding: utf-8 -*-
"""
@author: priyanka
"""

print("Significant Features of Python3.x")
print("1.Print is now a function")
print("------------------")
print("2.Division of 2 integers is a float")
print(4/2)
print(1/2)
print("------------------")
print("Use of // for integer division")
print(4//2)
print(1//2)
print("------------------")
print("3. Itertools is an built-in Python module that contains functions to create iterators for efficient looping")
from itertools import count
sequence = count(start=0, step=1)
while(next(sequence) <= 20):
    print(next(sequence))