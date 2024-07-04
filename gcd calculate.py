

#gcd calculate

print('gcd calculate in python')
num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))

if num2>num1:
  mn=num1
else:
    mn=num2
    for i in range(1,mn+1):
        if(num1%i==0 and num2%i==0):
            gcd=i
            print("he gcd of thid twp number is {gcd}\n:")
