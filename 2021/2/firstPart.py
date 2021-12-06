import numpy as np

filename = 'input.txt'
data = np.loadtxt(filename, delimiter=',', dtype=str)

horizontal_position = 0
depth = 0

for x in data:
	x = x.split()
	if x[0] == 'down':
		depth += int(x[1])
	elif x[0] == 'up':
		depth -= int(x[1])
	elif x[0] == 'forward':
		horizontal_position += int(x[1])

print(horizontal_position * depth)