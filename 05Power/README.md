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