import math
def sum(n):
    sum=0
    for i in range(1 , n+1):
      sum=sum+pow(n , 2)
    return sum

n=int(input("Please Enter The Number : "))
print(sum(n))
