
def euc(a,b):
    a = int(a)
    b = int(b)
    c = a % b
    while c != 0:
        a = b
        b = c
        c = a % b
        q = a / b
        b = (a-c)/q
    print (b,"is the GCD")
        
euc(raw_input("a"),raw_input("b"))  




