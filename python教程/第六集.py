#第六集
# #``````````````````start```````````````````
# if语言

# if True:
#   print('Conditional was True')

# if False:
#   print('Conditional was False')#这个将不会输出

# #`````````````````end````````````````````````````

#Comparisons:                  
#Equal:                ==
#Not Equal:            != 
#Greater Than:         >
#Less Than:            <
#Greater or Equal:     >=
#Less or Equal:        <=
#Object Identity:      is

# #````````````````````````````start```````````````````````
# language='Java'#此行在此模块必开

# if language == 'python':        #如果
#   print('Conditional was True')  
# elif language == 'Java':        #否则如果
#   print('Language is Java')
# elif language == 'C++':         #否则如果
#   print('Language is C++')
# else:                           #否则
#   print('No math')

# #````````````````````````````end````````````````````````

# #````````````````````````````start```````````````````````
# # 'and' 'or' 'not'语言
# #前三行在此模块必开
# user = 'Admin'
# logged_in = True #将True赋值给logged_in
# logged_out = False

# if user == 'Admin' and logged_in:  #这里用logged_in代替了True
#   print('Admin Page')
# else:
#   print('Bad Creds') 
# 
# if user == 'Admin' and logged_out: 
#   print('Admin Page')
# else:
#   print('Bad Creds') 

# if user == 'Admin' or logged_out: #or语言 两者有一个是对的则满足如果(可尝试改变两个变量)
#   print('Admin Page')
# else:
#   print('Bad Creds') 

# if not logged_in:           #not:如果不是xxx则输出xxxxx
#   print('Please Log In')
# else:
#   print('Welcome!')

# #For example:
# if not user=='Admin':
#   print('Sorry! You aren\'t Admin')
# else:
#   print('Hello! '+user+'.')
# #````````````````````````````end````````````````````````

# #````````````````````````````start```````````````````````

#  #'=='与'is'的区别
# a=[1,2,3]
# b=[1,2,3]

# print(a==b)
# print(a is b)
# #is输出'False的原因是a与b组成元素一样但是两者的id不一样,见下面
# print(id(a))
# print(id(b))

# #若将a赋值给b,则两者id相同
# b=a
# print(id(a))
# print(id(b))
# print(a is b)
# print(a==b)
# print(id(a)==id(b))

# #````````````````````````````end`````````````````````````


# #```````````````````````````start````````````````````````
# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example,'',(),[].
    # Any empty mapping. For example, {}.

condition=False #尝试改成True

if condition:
  print('Evaluated to True')
else:
  print('Evaluated to False')

condition=None

if condition:
  print('Evaluated to True')
else:
  print('Evaluated to False')

condition=0     #尝试改变数字

if condition:
  print('Evaluated to True')
else:
  print('Evaluated to False')

condition=()    #尝试成括号,中括号,大括号,以及双引号并在其中加入字符

if condition:
  print('Evaluated to True')
else:
  print('Evaluated to False')

# #````````````````````````````end`````````````````````````


