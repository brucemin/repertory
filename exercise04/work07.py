#篮球弹跳高度运算

h = int(input('请输入球的初始高度：'))
count = 1
#篮球经过总路程s,最后一次弹跳高度h
while 1:
    count = count + 1
    if count >1:
        s = 3*h*(1-(1/2)**count)
        h =h*(1/2)**count
        break
print(s)
print(h)



