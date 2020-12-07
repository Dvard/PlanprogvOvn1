def start():
	import os
	file_name = input('File name: (empty to quit) ')

	if not file_name:
		return

	if os.path.isfile(file_name):
		os.system(f'less {file_name}')
	else:
		print('Error!')
		start()


start()
