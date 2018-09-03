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