# -*- coding: utf-8 -*-
"""
Created on Sun March  15 2020
@author: Somyajit Chakraborty

"""

from random import random
from time import clock
import matplotlib.pyplot as plt

#randlist = [random() for x in range(2000)]

def getnewlist(nums):
    """Return a list of (n) random numbers."""
    return [random() for x in range(nums)] #Return new generated list of random nums back to call


def bubble(numbers): # Bubble sort implementation
    """Sort list using bubble sort."""
    nums = len(numbers)
    for i in range(nums):
        for j in range( i + 1, nums):
            if numbers[j] < numbers[i]: #is the next num less than the current
                numbers[j], numbers[i] = numbers[i], numbers[j] #if yes, swap
def insertion(numbers):
    """sort list using insertion sort."""
    nums = len(numbers)
    for i in range(1, nums):

            key = numbers[i]

            j = i-1
            while j >= 0 and key < numbers[j]:
                    numbers[j + 1] = numbers[j]
                    j -= 1
            numbers[j + 1] = key

def shuttle(numbers): #Shuttle (insertion) sort implementation
    """Sort list using shuttle sort."""
    for index in range(1, len(numbers)):

        currentvalue = numbers[index]
        position = index

        while position > 0 and numbers[position - 1] > currentvalue: #while true check if num should carry on being compared
            numbers[position] = numbers[position - 1] #insert num before num just compared
            position -= 1 #decrease position var by 1

        numbers[position] = currentvalue

def merge(numbers):
    """Sort list using merge sort."""
    nums = len(numbers)
    if nums>1:
        mid = nums//2
        lefthalf = numbers[:mid]
        righthalf = numbers[mid:]

        merge(lefthalf)
        merge(righthalf)
        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                numbers[k]=lefthalf[i]
                i=i+1
            else:
                numbers[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            numbers[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            numbers[k]=righthalf[j]
            j=j+1
            k=k+1

def test(sorttype, unsortedlist):
    """Test a sorting algorithm on a list and return execution time."""
    #Set copy equal to a new copy (different mem. location) of unsortedList to preserve current list
    #using the [:] split command which returns a copy of the whole list but as a new object
    copy = unsortedlist[:]
    start = clock() #Set start time. TODO - May convert to using timit module.
    sorttype(copy) #Run bubble or shuttle sort with copy of unsorted list as argument
    duration  = clock() - start #Work out how long the execution of algorithm took and set to duration
    #print(sortType.__name__ + " took " + str(duration) + " seconds.")
    return duration

def produceresults(startnumofnums=1, endnumofnums=2000, increment=50):
    """Produce a graph of # of #'s in random list against execution time for each algorithm."""
    xvals = []
    ybubble = []
    yshuttle = []
    yinsertion = []
    ymerge = []

    for i in range(startnumofnums, endnumofnums, increment):
        listtosort = getnewlist(i)[:] #Set listtosort to a new list of random numbers
        xvals.append(i) #append current number of numbers in list to x values
        ybubble.append(test(bubble, listtosort)) #append duration returned from sorting alg. to relevant yval list
        yshuttle.append(test(shuttle, listtosort)) #append duration returned from sorting alg. to relevant yval list
        yinsertion.append(test(insertion, listtosort)) #append duration returned from sorting alg. to relevant yval list
        ymerge.append(test(merge, listtosort)) #append duration returned from sorting alg. to relevant yval list

    plt.plot(xvals, ybubble, color="r", label="Bubble") #Set line on plot
    plt.plot(xvals, yshuttle, color="b", label="Shuttle") #Set line on plot
    plt.plot(xvals, yinsertion, color="g", label="insertion") #Set line on plot
    plt.plot(xvals, ymerge, color="y", label="merge") #Set line on plot
    plt.xlabel("Number of numbers in random list") #Label the x-axis
    plt.ylabel("Time taken to sort / seconds") #Label the y-axis
    plt.title("Time taken for sorting algorithms to sort random lists") #Give the graph a title
    plt.legend(loc=2) #Give the graph a legend to differentiate between lines. Set loc. to top left.
    plt.show() #Show the graph
