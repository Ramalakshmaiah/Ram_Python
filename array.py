# from array import *

# arr = array('i',[3,5,7,8,10])

# newarr = array(arr.typecode,(a*a for a in arr))

# for e in newarr:
#     print(e)

from array import *

arr = array('i',[])

n = int(input("Enter the length of the array "))

for i in range(n):
    x = int(input("Enter the next value "))
    arr.append(x)
print(arr)

val = int(input("Enter the value search "))

k = 0

for e in arr:
    if e==val:
        print(k)
        break
    k+=1
print(arr.index(val))

