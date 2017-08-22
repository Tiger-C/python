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
import sys
sys.path.append('/TEST/My_Module')

from my_module import find_index as fi,test

index =fi(courses,'Math') 

print(sys.path)