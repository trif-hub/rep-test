while True:
   password = input("Введите пароль: ")
   if all([
      len(password) > 8,
      any(c.isupper() for c in password),
      any(c.islower() for c in password)      
   ]):
      print("пароль подходит ", password)
      break
   else: 
    	print ("пароль не подходит  11")
    	
