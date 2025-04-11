import json

glos = {}
with open ('aaa1.json', 'r') as file:
	glos = json.load(file) 
def register ():	
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

  