# Simple def 
"""
def func (x,y):
    if x>y:
        return x
    else:
        return y

print(func(10,11))

"""

# Simple import things from a path
"""
import sys 
sys.path.append('C:User\Wysokie Energie\\Desktop')
import mymodule 

mymodule.func(3,4)
"""

# print (_name_) gives the name of the module you take things from
# print (_name_) in main fives "_main_"


# checking time!
"""
import time
start = time.clock()
i = 10**8
while i:
    i = i - 1
t = time.clock() - start
print (round(t,4), 'seconds')
"""

# Nice code!
"""
L = ['a','b','c']

for i in range(len(L)):
    print(i)
"""

print("10")
f = open('notes.txt','w')
f.write('let us be kids forever\n')
f.close()