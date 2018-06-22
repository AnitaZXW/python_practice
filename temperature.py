# TempConvert.py
Tempstr = input("请输入带有符号的温度值:")
if Tempstr[-1] in ['f','F']:
	c = (eval(Tempstr[0:-1])-32)/1.8
	print("转换后的温度是{:.2f}c".format(c))
elif Tempstr[-1] in ['c','C']:
	f = 1.8 * eval(Tempstr[0:-1]) + 32
	print("转换后的温度是{:.2f}f".format(f))
else:
	print("输入错误")