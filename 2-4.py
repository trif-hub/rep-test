n = [1, 4, 1, 6, 'hello', 'a', 5, 'hello']
unique = []
rep = []
for i in n:
   if i not in unique:
      unique.append(i)
   else:
      rep.append(i)
print(unique, rep)