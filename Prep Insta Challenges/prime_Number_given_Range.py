start_num=int(input("please Enter The Starting Number : "))
end_num=int(input("please Enter The Ending  Number : "))
count=0
for i in range(start_num , end_num):
    for j in range(1 , i+1):
        if i%j==0:
            count=count+1
    if count==2:
        print(i)
    count=0