#4．有一个不多于5位的正整数，求它是几位数，分别打印出每一位数字。
Integer = int(input('请输入一个小于五位数的整数：'))
#判断正整数位数，并将其输出
if Integer < 10 and Integer>0:
    print('是一位数,%d'%Integer)
elif Integer <100 and Integer>0:
    a = int(Integer/10)
    b = Integer%10
    print('是两位数，%d %d'%(a,b))
elif Integer <1000 and Integer>0:
    a = int(Integer / 100)
    b = int((Integer - 100 * a) / 10)
    c = Integer % 10
    print('是三位数，%d %d %d' % (a, b,c))
elif Integer <10000 and Integer>0:
    a = int(Integer / 1000)
    b = int((Integer - 1000 * a) / 100)
    c = int((Integer - 1000 * a - 100 * b) / 10)
    d = Integer% 10
    print('是四位数，%d %d %d %d' % (a,b,c,d))
elif Integer <100000 and Integer>0:
    a = int(Integer / 10000)
    b = int((Integer - 10000 * a) / 1000)
    c = int((Integer - 10000 * a - b * 1000) / 100)
    d = int((Integer - 10000 * a - 1000 * b - 100 * c) / 10)
    e = Integer % 10
    print('是五位数，%d %d %d %d %d' % (a,b,c,d,e))
else:
    print('输入数不符合')