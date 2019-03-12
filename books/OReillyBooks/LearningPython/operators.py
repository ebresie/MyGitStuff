# Operators examples 
#Generator function send protocol 
yield x

# Anonymous function generation 
lambda args: expression

#Ternary selection (x is evaluated only if y is true) 
print(x if y else z)

# Logical OR (y is evaluated only if x is false)
print(x or y)

#Logical AND (y is evaluated only if x is true) 
print(x and y )

#Logical negation 
print(not x )

#Membership (iterables, sets) 
print(x in y)
print(x not in y )

#Object identity tests
print(x is y)
print(x is not y)

#Magnitude comparison, set subset and superset;Value equality operators 
print(x < y)
print(x <= y)
print(x > y)
print(x >= y)
print(x == y)
print(x != y)

#Bitwise OR, set union
print(x | y)

#Bitwise XOR, set symmetric difference 
print(x ^ y)

#Bitwise AND, set intersection 
print(x & y )

#Shift x left or right by y bits 
print(x << y)
print(x >> y )

#Addition, concatenation; Subtraction, set difference 
print(x + y )
print(x -y )

#Multiplication, repetition;  
print(x * y )
# Remainder, format;
print(x % y )

# Division: true and floor 
# - expression performs true division in 3.X (retaining remainders) and classic division in 2.X (truncating for integers).
print(x / y)
# - floor division expression always truncates fractional remainders in both Python 2.X and 3.X.
print(x // y )

#Negation, identity 
print(-x )
print(+x )

#Bitwise NOT (inversion) 
print(~x)

#Power (exponentiation)
print(x ** y)

#Indexing (sequence, mapping, others) 
x='0123456789abcdefg'
i=10
print(x[i] )
 
 #Slicing
i=2
j=3
k=2
print(x[i:j:k]  )
 
 #Call (function, method, class, other callable)
x={print('hello function')}
x()
# x(...)  
 
 #Attribute reference
x.attr=123
print(x.attr)
 
 #Tuple, expression, generator expression
# (...)
#('a'，'b'，'c')
(...)
 
 #List, list comprehension 
# [...] 
#[a，b, c]
[...]
 
 #Dictionary, set, set and dictionary comprehensions
# {...} 
{ 'a1':'1'，'b2':'2'，'c3':'3'}

print('Done')