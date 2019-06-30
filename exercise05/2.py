# 随机数能否被5或6整除
import random
min = input('请输入最小值：')
max = input('请输入最大值：')
randNum = random.randint(int(min),int(max))
print(randNum)
if randNum/5 == 0:
    print('能被5整除')
elif randNum/6 == 0:
    print('能被6整除')
elif randNum/5 == 0 and randNum/6 == 0:
    print('能被5和6整除')
else:
    print('不能被5和6整除')
