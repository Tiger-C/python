#coding=utf-8

courses=['History', 'Math', 'Physics', 'Compsci']

# import my_module #引用my_module模块(使用文件my_modul中的代码)

# index = my_module.find_index(courses,'Math')
# print(index)


# import my_module as mm  #将my_module简化为mm

# index = mm.find_index(courses,'Math') 
# print(index)


# from my_module import find_index   #寻找my_module模块中的find_index

# index =find_index(courses,'Math') 
# print(index)
                                    
# #如若想要运行my_modul中的test,则:     
# from my_module import find_index,test     

# index =find_index(courses,'Math') 
# print(index)
# print(test)                          

# #综合:
# from my_module import find_index as fi,test  #寻找my_module文件中的find_index和test并将find_index简化为fi   

# index =fi(courses,'Math') 
# print(index)
# print(test)    


# from my_module import find_index as fi,test
# import sys

# index =fi(courses,'Math') 

# print(sys.path)#用sys模块寻找my_module的脚本运行目录

#尝试着将my_module文件转移到c盘的TEST文件夹中并运行上面代码

#我们可以手动添加文件目录(记得将上面代码注释掉)
# import sys
# sys.path.append('/TEST/My_Module')

# from my_module import find_index as fi,test

# index =fi(courses,'Math') 

# print(sys.path)


# # 一些模块:

# import random

# random_course = random.choice(courses)

# print(random_course)

# import math

# rads = math.radians(90)#将数字转为弧度

# print(math.sin(rads))#sin90°=1 ?
# print(math.cos(rads))#???不应该等于0 ???

# import datetime

# today = datetime.date.today()
# print(today)

# import calendar#日历模块

# print(calendar.isleap(2020))#isleap(闰年)

# import os

# print(os.getcwd())
# print(os.__file__)



# import antigravity#这个可以打开一个网页