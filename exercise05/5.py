# 5．假设某员工今年的年薪是30000元，年薪的年增长率6%。编写一个Java应用程序计算该员工10年后的年薪，并统计未来10年（从今年算起）总收入。
salary = 30000
rate = 0.06
count = 0
fund = 0
while 1:
    count = count +1
    salary = salary * (1+rate)
    fund = fund +salary
    if count >= 10:

        break
print('10年后的年薪%d元'%salary)
print('总收入为%d元'%fund)
