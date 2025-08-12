print("Arithmetic Calculator")
print("-----------------------------------------------------------")
print("Operator Description")
print("+   Addition")
print("-   Subtraction")
print("*   Multiplication")
print("/   Division")
print("%   Modulo")
print("^   Power of")
print()
a=int(input("Enter 1st Number:"))
b=int(input("Enter 2nd Number:"))
while(True):
    op=input("Enter the operator of your choice:")
    if a==0:
        print("Invalid number")
        exit()
    else:
        if op=='+':
            res=a+b
        if op=='-':
            res=a-b
        if op=='*':
            res=a*b
        if op=='/':
            res=a/b
        if op=='%':
            res=a%b
        if op=='^':
            res=a^b
        print("Result of the Arithmetic operation=",res)
    ch=input("Do you want to repeat [Y/N]?:")
    if ch=='Y':
        continue
    else:
        break
print("-----------------------------------------------------------")
