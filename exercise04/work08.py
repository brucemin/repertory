#人口增长问题
a = 13
t = 0.8/100
count = 0
while 1:
    count += 1
    a = a * (1 + t)
    if a >= 26:
        break
print(count)
print(a)


