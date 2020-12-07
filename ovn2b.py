def start():
	file_name = input('File name: (empty to quit) ')

	if not file_name:
		return

	try:
		with open(file_name) as f:
			lines = f.readlines()
			for line_number, line in enumerate(lines):
				print(line_number, end=' ')
				print(line)
	except FileNotFoundError:
		print('Error!')
		start()


start()
