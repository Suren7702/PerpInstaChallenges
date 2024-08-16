no=int(input("Please Enter The Number :"))
perfect=0
i=1
while i<no :
    if no%i==0:
     perfect+=i
    i+=1
if no==perfect:
  print(f"The {no} Number Is Perfect Number..!")
else:
  print(f"The {no} NUmber Is Not perfect Number..!")
