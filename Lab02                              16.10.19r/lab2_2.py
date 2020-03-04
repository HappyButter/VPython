import math

f = open('result_ex2.txt','w')

def func(x):
    sum = 0
    for i in range(x):
        sum = sum + (((2*(i+1) - 1) ** (-1)) * ((-1) ** (i+2)))
    return sum

for i in range(10000001):

    if (i < 100):
        a = 4 * func(i+1)
        b = a/math.pi
        f.write(str(i+1) + ')    ' + str(a) + ',    ' + str(b) + '\n')
    
    if (i == 1000 or i == 10000 or i == 100000 or i == 10000000):
        a = 4 * func(i+1)
        b = a/math.pi
        f.write(str(i) + ')    ' + str(a) + ',    ' + str(b) + '\n')
    
print("Let's fight!")

f.close()