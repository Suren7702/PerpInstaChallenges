num=int(input("Enter The Starting Number : "))
l_num = int(input("Enter The Ending Number : "))
for i in range(num , l_num+1):
    pow = len(str(i))
    sum=0
    main_temp=i
    while main_temp > 0:
        digit=main_temp % 10
        sum += digit ** pow
        main_temp = main_temp // 10
    if(i==sum):
        print(i)
else :
    print("Not Find Any Amstrong Number you Entered range...!")