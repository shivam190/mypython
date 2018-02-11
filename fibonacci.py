# Fibonacci Series using function
def fib(n):
    a = 0
    b = 1
    i = 1
    c = 0
    print(a,"\n")
    print(b,"\n")
    while(i<=n):
        c = a+b
        print(c,"\n")
        a = b
        b = c
        i = i + 1
        
