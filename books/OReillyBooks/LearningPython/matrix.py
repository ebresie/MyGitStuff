# Matrix lists
M=[[1,2,3],[4,5,6],[7,8,9]]
print(M)
print(M[1])
print([row[1] for row in M])
print([row[1] for row in M if row[1] % 2 ==0])
diag = [M[i][i] for i in  [0,1,2]]
# Collect a diagonal from matrix >>> diag [1, 5, 9]
print(diag)
doubles = [c * 2 for c in 'spam']
# Repeat characters in a string
print(doubles)
# Multiple values, "if" filters [[0, 0], [1, 1], [4, 8], [9, 27]
print([[x ** 2, x ** 3] for x in range(4)])
#[[2, 1, 4], [4, 2, 8], [6, 3, 12]]
#res= [[x， x / 2， x * 2] for x in range( -6，7，2 ) if x > 0 ]
res=[[x ** 2, x/2, x*2] for x in list(range(-6,7,2)) if x>0]
print( res)
# generator examples
G = (sum(row) for row in M)
print(G)
# Create a generator of row sums
print(next(G))
# iter(G) not required here 6
print(next(G))
# Run the iteration protocol next() 15
print(next(G))
print(list(map(sum, M)))
# set examples
print({sum(row) for row in M})
# Create a set of row sums {24, 6, 15}

# map/dictionary examples
res={i : sum(M[i]) for i in range(3)}
# Creates key/value table of row sums {0: 6, 1: 15, 2: 24}
print(res)
# List of character ordinals [115, 112, 97, 97, 109]
print([ord(x) for x in 'spaam'])
# Sets remove duplicates {112, 97, 115, 109}
print({ord(x) for x in 'spaam'})
 # Dictionary keys are unique {'p': 112, 'a': 97, 's': 115, 'm': 109}
print({x: ord(x) for x in 'spaam'})
# Generator of values <generator object <genexpr> at 0x000000000254DAB0> To understand objects like
print((ord(x) for x in 'spaam'))
