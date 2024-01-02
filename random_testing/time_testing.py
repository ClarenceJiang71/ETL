import time 

print(time.time())
print(time.localtime(time.time()))
print(type(time.localtime(time.time())))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

print(time.strptime("2023-12-12 11:51:21", "%Y-%m-%d %H:%M:%S"))