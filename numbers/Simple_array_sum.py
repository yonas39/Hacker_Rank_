"""
Given an array of integer find the sum of its elements. 
i.e arr= [1,2,3] ---> 1+2+3 =6  so return 6
"""
def simpleArraySum(array):
  """sum all the integers in the array and return its value"""

  return sum(array)

def sum_numbers(num):
  """
    This is the problem I created to test a closed form math formula:
    according to the formula the sum of the numbers between 1 to n can be 
    calculated as follows: n(n+1)/2. lets see if that is true !
  """
  return (num*(num+1)) / 2 

if __name__== '__main__':
  lis =[1,2,3,4,5,6,7]

  print(simpleArraySum(lis))

  #closed form 
  print (sum_numbers(7)) ## indeed it works 