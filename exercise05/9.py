# 9． 编写一个程序，找出大于200的最小的质数
num = 200
while 1:
    num = num+1
    for j in range(2,num):
        if num%j ==0:
            print(end ='')
    else:
        print('最小质数为%d'%num)
        break
