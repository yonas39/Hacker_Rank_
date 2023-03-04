import math
import os
import random
import re
import sys

"""
PROBLEM:
      Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal 
      value of each fraction on a new line with 6 places after the decimal.
      
      Note: 
        This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with 
        absolute error of up to 10^(-4) are acceptable.
      Example:
        arr= [1,1,0,-1,-1]
        there are n= 5 elements , two positive and two negative and one zero and their ratios are 2/5, 2/5, 1/5 with the decimals 
        0.400000, 0.400000, 0.200000
      complete the plusMinus function: plusMinus has the following 
        : parameter int arr[n]: an array of integers
        : contstraint
            0<n<100
            -100 <= arr[i] <=100
            
      The output should be the following: 
        In 3 lines, each 6 decimal:
          1. print proportion of positive values
          2. print proportion of negative values 
          3. print proportion of zeros

      
        
"""


def plusMinus(arr):
  """ 
    The plusMinus function identifies the numbers in the given array whose values are in less than zero, greaterthan zero or equal to zero. 
    Then it calculates the ratio for all the sections identified and return theier values with 6 decimal points. 
  """
    length=len(arr)
    less=0
    mid=0
    upper=0
    
    for num in arr:
       #number < 0
       if num <0:
          less+=1
       #numver >0
       elif num >0:
           upper+=1
       #numver ==0
       elif num==0:
           mid+=1
           
    print(format(upper/length,".6f")) 
    print (format(less/length,".6f")) 
    print(format(mid/length,".6f"))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
