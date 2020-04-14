#coding=utf-8
dict = {"name":"zhangsan","age":19}
for i in dict:
    print('%s:%s' %(i,dict[i]))
print(dict)
dict['age']=12
print(dict)
dict['six']=1
print(dict)
del dict['age']
print(dict)
dict.clear()
print(dict)