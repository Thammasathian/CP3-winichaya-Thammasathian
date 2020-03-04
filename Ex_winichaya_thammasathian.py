x = int(input("number:"))
y = int(input("number:"))
def AddNumber(x,y):
    total = x + y
    total1 = x - y
    total2 = x * y
    total3 = x / y
    print("%d"%x,"+","%d"%y,"=",total)
    print("%d"%x,"-","%d"%y,"=",total1)
    print("%d"%x,"*","%d"%y,"=",total2)
    print("%d"%x,"/","%d"%y,"=",total3)

AddNumber(x,y)