def start():
	file_name = input('File name: (empty to quit) ')

	if not file_name:
		return

	try:
		with open(file_name) as f:
			print(f.read())
	except FileNotFoundError:
		print('Error!')
		start()


start()
