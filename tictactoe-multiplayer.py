main = ['1','2','3','4','5','6','7','8','9']

def dothex(m1):
    index = 0
    while m1 != main[index]:
        index = index + 1
    main[index] = "X"
    print(" --- --- ---")
    print "|", main[0] ,"|", main[1] ,"|", main[2] ,"|"
    print(" --- --- ---")
    print "|", main[3] ,"|", main[4] ,"|", main[5] ,"|"
    print(" --- --- ---")
    print "|", main[6] ,"|", main[7] ,"|", main[8] ,"|"
    print(" --- --- ---")

def dotheo(m2):
    index = 0
    while m2 != main[index]:
        index = index + 1
    main[index] = "O"
    print(" --- --- ---")
    print "|", main[0] ,"|", main[1] ,"|", main[2] ,"|"
    print(" --- --- ---")
    print "|", main[3] ,"|", main[4] ,"|", main[5] ,"|"
    print(" --- --- ---")
    print "|", main[6] ,"|", main[7] ,"|", main[8] ,"|"
    print(" --- --- ---")

def win():
    if main[0]+main[1]+main[2]=='X''X''X' or main[0]+main[3]+main[6]=='X''X''X' or main[0]+main[4]+main[8]=='X''X''X' or main[1]+main[4]+main[7]=='X''X''X' or main[3]+main[4]+main[5]=='X''X''X' or main[6]+main[7]+main[8]=='X''X''X' or main[2]+main[5]+main[8]=='X''X''X':
        print "Congratulations player 1! you won!" 
    elif main[0]+main[1]+main[2]=='O''O''O' or main[0]+main[3]+main[6]=='O''O''O' or main[0]+main[4]+main[8]=='O''O''O' or main[1]+main[4]+main[7]=='O''O''O' or main[3]+main[4]+main[5]=='O''O''O' or main[6]+main[7]+main[8]=='O''O''O' or main[2]+main[5]+main[8]=='O''O''O':
        print "Congratulations player 2! you won!"
    else: 
        m2 = str(input ("Player 2, Choose a position for your third Move"))
        dotheo(m2)
        win()


print(" --- --- ---")
print "|", 1 ,"|", 2 ,"|", 3 ,"|"
print(" --- --- ---")
print "|", 4 ,"|", 5 ,"|", 6 ,"|"
print(" --- --- ---")
print "|", 7 ,"|", 8 ,"|", 9 ,"|"
print(" --- --- ---")

m1 = str(input ("Player 1, Choose a position for your First Move"))  
dothex(m1)
m2 = str(input ("Player 2, Choose a position for your First Move"))
dotheo(m2) 
m1 = str(input ("Player 1, Choose a position for your Second Move"))   
dothex(m1)
m2 = str(input ("Player 2, Choose a position for your second Move"))
dotheo(m2)
m1 = str(input ("Player 1, Choose a position for your third Move"))    
dothex(m1)
win()
