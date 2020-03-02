Username = input("Username:")
Password = input("Password:")
if Username == "wini" and Password == "1234":
    print("Welcome KumaShop")
    print("--------Product List----------")
    print("1.Neutrogena : 186 THB")
    print("2.Vaseline   : 248 THB")
    print("3.Dettol     :  99 THB")
    print("------------------------------")
    UserSelected = int(input("Product>>"))
    print("------------------------------")
    if UserSelected == 1 :
        Product = int(input("Number of Product:"))
        ProductPrice = 186
        Result = Product*ProductPrice
        print("All product prices",Result,"THB")
    elif UserSelected == 2 :
        Product = int(input("Number of Product:"))
        ProductPrice = 248
        Result = Product*ProductPrice
        print("All product prices",Result,"THB")
    elif UserSelected == 3 :
        Product = int(input("Number of Product:"))
        ProductPrice = 99
        Result = Product*ProductPrice
        print("All product prices",Result,"THB")
else:
    print("Username or Password is wrong!")

