import json

def register ():
	glos = {}
	login = input('введите логин ')
	passw = input('введите пароль ')
	if login not in glos.keys():
	 	glos[login] = passw
	 	print('пользователь добавлен')
	else:
	 	print('такой пользователь уже имеется')
	return glos

data = register()
print(data)

with open ('aaa1.json', 'w') as file:
	json.dump(data, file, indent=3)   