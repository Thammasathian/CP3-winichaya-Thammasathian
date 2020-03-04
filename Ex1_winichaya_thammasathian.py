price = int(input("price:"))
def Vatcalculate(price):
    result = price+(price*7/100)
    return result
print(Vatcalculate(price))