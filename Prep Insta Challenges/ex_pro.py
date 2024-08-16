#sum  of Number

num=int(input("Enter The Number : "))

reverse=0

while num > 0:
    digit = num % 10
    reverse = reverse + digit
    num = num//10
print(reverse)