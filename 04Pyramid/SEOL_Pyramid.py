stacks = int(input('Kindly enter a number between 1 and 8: '))
if stacks < 1 or stacks > 8:
    print("Seriously what's wrong with you")
else:
    for i in range(1, stacks + 1):
        print(' ' * (stacks - i), '#' * i, sep='')