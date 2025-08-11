#  indentify most repetitive element in the list

num_counter ={}

L1 = [1,1,2,3,4,2,3,4,3,5,3] 
for i in L1:
    if i in num_counter:
        num_counter[i] += 1
    else:
        num_counter[i] = 1

temp =0
final_result = None

for k,v in num_counter.items():
    print(f"k: {k},v: {v},temp: {temp}")

    if v > temp:
        temp = v
        final_result = k
print(final_result)


 

