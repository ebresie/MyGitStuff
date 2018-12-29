# binary files

import struct

# write binary
packed = struct.pack('>i4sh', 7, b'spam', 8)
# Create packed binary 
print('binary file:',packed)
# 10 bytes, not objects or text b'\x00\x00\x00\x07spam\x00\x08'
file = open('data.bin', 'wb')
# Open binary output file
file.write(packed)
# Write packed binary data 10
file.close()

# read binary
data = open('data.bin', 'rb').read()
# Open/read binary data file
print('read binary=',data)
# 10 bytes, unaltered #b'\x00\x00\x00\x07spam\x00\x08'
print('slice of bytes=',data[4:8])
# Slice bytes in the middle b'spam'
print('list=',list(data))
# A sequence of 8-bit bytes [0, 0, 0, 7, 115, 112, 97, 109, 0, 8]
struct.unpack('>i4sh', data)
# Unpack into objects again (7, b'spam', 8)