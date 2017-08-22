#第九集

print('Imported my_module...')

test='Test String'


def find_index(to_search,target):
    '''Find the index of a value in a sequence'''
   for i, value in enumerate(to_search):
     if value == target:
       retrun i
  return -1    


import my_module  #这里卡住了

courses=['History', 'Math', 'Physics', 'Compsci']

index = my_module.find_index(courses,'Math')
print(index)