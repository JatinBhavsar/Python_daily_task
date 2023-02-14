# WAP to print sum and count of even odd numbers

l1=[]
nums=[]
e_count=0
o_count=0
e_sum = 0
o_sum = 0

for i in range(10):
    nums = int(input())
    l1.append(nums)

for i in l1:
    if i%2 ==0:
        e_count += 1
        e__sum += 1
    else:
        o_count += 1
        o_sum += 1

print("count of even number : ", e_count)
print("count of odd number : ", o_count)
print("sum of even number : ", e_sum)
print("sum of odd number : ", o_sum)

    
    
