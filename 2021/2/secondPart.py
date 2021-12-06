import numpy as np

filename = 'input.txt'
data = np.loadtxt(filename, delimiter=',', dtype=str)

aim = 0
depth = 0
horizontal_position = 0

for x in data:
	x = x.split()
	if x[0] == 'down':
		aim += int(x[1])
	elif x[0] == 'up':
		aim -= int(x[1])
	elif x[0] == 'forward':
		horizontal_position += int(x[1])
		depth += (int(x[1]) * aim)

print(horizontal_position * depth)