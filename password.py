x = 3
while x > 0:
	x = x - 1
	password = input('Please input the password: ')
	if password == 'a123456':
		print('Log in successfully!')
		break
	else:
		if x > 0:
			print('Wrong password, you can still try', x , 'times.')
		else:
			print('The retry chances are used up, please contact your bank.')