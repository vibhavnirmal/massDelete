def fibonacchi(number):
    a=0
    b=1
    l=[0,1]
    for i in range(number-2):
        c=a+b
        a=b
        b=c
        p=c%10
        l.append(p)
    print(l)
    fib = [i for i in range(len(l))]
    return fib

fibonacchi(int(input()))
