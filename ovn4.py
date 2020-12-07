contacts = []

with open('TELEPHONENUM.txt') as f:

	is_name = True
	for line in f.readlines():
		line = line.replace('\n', '')

		if line:
			if not is_name:
				contacts[-1] = contacts[-1] + ': \t' + line
				is_name = True
				continue

			contacts.append(line)
			is_name = False
		else:
			is_name = True

for contact in contacts:
	print(contact)
