#第四集(包含部分文件3.py和部分第二集)
# courses=['History','Math','Physics','Compsci']#此行代码在Mutable之前都要打开
# print(courses)

# courses.append('Art')#在最后添加一个元素
# courses.insert(0,'English')#在0的位置添加一个元素

# courses_2=['Chinese','Education']
# courses.insert(1,courses_2)#看看这条代码与下面两条代码有什么不同
# courses.append(courses_2)
# courses.extend(courses_2)

# #用pop删除和用remove删除可以详见3.py
# # courses.remove('Math')#删除一个元素
# popped=courses.pop()#删除一个元素并将该元素赋值给popped (括号内无数字则默认最后一个)
# print(popped)#输出被删除的元素

# courses.reverse()#将元素倒叙

# courses.sort()#排序 按开头字母的顺序 数字排在字母前
# print(courses)
# courses.sort(reverse=True)#按顺序倒叙(若=False则无效)
# print(courses)
# sorted_courses=sorted(courses)
# print(sorted_courses)

# alphabet=['DA1','SA2','AD3','3AD']
# alphabet.sort()
# print(alphabet)

# nums=[3,5,1,4,2]
# nums.sort()
# print(nums)
# print(min(nums))#输出最小数
# print(max(nums))#输出最大数
# print(sum(nums))#输出总和


# #中文不知道是什么规则
# Chinese=['啊了','吧即','啦']
# Chinese.sort()
# print(Chinese)

# print(courses.index('Math'))#查找某元素在列表中的位置
# print('Art' in courses)#True则表示该元素存在于列表,False则是不存在

#for和in语言
# for item in courses:  #将courses中的元素一个一个输出
#   print(item)

# #输出元素位置和元素
# for course in enumerate(courses):     
#   print(course)                  

# for index,course in enumerate(courses):
#   print(index,course)

# for index,course in enumerate(courses,start=1):
#   print(index,course)

# courses_str=' - '.join(courses)#将' - '插入courses中输出

# new_list=courses_str.split(' - ')#将' - '从courses_str中删除

# print(courses_str) 
# print(new_list)


# #Mutable  (可变的)
# list_1=['History','Math','Physics','Compsci']
# list_2=list_1

# print(list_1)
# print(list_2)

# list_1[0]='Art'

# print(list_1)
# print(list_2)

# #Immutable   (不可变的)(这里很神奇,视频上不可以但是我可以)
# tuple_1=['History','Math','Physics','Compsci']
# tuple_2=tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0]='Art'

# print(tuple_1)
# print(tuple_2)


# #Sets
# cs_courses={'History', 'Math', 'Physics', 'Compsci','Math'}#用大括号则会将两个相同的元素只输出前一个
# art_courses={'History', 'Math', 'Art', 'Design'}
# print(cs_courses)
# print(cs_courses.intersection(art_courses))#输出两个列表中相同的元素
# print(cs_courses.difference(art_courses))#输出两个列表中不相同的元素
# print(cs_courses.union(art_courses))#将两个列表合并(每次运行顺序都不同)

#Empty Lists
empty_list=[]
empty_list=list()

#Empty Tuples
empty_tuple=()
empty_tuple=tuple()

#Empty Sets
empty_set={}    #错误的
empty_set=set()
