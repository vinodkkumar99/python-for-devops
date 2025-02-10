import re
text = "The rain in Spain"
pattern = r"in"

search=re.search(pattern, text)
if search:
    print("pattern found:",search.group())
else:
    print("pattern not found")