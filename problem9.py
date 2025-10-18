n = int(input("Enter any number: "))
n_str = str(n)
length=len(n_str)
sum=0
for i in n_str:
    sum=sum + pow(int(i),int(length))

if sum==n:
    print(f"{n} is Armstrong Number")
else:
 print(f"{n} is not Armstrong Number")
   
    

