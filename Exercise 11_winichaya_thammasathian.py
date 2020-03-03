number = int(input("Please Enter a number:"))
for i in range(number):
        print(" "*(number-i-1)+"*"*((i*2)+1))