import math
import os
import random
import re
import sys

def main():
   n=int(input("n? \n"))
   weird(n)
   
def weird(i):
    if i%2==0:
        if i>6 and i<20:
            print("Weird")
        elif i>2 and i<5:
            print("Not Weird")
        elif i>20:
            print("Not Weird")
    else:
        print("Weird")

main()