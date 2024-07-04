from cgi import print_directory
from traceback import print_tb


print("+ addition")
print("- substraction")
print("* multiplication")
print("/ division")
num1=input("enter number 1:")
num2=input("enter number 2:")
opr=input("enter the operator:(+,-,*,/")
if opr=="+":
    print(num1,"+",num2,"=",(num1+num2))
elif opr=="-":
      print(num1,"-",num2,"=",(num1-num2))
elif opr=="*":
      print(num1,"*",num2,"=",(num1*num2))
elif opr=="/":
    if num2=="0":
        print("divide not happend")
print(num1,"/",num2,"=",(num1/num2))
    
else:
    print("invalid choice")