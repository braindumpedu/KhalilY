import math

amount = int(raw_input('withdrawl amount'))

#100,50,20

availablebillsof100 = 1000
availablenotesof50 = 1000
availablebanknotesof20 = 1000

billsof100 = amount / 100
changefrom100 = amount % 100
billsof50 = changefrom100 / 50
changefrom50 = changefrom100 % 50
billsof20 = changefrom50 / 20
changefrom20 = changefrom50 % 20

paperof100 = amount / 100
backfrom100 = amount % 100
paperof20 = backfrom100 / 20
backfrom20 = backfrom100 % 20

notesof50 = amount / 50
leftfrom50 = amount % 50
notesof20 = leftfrom50 / 20
leftfrom20 = leftfrom50 % 20

notesof50minus1 = notesof50 - 1

banknotesof20 = amount / 20
leftoverfrom20 = amount % 20

if (billsof100 <= availablebillsof100) & (billsof50 <= availablenotesof50) & (billsof20 <= availablebanknotesof20) & (changefrom20 == 0):
    print(billsof100,"notes of 100", ",", billsof50, "notes of 50", ",", billsof20, "notes of 20")
elif (paperof100 <= availablebillsof100) & (paperof20 <= availablebanknotesof20) & (backfrom20 == 0):
    print(paperof100,"notes of 100",",",paperof20,"notes of 20")
elif (notesof50 <= availablenotesof50) & (notesof20 <= availablebanknotesof20) & (leftfrom20 == 0):
    print(notesof50,"notes of 50",",",notesof20,"notes of 20")
elif (banknotesof20 <= availablebanknotesof20) & (leftoverfrom20 == 0):
    print(banknotesof20,"notes of 20")
elif (notesof50minus1 <= availablenotesof50) & (3 <= availablebanknotesof20) & (leftfrom50 == 10):
    print(notesof50minus1,"notes of 50",",","3 notes of 20")                     
else:
    print("error")

