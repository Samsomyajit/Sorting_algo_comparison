# Sorting Algorithms Speed Comparison

## Author
Name: Somyajit Chakraborty, Research and Development Manager/CTO, Bread and Code

## Description

This python script defines functions that enable the user to test and compare the 'Bubble' and 'Shuttle', 'Insertion', 'Merge' sorts on some randomly generated lists.

## Optional / Required Modules

Apart from in-built modules, this code defines a function to plot a comparison of execution times for each algorithm.
The necessary module for this to work is **matplotlib**. If you are on windows I recommend getting a distribution of python that comes with many packages pre-installed such as **python(x,y)** or **WinPython**.
If you are on linux then I recommend using your package manager to install matplotlib (e.g. `sudo apt-get install python-matplotlib`).

## Example Usage

````python
from sorting import getnewlist, bubble, shuttle, insertion, merge, test, produceresults

randomlist = getnewlist(500) #Get a list of 500 random numbers

print("Bubble took: " + str(test(bubble, randomlist)) + " seconds.")
print("Shuttle took: " + str(test(shuttle, randomlist)) + "seconds.")
print("Insertion took: " + str(test(insertion, randomlist)) + "seconds.")
print("Merge took: " + str(test(merge, randomlist)) + "seconds.")

produceresults(1, 1000, 20) #Comparison graph between algorithms acting on list of size 1 to 1000, incrementing by 20
````
## Graph Analysis
 <p align="center">
  <img  src="https://github.com/Samsomyajit/Sorting_algo_comparison/blob/master/graph/Figure_1-1.png">
</p><br>
<h2>Runtime Analysis</h2>
 <p align="center">
  <img  src="https://github.com/Samsomyajit/Sorting_algo_comparison/blob/master/graph/runtime_analysis.JPG">
</p>

## License
<pre>
The MIT License(MIT)

Copyright (c) 2020 Somyajit Chakraborty

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
</pre>
