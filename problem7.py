
a = int(8)
b = int(12)

while b != 0:
    a, b = b, a % b 
    print(a,b)

print("GCD is:", a)


