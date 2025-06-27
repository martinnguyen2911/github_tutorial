
print("Hello, World!")
def mean(input):
  sum = 0
  for entry in input:
    sum += entry
  return sum / len(input)

my_list = [0, 1, 2, 3, 4, 5]
print(mean(my_list))

import math
def median(input):
  mid = len(input)//2
  return (input[mid-1] + input[mid])/2

my_list = [0, 1, 2, 3, 4, 5]
print(median(my_list))