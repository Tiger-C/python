#第五集
# student={'name':'Tiger-C','age':19,'courses':['Math','CompSci']}#此行必开

# print(student['name'])#用中括号来输出一个元素
# print(student.get('name'))

# print(student.get('phone'))#若用这行代码来输出一个不存在的元素,则输出None
# # print(student['phone'])#若用此行代码来输出一个不存在的元素,则会显示出错
# print(student.get('name','Not Found'))
# print(student.get('phone','Not Found'))

# student['phone']='666-8888888' #添加了电话
# student['name']='Zhang Yifeng'#更改了姓名

# print(student)

# #用update来修改元素信息
# student.update({'name':'Zhang Yifeng','age':19,'courses':['Math','CompSci'],'phone':'666-8888888'})
 
# print(student)

# #用del删除元素(与pop和remove删除的不同详见3.py)
# del student['age']

# print(student)

# #理解但无法用中文表述...
# print(student.keys())
# print(student.values())
# print(student.items())

# for key in student:
#   print(key)

# for key,values in student.items():
#   print(key,values)

