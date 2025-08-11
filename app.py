

# Name = int(input("Enter a No: "))

# if Name%2==0:
#     print("This No is Even")
# else:
#     print("This No is odd")


palidrom = input("Enter a name: ")

# reverse = palidrom[::-1]

# if reverse==palidrom:
#     print("This is a palidrom")
# else:
#     print("Not a palidrom")

i=len(palidrom)-1
rev=[]

while 0<=i:
    x=palidrom[i]
    rev.append(x)
    i-=1
reverse = result = "".join(rev)
if palidrom == reverse:
    print("palindrom")
else:
    print("not a palindrome")





