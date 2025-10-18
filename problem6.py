n = "1233321" 

max_count = 0

for i in n:
    count = n.count(i)
    if count > max_count:
        max_count = count

print(max_count)