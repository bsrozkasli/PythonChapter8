from time import *
print("{0}\n,{1}\n,{2}".format(gmtime(1),localtime(),time()))
time_here=localtime()
print(f"Year:{time_here[0]},{time_here.tm_year}")
print(f"Month:{time_here[1]},{time_here.tm_mon}")
print(f"Year:{time_here[2]},{time_here.tm_mday}")