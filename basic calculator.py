#assignment 1
print("....calculator............")
print("+ addition ")
print("- subtraction ")
print("* multiplication ")
print("/ division")

choice=input("enter your choice:")
num1=int(input("enter number 1:" ))
num2=int(input("enter number 2:" ))
if (choice=="+"):
   print(num1,"+",num2,"=",(num1+num2))
elif (choice=="-"):
   print(num1,"+",num2,"=",(num1- num2))

elif (choice=="*"):
    print(num1,"*",num2,"=",(num1*num2))
elif (choice=="/"):
   if(num2==0):
      print("division not posible")
   else:
      print(num1,"/",num,"=",(num1/num2))
else:
      print("invalid input")

'''output 1:
....calculator............
+ addition 
- subtraction 
* multiplication 
/ division
enter your choice:+
enter number 1:4
enter number 2:4
4 + 4 = 8


output 2:
....calculator............
+ addition 
- subtraction 
* multiplication 
/ division
enter your choice:-
enter number 1:65
enter number 2:32
65 - 32 = 33

output 3:
....calculator............
+ addition 
- subtraction 
* multiplication 
/ division
enter your choice:*
enter number 1:32
enter number 2:9
32 * 9 = 288
output 4:
....calculator............
+ addition 
- subtraction 
* multiplication 
/ division
enter your choice:/
enter number 1:21
enter number 2:3
21 / 3 = 7.0'''

