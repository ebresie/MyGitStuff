my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict)
prices={'apple':2.99, 'orange':1.99, 'milk':5.80}
print(prices)
d={'k1':123,'k2':[0,1,2], 'k3': {'insidekey':100}, 'key1':['a','b','c']}
print(d)
print(d['k3'])
print(d['k3']['insidekey'])
print(d['k2'][2])
print(d['key1'])
mylist = d['key1']
print(mylist)
letter = mylist[2]
print(letter)
print(d['key1'][2].upper())
d2 = {'k1':100, 'k2':200}
print(d2)
d2['k3']=300
print(d2)
d2['k1']='NEW VALUE'
print(d2)
print(d2.keys())
print(d2.values())