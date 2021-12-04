import numpy as np

filename = 'input.txt'
data = np.loadtxt(filename, delimiter=',', dtype=int)

not_used = False
first = data[0]

number = 0

plus = 0
minus = 0

for x in data[1:]:
    if not_used == False:
        if x > first:
            plus += 1
        else:
            minus += 1
        not_used = True
        number = x
    else:
        if x > number:
            plus += 1
            number = x
        else:
            minus += 1
            number = x

print(plus, minus)