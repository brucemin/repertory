# 8． 分别使用for循环，while循环求1到100之间所有能被3整除的整数的和。
#while循环
count = 1
sum = 0
while count < 100:
    count += 1
    sum = sum + count
print('整数的和为%d' % sum)

# print('整数的和为%d'%sum)
#for循环
count = 1
sum = 0
for count in range(1,100):
    if count % 3 == 0:
        sum = sum + count
print('整数的和为%d'%sum)