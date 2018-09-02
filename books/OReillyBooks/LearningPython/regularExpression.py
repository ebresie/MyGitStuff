import re;
S='Hello   Python world'
match=re.match('Hello[ \t]*(.*)world', S);
print(match.group(1));