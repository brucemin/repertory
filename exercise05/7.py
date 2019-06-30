price = int(input('请输入汇率：'))
if price < 100:
    print('汇费为一元')
elif price < 5000:
    cost = price * 0.01
    print('汇费为%.2f'%cost)
else:
    print('汇费为50元')
    

