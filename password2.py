password = 'a123456'
x = 3
while True:
	pwd = input('Please input the password: ')
	if pwd == password:
		print('Log in Successfully!')
		break
	else:
		x = x - 1
		print('Failed to log in! You still have', x ,'time.')
		if x <= 0:
			print('Please contact your bank.')
			break

