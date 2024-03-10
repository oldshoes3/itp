# Power

## Seol_power.py that prints y=x^2 horizentally from -8 to 8

- one of the template given as a sparting point

<pre>
for i in range(-8, 9):
</pre>

- found out:
    - 1st row: i == -8, 64 '*'s
    - 2nd row: i == -7, 49 '*'s
    - 3rd row: i == -6, 36 '*'s
    - ...
    - 9th row: i == 0, zero *
    - 10th row: i == 1, 1 '*'
    - 11th row: i == 2, 4 '*'
    - ...
    - 17th row, i == 8, 64 '*'s 
- in the each row, the number of '*' will be i^2

- under a for loop:

<pre>
for i in range(-8, 9):
</pre>

- add a print statement that tells 'multiply '*' by i^2
 
<pre>
print('*' * (i ** 2))
</pre>


- concern:
     - It seems this assignment was intended for utilizing function defination and call
        - get_power(x, n) seems to be for a powering function instead of just write (i ** 2)
        - print_graph(n) seems to be for a function that tells "print the character '*' n times"
    - write the following code.
        - looks more complex. commented out

<pre>
def get_power(x, n):
    return x ** n

def print_graph(n):
    print('*' * n)

for i in range(-8, 9):
    print_graph(get_power(i, 2))
</pre>
