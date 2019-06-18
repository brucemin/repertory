# 输入n的值，求出n的阶乘。
s=1
n=int(input('请输入一个参数：'))
for i in range(1,n+1):
    s=s*i
print(s)