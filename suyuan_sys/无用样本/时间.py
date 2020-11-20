import time
import datetime

# t=int(time.time()) #秒级时间戳
# now=time.strftime("%Y%m%d%H%M%S",time.localtime(t))
# print(now)
li1=[]

li=[54,56,89,36]
li.insert(0,'"')
li.append('"')
print(li)
for i in li:


    li1.append(str(i))
s="_".join(li1)

print('"'+s+'"')


