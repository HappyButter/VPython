# Odd / Even / Prime number program

def oddEvenPrime(num):
    if num % 2 == 0 :
        print(num , " is an even number!")
    else: 
        print(num , " is an odd number!")
    
    isPrime(num)


def isPrime(num):
    flagPrime = 1
    halfNum = num // 2
    
    for i in range(2, halfNum + 1):        
        if num % i == 0:
            flagPrime = 0
            break
    
    if  flagPrime == 1:
        print(num , " is a Prime number!\n")
   

value = int(input("Eter your number: "))

print("-"*15)
oddEvenPrime(value)
print("-"*15)
oddEvenPrime(3)
print("-"*15)
oddEvenPrime(10)
