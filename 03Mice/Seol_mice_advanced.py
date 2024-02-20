#makeThree = int(1 / 2 * 3 / 4 * 5 / 6 * 7 / 8 * 9 / 10 * 11 / 12 * 13 / 14 * 15)

result = 1
ind = 1
while result < 3:
    if ind % 2 == 1:
        result = result * ind
    else:
        result = result / ind
#    print (ind, result)
    ind = ind + 1


print(f'{int(result)}\n\tBlind\n\t\tMice')