Number = int(input('请输入一个三位数：'))
#输出每一位上的数
a = int(Number/100)
b = int((Number-100*a)//10)
c = int(Number%10)
#判断a，b，c大小,并按从大到小排列,再从小到大排列
if a>b and a>c and b>c:
    print(str(a) + str(b) + str(c))
    print(str(c) + str(b) + str(a))
elif a>b and a>c and c>b:
    print(str(a) +str(c) +str(b))
    print(str(b) + str(c) + str(a))
elif b>a and b>c and a>c:
    print(str(b)  + str(a) + str(c))
    print(str(c) + str(a) + str(b))
elif b>a and b>c and c>a:
    print(str(b)+ str(c) + str(a))
    print(str(a) + str(c) + str(b))
elif c>a and c>b and a>b:
    print(str(c) + str(a) + str(b))
    print(str(b) + str(a) + str(c))
else:
    print(str(c)+ str(b) + str(a))
    print(str(a)+ str(b) + str(c))
