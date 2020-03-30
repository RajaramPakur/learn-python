import re

# Regular expressions
text_to_search = '''
ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

1234567890
Mr. Rajaram Pakur

Hello Doctor
Ha Haha

MetaCharacters (Need to be escaped):
. ^ $ # @ ! & * ( ) [ ] { } ? /

rajarampakur.com
332-555-1111

123.456.1234
911-555-1111
977-555-1111

cat
bat
mat
sat


'''

sentance = 'Start a sentence and then bring it to an end'

# print('\tTab')
# compare to raw string
# print(r'\tTab')

# match phone number pattern
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

# Using file contents
# ==========
# f = open('test.txt', 'w')
# f.write(text_to_search)
# f.close
# with open('test.txt', 'r', encoding='utf-8') as f:
# contents = f.read()

# pattern = re.compile(r'9[71][71][-.]\d\d\d[-.]\d\d\d\d')

# specify range
pattern = re.compile(r'[^b]at')

matches = pattern.finditer(text_to_search)
print({match for match in matches})
