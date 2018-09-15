L=[123, 'spam',1.23];
print(L);
print('len=',len(L))
# Indexing by position 123 
print(L[0])
# Slicing a list returns a new list [123, 'spam']
print(L[:-1])

# Concat/repeat make new lists too [123, 'spam', 1.23, 4, 5, 6]
print(L + [4, 5, 6])

print(L * 2)
L.append('NI')
print(L)
# additional list operators
L.insert(123,1)
print('insert=',L)
L.remove(1)
print('remove=',L)
L.extend( [3] )
print('extend=',L)
print('before reverse=',L)
L.reverse()
print('reverse=',L)
N=[1,5,4,2,100,2,3]
N.sort()
print('sort=',N)
print('before reverse=',N)
N.reverse()
print('reverse=',N)

# Matrix lists
M=[[1,2,3],[4,5,6],[7,8,9]]
print(M)
print(M[1])