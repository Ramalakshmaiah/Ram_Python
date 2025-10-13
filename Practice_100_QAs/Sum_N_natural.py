
# Method 1

num = int(input("Enter a number !"))

sum = (num*(num+1))/2

print("The Sum of N natural Number is {}".format(sum))

# Method 2

num = int(input("Enter the number "))

value = 0

for i in range(1,num+1):

    value = value + i

    print("The sum of N natural number is",value)