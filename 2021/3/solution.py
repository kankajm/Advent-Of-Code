import numpy as np

# This solution is inspired by: https://github.com/kodsnack/advent_of_code_2021/blob/main/alextelon-python/3/solve.py

filename = 'input.txt'
lines = np.loadtxt(filename, delimiter=',', dtype=str)

gamma_rate = ""
epsilon_rate = ""

for x in zip(*lines):
    if x.count('0') > x.count('1'):
        gamma_rate += '0'
        epsilon_rate += '1'
    else:
        gamma_rate += '1'
        epsilon_rate += '0'

g = int(gamma_rate, 2)
e = int(epsilon_rate, 2)

print('Part one:', e*g)


data = lines[::]
for i in range(len(data[0])):
    bits = list(zip(*data))[i]
    if len(data) == 1:
        break
    if bits.count('0') > bits.count('1'):
        data = [line for line in data if line[i] == '0']
    else:
        data = [line for line in data if line[i] == '1']
if len(data) == 1:
    oxygen = data[0]
oxygen = int(oxygen, 2)

data = lines[::]
for i in range(len(data[0])):
    bits = list(zip(*data))[i]
    if len(data) == 1:
        break
    if bits.count('0') <= bits.count('1'):
        data = [line for line in data if line[i] == '0']
    else:
        data = [line for line in data if line[i] == '1']
if len(data) == 1:
    co2 = data[0]
co2 = int(co2, 2)

print('Part two:', co2*oxygen)
