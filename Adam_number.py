def reverse_(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
a=int(input())
b=a**2
c=reverse_(a)
d=c**2
e=reverse_(d)
print(a**2==e)
