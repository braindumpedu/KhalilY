import math

amount = int(raw_input('withdrawl amount'))

#100,50,20

billsof100 = amount / 100
changefrom100 = amount % 100
billsof50 = changefrom100 / 50
changefrom50 = changefrom100 % 50
billsof20 = changefrom50 / 20
changefrom20 = changefrom50 % 20

notesof50 = amount / 50
leftfrom50 = amount % 50
notesof20 = leftfrom50 / 20
leftfrom20 = leftfrom50 % 20

banknotesof20 = amount / 20
leftoverfrom20 = amount % 20

#print billsof100
#print changefrom100
#print billsof50
#print changefrom50
#print billsof20
#print changefrom20

#print notesof50
#print leftfrom50
#print notesof20
#print leftfrom20

#print banknotesof20
#print leftoverfrom20

if changefrom20 == 0:
    print(billsof100,"notes of 100", ",", billsof50, "notes of 50", ",", billsof20, "notes of 20")
elif leftfrom20 == 0:
    print(notesof50,"notes of 50",",",notesof20,"notes of 20")
elif leftoverfrom20 == 0:
    print(banknotesof20,"notes of 20")
else:
    print("error")



