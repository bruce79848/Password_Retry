x = 3
while x > 0:
	x = x - 1
	password = input('Please input the password: ')
	if password == 'a123456':
		print('Log in successfully!')
		break
	else:
		if x > 0:
			print('You can still try', x , 'times.')
		else:
			print('Please contact your bank.')