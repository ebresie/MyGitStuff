# basic string / byte conversion
S='shrubbery'
L=list(S)
print(L)
L[1]='c'
print(L)
print(''.join(L))
B=bytearray(b'spam')
print(B)
B.extend(b'eggs')
print(B)
B.decode()
print(B.decode())
# string methods 
S='Spam'
print(S)
print(S.find('pa'))
print(S.replace('pa','XYZ'))
line='aaa,bbb,cccc,dd'
print(line.split())
print(S.upper())
print('is alpha=',S.isalpha())
print('is digit',S.isdigit())
line='aaa,bbb,cccc, dd\n'
print(line)
print(line.rstrip())
print(line)
print('{:,.2f}'.format(26999.2567))
print('%.2f | %+05d' % ( 3.14159, -42 ))
# unicode encoding/decoding
print('\u00A3','\u00A3'.encode('latin1'),b'\xA3'.decode('latin1'))