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
res=[[x ** 2, x/2, x*2] for x in list(range(-6,7,2))]
print( res )