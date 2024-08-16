num1=int(input("please Enter The starting Number : "))
num2=int(input("please Enter The Ending Number : "))

value=0

for i in range(num1 , num2+1):
    value=value+i

print("The Sum Of Given Range Is : ",value)
