import decimal;
#import decimals and fractions
# Integers (unlimited size)
print('Integer Values:');
intValues = 1234;
print(intValues);
intValues=-24;
print(intValues);
intValues =0;
print(intValues);
intValues =99999999999999;
print(intValues);
print()

# Floating-point numbers 
print('Floating Point Values:');
floatValue=1.2;
print(floatValue);
floatValue=1.;
print(floatValue);
floatValue=3.14e-10;
print(floatValue);
floatValue=4E210;
print(floatValue);
floatValue=4.0e+210;
print(floatValue);
print()

#Octal, hex, and binary literals in 3.X
# - these are treated like integers
# - to print out string version need oct, hex, or bin functions
print('Octal, hex, and binary literals in 3.X:');
octalValue=0o177;
print(oct(octalValue));
hexValue=0x9ff;
print(hex(hexValue));
binaryValue=0b101010;
print(bin(binaryValue));
print()
# Complex number literals 
print('Complex number literals :');
print(3+4j);
print( 3.0+4.0j)
print(3J);
realValue=3.0
imaginaryValue=5
print(complex(realValue,imaginaryValue));
print();

#Sets: 2.X and 3.X construction forms 
print('Sets: 2.X and 3.X construction forms :');
print(set('spam'))
print({1, 2, 3, 4} );
print()

# Decimal and fraction extension types 
#print('Decimal and fraction extension types ');
#print(Decimal('1.0'));
#print(Fraction(1, 3) )
#print()

# Boolean type and constants
print('Boolean type and constants');
X=1
print(bool(X));
print(True)
print(False)
print()

print('Done')