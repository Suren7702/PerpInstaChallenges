
def sum(n):
    sum=0
    for i in range(1 , n+1):
        sum=sum+i
    return sum

n=int(input("Please Enter The Number :"))
print(sum(n))