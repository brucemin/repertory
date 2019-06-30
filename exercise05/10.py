# 10． 由命令行输入一个4位整数，求将该数反转以后的数，如原数为1234，反转后的数位4321
Integer = int(input('输入一个四位整数:'))
a = int(Integer / 1000)
b = int((Integer - 1000 * a) / 100)
c = int((Integer - 1000 * a - 100 * b) / 10)
d = Integer% 10
print('%d%d%d%d'%(d,c,b,a))