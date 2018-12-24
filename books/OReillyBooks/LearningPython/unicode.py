S='sp\xc4m'
# Non-AUnicodeSCII  text
print('unicoded text=',S)
# 'spÄm'
print('unicode character=',S[2])
# Sequence of characters 'Ä'
file = open('unidata.txt', 'w', encoding='utf-8')
# Write/encode UTF-8 text
file.write(S)
# 4 characters written 4
file.close()
text = open('unidata.txt', encoding='utf-8').read()
# Read/decode UTF-8 text
print('read unicode=',text)
#'spÄm'
print('text len=',len(text))
# 4 chars (code