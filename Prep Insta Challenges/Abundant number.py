n=int(input("Please Enter The Number : "))
sum=1

for i in range(2 , n):
    if n % i ==0:
        sum=sum+i   
if sum > n:
   print("Its Abundant number..!")
else:
    print("its Not Abundant number..!")
