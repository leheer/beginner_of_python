#判断一个数是否是素数
flag = False
while True:
    try:
        a = int(input('输入一个整数'))
        if a > 1:
            break
        else:
            print('请输入大于1的整数')
    except ValueError:
        print("输入错误，请重新输入整数。")



for i in range(2,a):
    if a % i == 0:
        flag = True
        break
if flag:
    print('是合数')
else:
    print('是素数')