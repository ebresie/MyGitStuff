f = open('data.txt', 'w')
# Make a new file in output mode ('w' is
f.write('Hello\n')
# Write strings of characters to it 6
f.write('world\n')
# Return number of items written in Python 3.X 6
f.close()
# Close to flush output
print('Done writing file')
print('Reading file')
f = open('data.txt')
# 'r' (read) is the default processing mode
text = f.read()
# Read entire file into a string
print(text)
# print interprets control characters Hello world 
print(text.split())
# File content is always a string ['Hello', 'world']
f.close()
print('Done Reading entire file')

for line in open('data.txt'): 
    print('line='+line)
print('Done Reading file iterating line by line')

