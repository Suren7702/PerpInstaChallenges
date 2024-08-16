import math

def prfect_Squre(n):
    if math.ceil(math.sqrt(n))==math.floor(math.sqrt(n)):
        print("True")
    else:
        print("False")

n=49
prfect_Squre(n)

print(math.ceil(math.sqrt(n)))