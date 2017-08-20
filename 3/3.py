# #3.1
# names=['zhang dongzhou','jiang miaoshan','zhang qiyang','zhang yifeng','zhang tong']
# def T(a):
#   return str(a.title())
# message=T(names[0])+"\tand\t"+T(names[-4])+"\tis\t"+T(names[2])+","+T(names[3])+"\tand\t"+T(names[-1])+"'s parents!"
# print("It is the most important that\n",message)


# #3.2[列表元素的添加,修改,删除(del,在删除这个元素后不在使用这个元素,则用del)]
# families=['zhang dongzhou','jiang miaoshan','zhang yi','sssss']
# del families[-1]#(可以尝试将此行代码-
# families[-1]='zhang yifeng'#-
# families.append('zhang tong')# -
# families.insert(2,'zhang qiyang')#-此行代码打乱顺序 会有什么变化)
# print(families)


#pop删除[如果在删除一个列表元素之后还要用到这个元素则用pop()删除].remove()删除也可以和pop一样再次使用已删除的元素
f=['a','b','c','d']
popped_f=f.pop(0)
popped_F=f.pop()#pop后括号中不添加数字默认最后一位
the_third_alphabet='c'
f.remove(the_third_alphabet)
print(f)#为什么可以直接输入f而下面不行?
print(popped_f)
print(popped_F)
print("The third alphabet is "+the_third_alphabet.upper()+".")
msg= 'sahdhsahdias{},dhasidhiaoshdioas{}dasdhasdhasi'.format(f[0],'0000')
print(msg)
message="The\tfirst\tEnglish\talphabet\tis\t"+popped_f+",\nthe\tsecond\talphabet\tis\t"+f[0]+",\nthe\tthird\tis\t"+popped_F+"."
# message=f+["."]#为什么不能直接用f?
print(message)
# print("The\tfirst\tEnglish\talphabet\tis\t"+popped_f+",\nthe\tsecond\talphabet\tis\t"+f+",\nthe\tfourth\tis\t"+popped_F+".")
#此处亦不行?


# #3.3


