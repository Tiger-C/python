#python教程第二集(一个一个运行)
message="Hello everybody."
print(len(message))# 显示元素有多少个字母组成
print(message[15])#从0开始一共有16个字母,最后一个是第15个
print(message[0:7])#输出从第0个字母到第7个字母
print(message[8:7])#无法输出
print(message[:9])#默认输出从0到9的字母
print(message[4:])#默认输出从4到最后一个字母
print(message.count('l'))#l出现过几次
print(message.count('hello'))#hello不存在即为0次
print(message.find('eve'))#eve从第几个开始出现
print(message.find('evebsdaod'))#-1即为can't find it
msg=message.replace('everybody','guys')#替换,也可以用另一种修改见'3.py'
print(msg)

A='Hello'
B='zhang yifeng'
message='{}, {}.Welcome!'.format(A,B.title())
print(message)
message='{A}, {B}.Welcome!'
print(message)
message=f'{A}, {B.title()}.Welcome!'
print(message)
print(dir(B))#列出B可以用的公式
print(help(str))#是告诉你有哪些方程.
print(help(str.lower))#告诉你某个方程的用途