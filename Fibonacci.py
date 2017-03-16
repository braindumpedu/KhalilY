def fibo(n):
    i = 2
    F1 = 1
    F2 = 1
    while i !=n:
        F = F1 + F2
        F1 = F2
        F2 = F
        i = i + 1        
    return F2

print fibo(10)