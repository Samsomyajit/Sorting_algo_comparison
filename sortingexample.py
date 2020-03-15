# -*- coding: utf-8 -*-
"""
Created on Sun March  15 2020
@author: Somyajit Chakraborty
"""

from sorting import getnewlist, bubble, shuttle, insertion, merge, test, produceresults

randomlist = getnewlist(500) #Get a list of 500 random numbers

print("Bubble took: " + str(test(bubble, randomlist)) + " seconds.")
print("Shuttle took: " + str(test(shuttle, randomlist)) + "seconds.")
print("Insertion took: " + str(test(insertion, randomlist)) + "seconds.")
print("Merge took: " + str(test(merge, randomlist)) + "seconds.")

produceresults(1, 1000, 20) #Comparison graph between algorithms acting on list of size 1 to 1000, incrementing by 20
