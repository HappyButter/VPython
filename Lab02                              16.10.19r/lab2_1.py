# Monte Carlo 
import random
import math

f = open('result_ex1.txt','w')

circleHits = 0


for i in range(1000001):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
     
    if  math.sqrt(x ** 2 + y ** 2) < 1 :
        circleHits = circleHits + 1
    
    circleField = (4 * circleHits) / (i + 1)
    accuracy = circleField / math.pi

    if (i < 101): 
        f.write(str(i+1) + ')    ' + str(circleField) + ',    ' + str(accuracy) + '\n')
    if (i == 1000 or i == 10000 or i == 100000 or i == 1000000):
        f.write(str(i) + ')    ' + str(circleField) + ',    ' + str(accuracy) + '\n')


    
f.close() 