import datetime
now=datetime.datetime.now()
date=str(now)
item=input("Enter the name of Item : ")
qty=int(input("Enter the quantity : "))
price=int(input("Enter the price of "+ item+ ": "))
val=qty*price
tax=5/100*val
net=val+tax
print("="*65)
print("\t\t\tINVOICE")
print("-"*65)
print("Date : {a:>55s}".format(a=date))
print("="*65)
print("Item", " "*10, "QTY", " "*10, "Unit Price", " "*10, "Net Total")
print("="*65)
print("{0:<14s}{1:>4d}{2:>20d}{3:>20d}".format(item, qty, price, val))
print("Tax {0:>55.2f}".format(tax))
print("="*65)
print("Amount Payable ", " "*38, net)
print("="*65)
