# draw sinus in a file
import math

f = open ('result.txt','w')

x = [ (x*2*math.pi)/50 for x in range(51)  ] # list comprehension


for i in range(51):
    
    y = 50 * math.sin(x[i])
    y_new = int(y)
    
    if ( y_new > 0 ):
        f.write( 50 * ' ' + y_new * '+'  + '\n')
    elif ( y_new < 0):
        f.write( (50+y_new) * ' ' + (-y_new) * '-'  + '\n')
    else:
        f.write( 50 * ' ' + '0\n')


f.close()