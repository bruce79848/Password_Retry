x = 3
while x > 0:
	password = input('Please input the password: ')
	if password == 'a123456':
		print('Log in successfully!')
		break
	else:
		print('You can still try', x - 1 , 'times.')
		x = x - 1
		if x <= 0:
			print('Please contact your bank.')
			break
