# Set testing

L1 = [1, 4, 5, 6, 6, 10]
L2 = [1, 2, 5, 5, 17]

def setTest(lis_1, lis_2):
    set1 = set(lis_1)
    set2 = set(lis_2)
    setResult = set1 & set2
    return setResult

print(setTest(L1, L2))


L = [1,2,3]
L.insert(-1,400)
print (L)