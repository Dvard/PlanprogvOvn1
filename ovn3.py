def get_contact_info():
	name = str(input('Name: '))
	phone_nbr = str(input('Phone number: '))

	return name, phone_nbr


while True:
	name, nbr = get_contact_info()

	if name and nbr:
		with open('TELEPHONENUM.txt', 'a+') as f:
			f.writelines([name + '\n', nbr + '\n', '\n'])
	else:
		break


