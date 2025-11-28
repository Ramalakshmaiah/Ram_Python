
# # n = int(input("Enteer a number: "))

# # a,b = 0,1

# # while a < n:
# #     print(a,end =" ")
    
# #     a,b = b,a+b

# def feb(n):
#     a = 0
#     b = 1

#     if n==1:
#         print(a)

#     else:
#         print(a)
#         print(b)

#         for i in range(2,n):
#             c = a + b
#             a = b
#             b = c
#             print(c)
# feb(10)

def fact(n):

    if n == 0:
        return 1
    return n * fact(n-1)

result = fact(5)

print(result)