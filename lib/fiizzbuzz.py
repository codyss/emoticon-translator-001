'''
Programming background in Python.

The first exercise allows you to assess your ability to program in Python.
As a data analyst, you will spend much of your time writing code and
programs to work with data or to build mathematical, statistical, or
machine learning models to find insights from data.

Complete this function that transforms a list of integers.

1)  For numbers that are multiples of three replace the integer with the string "Fizz".

2)  For numbers that are multiples of five replace the integer with the string "Buzz".

3)  For numbers that are multiples of both three AND five replace the integer
    with the string "FizzBuzz"

Your function should take in a list of integers as input.
Your function should not modify the input list.
Your function should return an updated list with integers and strings.
'''

def fizzbuzz(intList):
  new_list = []
  for i in intList:
    if i % 5 == 0 and i % 3 == 0:
      new_list.append('FizzBuzz')
    elif i % 5 == 0 and i % 3 != 0:
      new_list.append('Buzz')
    elif i % 5 != 0 and i % 3 == 0:
      new_list.append('Fizz')
    else:
      new_list.append(i)
  return new_list


def lucky_sevens(numbers):
  i = 0
  while i <= len(numbers):
    if i <= len(numbers) - 3:    
      if sum(numbers[i:i+3]) == 7:
        return True
        break
      else:
        i += 1


def disemvowel(string):
  new_string = ""
  for i in string:
    if i = 'a' or i = 'e' or i = 'i' or i='o' or i = 'u':
      pass
    else:
      new_string.append(i)
  return new_string



