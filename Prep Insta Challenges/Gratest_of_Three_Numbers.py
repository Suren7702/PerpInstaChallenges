print("Please Enter The Three Number : ")
num1=int(input())
num2=int(input())
num3=int(input())
if(num1>=num2):
    if(num1>=num3):
        print("The Largest Number Is : ",num1)
elif(num2>=num3):
    print("The Largest Number Is : ",num2)
else :
    print("The Largest Number Is : ",num3)