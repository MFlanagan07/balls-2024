print("which converter do you want to use?\nBinary Numbers to Decimal Numbers(1)\nDecimal Numbers to Binary Numbers(2)\nAdd two Binary Numbers(3)")
def binarytodecimal(binary):
    total = 0
    for index, x in enumerate(binary):
        expo = (len(binary)-index-1)
        num = int(x)
        if num == 1: 
            total += (2**expo)
    return total
def decimaltobinary(decimal):
    decimal = bin(decimal)
    num = decimal
    return num
a = int(input(""))
def binaryaddition(answer):
    number = (answer + answer)
    add = decimaltobinary(number)
    return(add)
if a == 1:
    bina = str(input("enter the binary number "))
    print(binarytodecimal(bina))
if a == 2:
    deci = int(input("enter the decimal number "))
    print(decimaltobinary(deci))
if a == 3:
    ans = int(input("enter the number "))
    ans2 = int(input("enter the second number "))
    num1 = ans+ans2
    print(binaryaddition(num1))
