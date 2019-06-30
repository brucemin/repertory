profit = float(input('请输入当月利润(单位/万)：'))
if profit <= 10:
    reward = profit/10
    print('奖金 %f万'%reward)
elif profit <= 20:
    reward =10/10 + (profit-10)*0.075
    print('应发放奖金 %.3f万'%reward)
elif profit <= 40:
    reward = 10/10 + 10*0.075+(profit-20)*0.005
    print('应发放奖金 %.3f万'%reward)
elif profit <= 60:
    reward = 10/10 + 10*0.075+20*0.005+(profit-40)*0.003
    print('应发放奖金 %.3f万'%reward)
elif profit <= 100:
    reward = 10/10 + 10*0.075+20*0.005+40*0.003+(profit-60)*0.0015
    print('应发放奖金 %.3f万'%reward)
else:
    reward = 10/10+10*0.075+20*0.005+20*0.003+40*0.0015+(profit-100)*0.001
    print('应发放奖金 %.3f万' % reward)