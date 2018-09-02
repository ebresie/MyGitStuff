L=[123, 'spam',1.23];
print(L);
print('len=',len(L))
# Indexing by position 123 
L[0]
# Slicing a list returns a new list [123, 'spam'           
L[:-1]                           

# Concat/repeat make new lists too [123, 'spam', 1.23, 4, 5, 6]
L + [4, 5, 6]

L * 2