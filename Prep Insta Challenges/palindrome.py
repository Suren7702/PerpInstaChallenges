num = int(input("Please Enter The Number : "))
main_num=num
reverse = 0 
while(num > 0 ):
    digit = num % 10
    reverse = reverse * 10 +digit
    num = num//10

if(main_num == reverse):
    print("This is Palindrome Number !..")
else:
    print("This is Not Palindorme Number !..")