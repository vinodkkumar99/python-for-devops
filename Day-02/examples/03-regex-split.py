import re
text='abc,def,ghi,jkl'
pattern=r","

new_text=re.split(pattern,text)
print('new_text:',new_text)