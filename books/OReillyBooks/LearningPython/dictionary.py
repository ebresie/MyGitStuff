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
D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(D)
print(D.keys())
print(D.values())
print(D['food'])
# Fetch value of key 'food' 'Spam'
D['quantity'] += 1
print(D['quantity'])
# Add 1 to 'quantity' value D {'color': 'pink', 'food': 'Spam', 'quantity': 5}

D = {}
# Create keys by assignment
D['name'] = 'Bob'
D['job'] = 'dev'
D['age'] = 40
print(D) # {'age': 40, 'job': 'dev', 'name': 'Bob'}
print(D['name'])
# usage of dict to make dictionary
bob1 = dict(name='Bob', job='dev',age=40)
# Keywords
print(bob1)
# {'age': 40, 'name': 'Bob', 'job': 'dev'}
bob2 = dict(zip(['name', 'job', 'age'],['Bob', 'dev', 40]))
# Zipping
print(bob2) # {'job': 'dev', 'name': 'Bob', 'age': 40}
rec = {'name': {'first': 'Bob', 'last': 'Smith'},'jobs':['dev','mgr'],'age': 40.5}
print(rec) 
D = {'a': 1, 'b': 2, 'c': 3}
# D {'a': 1, 'c': 3, 'b': 2}
D['e'] = 99
# Assigning new keys grows dictionaries
print(D)
# {'a': 1, 'c': 3, 'b': 2, 'e': 99}
if not 'f' in D:
    print("missing")
    print("still")
value = D.get('x', 0)
# Index but with a default
print(value) # 0
value = D['x'] if 'x' in D else 0
# if/else expression
print(value) # 0
D = {'a': 1, 'b': 2, 'c': 3}
print("D = {'a': 1, 'b': 2, 'c': 3}")
print(D)
# {'a': 1, 'c': 3, 'b': 2}
Ks = list(D.keys())
# Unordered keys list
print(Ks)
# A list in 2.X, "view" in 3.X: use list() ['a', 'c', 'b']
Ks.sort()
# Sorted keys list
print(Ks)
for key in Ks:
    # Iterate though sorted keys
    print(key, '=>', D[key])
    # <== press Enter twice here (3.X print)
for key in sorted(D):
    print(key, '=>', D[key])
    
for c in 'spam':
    print(c.upper())
x = 4
while x > 0:
    print('spam!' * x)
    x -= 1
