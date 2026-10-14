#move zero to end
nums = [0, 1, 0, 3, 12]
a=[]
for i in nums:
    if i!=0:
        a.append(i)
for i in nums:
    if i==0:
        a.append(i)
print(a)