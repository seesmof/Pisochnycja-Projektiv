import string
import time
import os
import re

root_folder_path=os.path.dirname(os.path.abspath(__file__))
target_file_path=os.path.join(root_folder_path,'test.md')

def mark_text(
    given_text:str,
):
    def make_dashes_typographical(text):
        text=re.sub(r'(\s)-',r'\1—',text)
        text=re.sub(r'-(\s)',r'—\1',text)
        return text

    def render_accent_marks(text):
        accent_mark='\u0301'
        return re.sub(rf'([аеєиіїоуюяАЕЄИІЇОУЮЯ])!([\w{string.punctuation}])',rf'\1{accent_mark}\2',text)

    def make_apostrophes_typographical(text):
        return re.sub(rf'(\w)\'([\w{string.punctuation}])',r'\1ʼ\2',text)

    def make_quotes_typographical(text):
        def replace_at_index(text,index=0,replacement=''):
            return f'{text[:index]}{replacement}{text[index+1:]}'

        single_last_closing=False
        double_last_closing=False
        for i,symbol in enumerate(text):
            if symbol=="'":
                if not single_last_closing: 
                    text=replace_at_index(text,i,'‹')
                    single_last_closing=True
                else: 
                    text=replace_at_index(text,i,'›')
            elif symbol=='"':
                if not double_last_closing: 
                    text=replace_at_index(text,i,'«')
                    double_last_closing=True
                else: 
                    text=replace_at_index(text,i,'»')
        return text

    dashes_fixed=make_dashes_typographical(given_text)
    apostrophes_fixed=make_apostrophes_typographical(dashes_fixed)
    quotes_fixed=make_quotes_typographical(apostrophes_fixed)
    accents_fixed=render_accent_marks(quotes_fixed)
    return accents_fixed

with open(target_file_path,encoding='utf-8',mode='r') as f:
    read_text=f.read()
with open(target_file_path,encoding='utf-8',mode='w') as f:
    f.write(mark_text(read_text))
print('Text marked')

while 1:
    with open(target_file_path,encoding='utf-8',mode='r') as f:
        new_read_text=f.read()
    if new_read_text!=read_text:
        marked_text=mark_text(new_read_text)
        with open(target_file_path,encoding='utf-8',mode='w') as f:
            f.write(marked_text)
        print('\nText marked')
        read_text=marked_text
    else: read_text=new_read_text
    time.sleep(1)