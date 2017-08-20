name="zhang yiFeng"
print(name.title())#首字母大写
print(name.upper())#全部大写
print(name.lower())#全部小写

A="Zhang"
B="Yifeng"
C=A+" "+B
D=(A," ",B)
E="'happy birthday '"
print(C," ",D)



message="\tHello,"+C+"!"+"\n\tWe are family."+"\n\tAnd I'll tell you "+E.title()


print(message)



Margin=' 注意前后空白 '
print(Margin.rstrip(),".")#消除后面空白
print(Margin.lstrip(),".")#消除前面空白
print(Margin.strip(),".")#消除前后空白
