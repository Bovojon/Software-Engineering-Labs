import math
from HeapSort import *
from QuickSort import *

def introsort(sortablelist):
    maxdepth = int(math.floor(math.log(len(sortablelist)))) * 2
    introhelp(sortablelist, maxdepth, 0, len(sortablelist)-1)

def introhelp(sortablelist, maxdepth, first, last):
    n = len(sortablelist)
    if n <= 1:
        pass
    elif maxdepth == 0:
        heapsort(sortablelist)
    else:
        middle = partition(sortablelist, first, last)
        introhelp(sortablelist, maxdepth - 1, first, middle - 1)
        introhelp(sortablelist, maxdepth - 1, middle + 1, last)