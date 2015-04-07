#!/usr/bin/env python
import numpy as np

'''
My solution(s) to the famous FizzBuzz test which asks the coder to solve the following:
Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
'''

nums = np.arange(1,101)

'''first solution'''
print('First Solution:')
#grab multiples of three and five
thirds = nums[2::3]
fives = nums[4::5]

for third in thirds:
	print('Fizz')
for fifth in fives:
	print('Buzz')

for num in nums:
	if num % 15 == 0:
		print('FizzBuzz')

'''second solution'''

for num in nums:
	if num % 3 == 0:
		print('Fizz')
	if num % 5 == 0:
		print('Buzz')
	if num % 15 == 0:
		print('FizzBuzz')

