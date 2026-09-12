n=int(input('enter the number'))
count=0
x=n
while x!=0:
    x=x//10
    count=count+1

sum=0
x=n
while x!=0:
    d=x%10
    sum=sum+d**count
    x=x//10
if sum==n:
    print('is a arm strong number')
else:
    print('not a arm strong number')