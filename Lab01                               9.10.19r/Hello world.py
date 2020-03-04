"""L = [1, 2, 3, 4, 5, 6]

L.append(1)
print(L)

L.insert(1, 500)
print(L)

a = L.pop(2)
print(L,'\n',a)
"""


"""
L = [1,2,3,4,5]

set1 = set(L)
set2  = set([4,5,9,10,10,10])
print (set1)
print (set2)

print (set1-set2)

"""


"""
tel = {'John':1234, 'Kate': 5678}

tel ['Tom'] = 9000
tel ['Bob'] = 1000

print (tel)
print (list(tel.keys()))
print (list(tel.values()))
"""


"""
def fun1(x,y):
    return x*y

print (fun1(5,2))

print (8.5-8.4)
"""


"""
import random

print (random.random())
print (random.uniform(0,10))
print (random.randint(2,100))
print (random.choice(['yes','no']))
print (random.randrange(1,100,2))

#Marsenne Twister read 
"""


"""
import math
print (math.cos(3.14))

print (dir(math))
"""


# List comprechantion -----> Exam


"""
import math
import random

print ([x/10. for x in range(0,10)])

print ([[x,y] for x in range(5) for y in range(5) if x>y and x>=2 and y>=2])
"""


"""
L = [3, 5, 7, 2, 8, 9]
a = 0
b = 0

for i in L:
    a = L[b] + a
    b = b + 1

print(a)
"""
