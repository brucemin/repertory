# 折纸上月球

n=0
sum=0.088
while(n<=1000):
    n += 1
    sum = 0.088 * 2 ** n
    if sum >= 363300000000:
        break
print(sum)
print(n)

