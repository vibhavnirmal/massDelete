
x = int(input())

def factorial(x):
    if x <= 1:
        return x
    else:
        return x * factorial(x-1)

count = 0
def count_zeros(p):
    global count
    if p%10 == 0:
        p = p//10
        count = count + 1
        count_zeros(p)
        return count
    else:
        return count

y = factorial(x)
print(y)
print(count_zeros(y))
