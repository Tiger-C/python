#第三集
num=3.14
print(type(num))#type告诉你数字的类型(int-整数,float-浮点数(即带小数点的数))

# 算术运算(不能运行)
# Arithmetic Operators:
# Addition:           3+2  加
# Subtraction:        3-2  减  
# Multiplication:     3*2  乘
# Division:           3/2  除
# Floor Division:     3//2 除取整数位(不是四舍五入)
# Exponent:           3**2 次方
# Modulus:            3%2  取余数
# print(3+2*2)
# print((3+2)*2)

num=3
num=num**2
print(num)

num=3
num **=2#相当于num=num**2
print(num)

print(abs(-10))#将负数变正
print(round(3.75))#四舍五入(默认至整数位)
print(round(3.1415926,3))#四舍五入到第3位小数

#数字比较(不能运行)
#Comparisons:                  
#Equal:                3==2    (等于)
#Not Equal:            3!=2    (不等于)
#Greater Than:         3>2     (大于)
#Less Than:            3<2     (小于)
#Greater or Equal:     3>=2    (大于等于)
#Less or Equal:        3<=2    (小于等于)

num_1=3
num_2=2
print(num_1==num_2)#输出True即为正确,False即为错误
print(num_1*num_2==num_1*2)

num_1='100'
num_2='200'
print(num_1+num_2)
num_1=int(num_1)
num_2=int(num_2)
print(num_1+num_2)