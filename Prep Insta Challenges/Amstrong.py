num = int(input("Please Enter The Number : "))
sum = 0
temp = num
main_temp=str(temp)
while(num > 0):
    digit = num % 10 
    sum += digit**len(main_temp)
    num =num// 10
if(sum == temp):
    print("This is Amsrong Number...!")
else :
    print("this is Not Amstrong Number...!")