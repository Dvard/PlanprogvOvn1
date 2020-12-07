import random

rand_numbers = [str(random.randint(1, 101)) + '\n' for _ in range(20)]

with open('random_numbers.txt', 'w+') as f:
	f.writelines(rand_numbers)

with open('random_numbers.txt') as f:
	for line in f.readlines():
		print(line, end='')
