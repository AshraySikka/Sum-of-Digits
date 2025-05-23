num = int(input('Enter a number: '))
s=0
n=num
while n>0:
    r=n%10
    s=s+r
    n=n//10
print('Sum of all the digits of',num,' is: ',sum)
