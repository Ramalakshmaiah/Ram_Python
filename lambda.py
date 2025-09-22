# f = lambda a,b:a+b

# result = f(45,34)

# print(result)

nums = [2,3,4,5,6,7,8,9,10,11,23,34]

evens = list(filter(lambda n : n %2==0,nums))

print(evens)

odds = list(filter(lambda n : n %2!= 0,nums))

print(odds)

doubls = list(map(lambda n: n*2,evens))

print(doubls)