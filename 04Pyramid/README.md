# Homework

## 1. Pyramid

### What?
- a python file Seol_pyramid.py that prints:
         #
        ##
       ###
      ####
     #####
    ######
   #######
  ########

### How?
- 1. variable [stacks]: ask use the input; limit the number between 1 and 8.
    - if stack < 1 or stacks > 8: print something like 'plz input a number within the range of 1-8'
    - else: next
- 2a.
    - if stack == 1
        - print a single #
    - if stack == 2
        - 1st row: 1 space + 1 #
        - 2nd row: 0 space + 2 #s
    - if stack == 3
        - 1st row: 2 spaces + 1 #
        - 2nd row: 1 space + 2 #s
        - 3rd row: 0 space + 3 #s
    - if stack == 4
        - 1st row: 3 spaces + 1 #
        - 2nd row: 2 spaces + 2 #s
        - 3rd row: 1 space + 3 #s
        - 4th row: 0 space + 4 #s
    - ...
    - if stack == n
        - 1st row: (n-1) spaces + 1 #
        - 2nd row: (n-2) spaces + 2 #s
        - 3rd row: (n-3) spaces + 3 #s
        - ...
        - mth row: (n-m) spaces + m #s
        - ...
        - nth row: (n-n) spaces + n #s