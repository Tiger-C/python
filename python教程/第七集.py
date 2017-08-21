#第七集

# #``````````````````````start`````````````````````````````````````

# nums=[1,2,3,4,5]#此行必开

# for num in nums:
#   if num == 3:
#     print('Found!')
#     break     #停止
#   print(num)

# for num in nums:
#   if num == 3:
#     print('Found!')
#     continue     #继续
#   print(num)

# for num in nums:
#   for letter in 'abc':
#     print(num,letter)
  
# #``````````````````````end```````````````````````

# #``````````````````````start`````````````````````
# for i in range(10): #range(范围)从0开始到10之前
#   print(i)

# for i in range(1,10): #从1开始到10之前
#   print(i)

x=0#此行必开

# while x<10:
#   print(x)
#   x +=1     #赋予了一个循环让x不断加一并返回上面运行直到无法输出

# while x<10:
#   if x==5:
#     break
#   print(x)
#   x+=1

while True:
  # if x == 5:  #尝试将这行代码和break删除
  #   break     #(做好编辑器卡住的准备!)
  print(x)
  x += 1
                

#以下代码有毒 运行后编辑器卡住,估计是因为他会无限重复下去,同上(这是我自己尝试创造的代码)
# while x<15:     
#   for x in range(3,11):
#     print(x)
#   x+=1

# #``````````````````````end```````````````````````
