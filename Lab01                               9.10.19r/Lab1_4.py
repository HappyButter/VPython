# Perfect numbers generator

def generatePerfectNum(N):
    for i in range(N):
        halfNumber = i//2 
        sum = 0
        for k in range(halfNumber):
            if i % (k+1) == 0:
                sum += (k+1)
    
        if i==sum & sum > 2:
            print(i)
            print("It's a Perfect number!!\n")
    
generatePerfectNum(10000)