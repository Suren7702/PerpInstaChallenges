st_num=int(input("Please Enter The NUmber : "))
first=0
second=1
for i in range(st_num):
  print(first)
  temp = first
  first=second
  second=temp+second
print(second)