import os
import re

root_folder_path=os.path.dirname(os.path.abspath(__file__))
target_file_path=os.path.join(root_folder_path,'test.md')
with open(target_file_path,encoding='utf-8',mode='r') as f:
    text=f.read()

'''
replace all ` -` with em dash 
replace all ` "` and `" ` with opening and closing double brackets 
replace all ` '` and `' ` with opening and closing single brackets 
replace all `\w!` and `!\w` with embeded accent mark 
replace all `\w'` and `'\w` with apostrophe symbols 
'''

text=text.replace(' -',' —')
accent_mark='\u0301'
text=re.sub(r'(\s)-',r'\1—',text)
text=re.sub(r'-(\s)',r'—\1',text)
last_closing=False
for i,symbol in enumerate(text):
    print(rf'{symbol}')
text=re.sub(r'(\w)!',rf'\1{accent_mark}',text)
text=re.sub(r'!(\w)',rf'{accent_mark}\1',text)
text=re.sub(r'(\w)\'',r'\1ʼ',text)
text=re.sub(r'\'(\w)',r'ʼ\1',text)

with open(target_file_path,encoding='utf-8',mode='w') as f:
    f.write(text)