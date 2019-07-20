f = open('/Users/Umesh/python/project/data_basenew.txt', 'r')
d = {}
for line in f:
    name,password=line.strip().split('=')
    d[name.strip()]=password.strip()
f.close()
print(d)
