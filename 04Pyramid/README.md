# Homework

## 1. Pyramid

### What?
- a python file Seol_pyramid.py that takes input between 1 and 8
- if input is 8, prints the following.

<pre>
               #
              ##
             ###
            ####
           #####
          ######
         #######
        ########
</pre>

- if input is less than 8, [...]

### How?
- 1st: variable [stacks]: ask user the input; limit the number between 1 and 8.
    - if stack < 1 or stacks > 8: print something like 'plz input a number within the range of 1-8'
    - else: next
- 2nd:

<pre>
	if stack == 1  
		one row: 0 space + 1 #  
	if stack == 2  
		1st row: 1 space + 1 #  
		2nd row: 0 space + 2 #s  
	if stack == 3  
		1st row: 2 spaces + 1 #  
		2nd row: 1 space + 2 #s  
		3rd row: 0 space + 3 #s  
	if stack == 4  
		1st row: 3 spaces + 1 #  
		2nd row: 2 spaces + 2 #s  
		3rd row: 1 space + 3 #s  
		4th row: 0 space + 4 #s  
	...  
	if stack == n  
		1st row: (n-1) spaces + 1 #  
		2nd row: (n-2) spaces + 2 #s  
		3rd row: (n-3) spaces + 3 #s  
		...  
		mth row: (n-m) spaces + m #s  
		...  
		nth row: (n-n) spaces + n #s
</pre>

- It's possible to have only one for loop
    - use [for i in range(1, stacks+1)], so 1st iteration has i = 1, nth iteration has i = n
    - in each iteration, print ' ' * (stacks - n)
    - in each iteration, print '#' * n

## 2. Fizzbuzz

### What?
- a python file Seol_fizzbuzz.py that prints integers from 1 to 100, except:
    - integers divisible by 3 turn "Fizz"
    - integers divisible by 5 turn "Buzz"
    - integers divisible by both 3 and 5 turn "FizzBuzz"

### How?
- have for loop, have 100 iteration
    - let's have range(1, 101) so the i (index) starts from 1 to 100
- multiples of 3 AND 5 -> FizzBuzz (filter multiples of 15 out here)
- multiples of 3 -> Fizz
- bultiples of 5 -> Buzz
- else -> i
- increase i