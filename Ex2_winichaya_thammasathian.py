def login():
    Username = input("Username:")
    Password = input("Password:")
    if Username == "wini" and Password == "1234":
        print("login Success")
        return ShowMenu()

    else:
        print("False")
        return login()

def ShowMenu():
    print("---------kuma--------------")
    print("1.vat calculator")
    print("2.price calculator")
    return Menuselect()

def Menuselect():
    UserSelected = int(input("menu:"))
    if UserSelected == 1:
        return print(vatcalculate(int(input("price:"))))
    elif UserSelected == 2:
        return print(pricecalculate())

def vatcalculate(totalprice):
    result =  totalprice + (totalprice * 7 / 100)
    return  result

def pricecalculate():
    price1 = int(input(" First product price:"))
    price2 = int(input(" Second product price:"))
    return vatcalculate(price1 + price2)

print(login())





