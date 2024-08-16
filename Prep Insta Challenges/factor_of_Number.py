num = int(input("Please Enter The Number : "))
count=0
for i in range(1 , num+1):
    if num % i ==0:
        print(i)
        count=count+1
if(count==2):
    print("The Given Number Is prime ! ")
else:
    print("The Given NUmber Is Not Prime !")