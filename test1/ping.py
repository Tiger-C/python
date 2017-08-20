# 引入os模块
import os
# 引入时间模块
import time

website = ["192.168.31.1","www.163.com","www.baidu.com","www.taobao.com","192.168.2.11","192.168.1.135"]

def pingWebsite(websites):
  for website in websites :
    start = time.time()
    response = os.system("ping -c 1 " + website)
    duration = time.time() - start
    print( "我们正在ping:", website,"耗时:",ms(duration),'\n')

def ms(a):
  return str(round(a * 1000,1)) + " 毫秒"

pingWebsite(website)

