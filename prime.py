# Program of prime number
n = int(input("enter the number"))
for n in range(n-1,n+1):
    for x in range(2,n):
        if n % x == 0:
            print(n,"is not a prime number")
            break
        else:
            print(n,"is a prime number")
