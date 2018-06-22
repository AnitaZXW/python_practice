# # TempConvert.py
Tempstr = input("请输入带有符号的温度值:")
if Tempstr[-1] in ['f','F']:
	c = (eval(Tempstr[0:-1])-32)/1.8
	print("转换后的温度是{:.2f}c".format(c))
elif Tempstr[-1] in ['c','C']:
	f = 1.8 * eval(Tempstr[0:-1]) + 32
	print("转换后的温度是{:.2f}f".format(f))
else:
	print("输入错误")

Tempstr = input()
if Tempstr[0:3] == "RMB":
	c = (eval(Tempstr[3:]))/6.78
	print("USD{:.2f}".format(c))
elif Tempstr[0:3] == "USD":
	f = 6.78 * eval(Tempstr[3:])
	print("RMB{:.2f}".format(f))
else:
	print("输入错误")


a = input()
a = eval(a)
print(a ** 0, a ** 1, a ** 2, a ** 3, a ** 4, a ** 5)