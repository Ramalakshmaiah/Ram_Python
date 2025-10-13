# Greatest of the two numbers
# first = int(input("Enter the fisrt no "))
# second = int(input(" Enter the second no "))

# if first > second:
#     print("First no is greater than second ")
# else:
#     print("Second no is greater than first")

# Greatest of the three numbers

first = int(input("Enter the fisrt no "))
second = int(input(" Enter the second no "))
third = int(input("Enter the third no "))

if first > second and first > third:
    print("first no is greater than second and third no")
elif second > first and second > third:
    print("second no is greater than first and third no")
else:
    print("third no is greater than second and first no")