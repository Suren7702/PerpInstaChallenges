def factorial(value):
    result=1
    while value > 0 :
        result *= value
        value -= 1
    return result

number=int(input())

sum=0

n=number

while n > 0:
    sum +=factorial( int(n % 10) )
    n= int(n/10)


isStrong = number == sum

print(f"The Number{number} is a Strong Number? {isStrong}")