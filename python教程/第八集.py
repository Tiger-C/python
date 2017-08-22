#第八集

#函数

# def hello_func():   #定义一个函数'hello_func()'
#   pass                 #此函数的内容忽略

# print(hello_func) 
# print(hello_func())

# def hello_func():    #定义一个函数'hello_func()'
#   print('Hello Function!')   #此函数的内容是"print('Hello Function.') "
                            
# hello_func()       #输出此函数 #法1
# print('Hello Function!')      #法2

#如果我们在输出多次'Hello Function!'后要修改输出内容,用法1则只需在函数内容修改,用法2则需一个一个修改
#For example:
#将输出修改成'Hello Funtion.'

# def hello_func():   
#   print('Hello Function!') 

# hello_func()      
# hello_func()      
# hello_func()

# print('Hello Function!')  
# print('Hello Function!')  
# print('Hello Function!')  

#return与print的区别:

# def hello_func():   
#   return'Hello Function!.'

# hello_func()       #无法输出
# print(hello_func())
# # print(hello_func().upper())

# def hello_func(greeting):   
#   return'{} Fuction.'.format(greeting)

# print(hello_func('Hi'))

# def hello_func(greeting,name='You'):   
#   return'{},{}.'.format(greeting,name)

# print(hello_func('Hi'))
# print(hello_func('Hi',name='Zhang'))
# print(hello_func('Hi','Guy'))


# def student_info(*args,**kwargs):
#   print(args)
#   print(kwargs)

# courses=['Math','Art']
# info={'name': 'John', 'age': 22}

# student_info(courses,info)  
# student_info(*courses,**info) 


#Number of days per month.First value placeholder for indexing purposes.
#每月的天数。第一个值占位符用于索引。
month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

#一个计算年份是否为闰年的函数
def is_leap(year):
#闰年则返回真实的，非闰年则返回错误的。  
  """Return True for leap years, False for non-leap years.""" 

#这是一个闰年的计算方法,不同地方,国家有不同的算法,中国只有and前面那一些
  return year % 4 ==0 and (year % 100 != 0 or year %400 == 0)

print(is_leap(2017))
print(is_leap(2020))


#一个计算某年某月的天数的函数
def days_in_month(year,month):
#将天数返回给给那个月以及那年  
  """Return number of days in that month in that year."""
  
  if not 1 <= month <=12:#这行代码是筛选出非1-12的月份
    return 'Invalid Month'#并将它们输出为无效月份

  if month ==2 and is_leap(year):#这行代码则是找到闰年的二月
    return 29                   #并输出29天

  return month_days[month]  #相当于month_days[1](列表month_days的第二个值)

print(days_in_month(2017,2))
print(days_in_month(2020,2))
