
a = int(8)
b = int(12)

while b != 0:
    a, b = b, a % b 
    print(a,b)

print("GCD is:", a)

s1=10
s2=20
s1 , s2 =s2 ,s1
print(s1)
print(s2)