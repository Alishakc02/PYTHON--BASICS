#mini calculator using if else statement
a=input("enter the first number:")
print(a)
b=input("enter second number:")
print(b)
a=int(a)
b=int(b)
operator=input("enter the operstor(+,-,*,/,%)")
if operator == '+':
    print(a+b)
elif operator == '-':
    print(a-b)
elif operator == '*':
    print(a*b)
elif operator == '/':
    print(a/b)
elif operator == '%':
    print(a%b)
else:
    print("not available at the moment")
    
    