menu = [['iphone',6888],['三星',3000],['小米',2500]]
print(menu[1])
shop_car = []
flag = True
while flag:
    print('******商品列表******')
    for index,i in enumerate(menu):
        print('%s. %s|%s'%(index,i[0],i[1]))
    j= input('输入：')

    if j.isdigit():
        j = int(j)
        if j>=0 and j< len(menu):
            if menu[j] not in shop_car:
                shop_car.append(menu[j])
            else:
                print('您已购买此产品')
        else:
            print('该商品不存在')
    elif j == 'q':
        if len(shop_car)>0:
            # print('已购买%s'%shop_car)
            print('您已购买以下产品')
            for index,i in enumerate(shop_car):
                print('%s. %s|%s'%(index,i[0],i[1]))

        else:
            print('购物车为空')
        flag = False
