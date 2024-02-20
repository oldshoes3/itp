# Mice

## What?
- a python file (~{Seol}mice.py~ Seol_mice.py) that prints following:

		3
			Blind
				Mice


- Having a calculation for 3
    - 1 / 2 * 3 / 4 * 5 / 6 * 7 / 8 * 9 / 10 * 11 / 12 * 13 / 14 * 15 -> round off with int() function

## How?
- print function
    - 3 - (new line)
    - (tap) - 'Blind' - (new line)
    - (tap) - (tap) - 'Mice'

- put the above formula instead of 3
- (new line) -> \n
- (tap) -> \t

## problem
- If the file is in the github repository and run it, the error (can't find '__main__' module in ...) shows up. If the file is in other folder in my laptop, it runs without error.
    - solution: Erasing '{' and '}' in the file name removes the error (2024-02-20)


## Additional Seol_mice_advanced.py file (2024-02-20 added)
- instead of the long expression (1 / 2 * 3 / 4 * 5 / 6 * 7 / 8 * 9 / 10 * 11 / 12 * 13 / 14 * 15)
- using loop
    - make 2 variables (result=1) and (ind=1)
    - (ind) will increase by one in each iteration
    - each iteration
        - if (ind) is odd (remainder is 1 when divided by 2)
            - (result) * (ind)
        - else (if (ind) is even)
            - (result) / (ind)
    - loop while (result < 3) (the loop stops as soon as the result >= 3)
    - round off the (result) (using int()) to make 3