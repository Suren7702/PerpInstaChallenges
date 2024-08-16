
n=int(input("Please Enter The Nummber : "))
number=n
sum=0
while n > 0 :
    digit=n%10
    sum=sum+digit
    n=n//10
if number%sum==0:
    print("Yes its Harshed_Number..!")
else:
    print("NO its Not Harshed_Number...!!!")

