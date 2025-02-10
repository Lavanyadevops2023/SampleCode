'''str=['netflix','hulu','disney','appletv']
p='hulu'
if p in str:
    print("hulu", "is the streaming servies")
else:
    print("It is not include")'''

#string replacement
'''text="Hello world!"
part = text.split("world")
new_text="python".join(part)
print(new_text)'''

#regular expression
import re
text="Hello World!"
new_text=re.sub(r"world","python",text)
print(new_text)