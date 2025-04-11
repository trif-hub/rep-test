from random import randint
n = 5
m = [[randint(0,100) for i in range(n)] for j in range (n)]
nmax = 0 
for wex in m:
   for elem in wex:
      if elem > nmax:
         nmax = elem
         print (nmax)
for wex in m:
   print (wex)