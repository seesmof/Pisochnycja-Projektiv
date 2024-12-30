import glob
from shutil import copy2
import os
import re
import time 

root_folder=os.path.dirname(os.path.abspath(__file__))
paratext_folder=os.path.join(r'C:\My Paratext 9 Projects\UFB')
revision_folder=os.path.join(root_folder,'Revision')
revision_files = glob.glob(revision_folder + "\\*.USFM")

def copy_to_paratext():
    try:
        for file_path in revision_files:
            copy2(file_path, os.path.join(paratext_folder, file_path.split("\\")[-1]))
    except: pass
    for file_name in os.listdir(revision_folder):
        paratext_file_path=os.path.join(paratext_folder,file_name)
        with open(paratext_file_path,encoding='utf-8',mode='r') as f:
            lines=f.readlines()
        lines=[l for l in lines if '\\rem' not in l]
        with open(paratext_file_path,encoding='utf-8',mode='w') as f:
            f.write('\n'.join([l.strip() for l in lines]))

def form_markdown_output():
    def remove_footnotes_with_contents(verse: str):
        footnote_pattern=r'\\(\+*)f(.*?)\\(\+*)f\*'
        return re.sub(footnote_pattern,'',verse)
    output_lines=[]

    for file_name in os.listdir(revision_folder):
        file_path=os.path.join(revision_folder,file_name)
        with open(file_path,encoding='utf-8',mode='r') as f:
            lines=f.readlines()
        
        Book_name=file_name[2:].split('.')[0]
        output_lines.append(f'# {Book_name}')
        for line in lines:
            if r'\c ' in line:
                chapter_number=line[3:].strip()
                res=f'### {Book_name} {chapter_number}'
                output_lines.append(res)
            elif r'\p' in line:
                output_lines.append('')
            elif r'\v ' in line:
                WJ_COLOR='#7e1717'
                line=line[3:].strip()
                verse_number,contents=line.split(maxsplit=1)
                contents=re.sub(r'\\(\+?)qt\s',f'<span style="font-variant: small-caps">',contents)
                contents=re.sub(r'\\(\+?)wj\s',f'<span style="color: {WJ_COLOR}">',contents)
                contents=re.sub(r'\\(\+?)add\s','<em>',contents)
                contents=contents.replace('\\add*','</em>')
                contents=remove_footnotes_with_contents(contents)
                # all other closing tags
                contents=re.sub(r'\\(\+?)\w+\*','</span>',contents)
                res=f'<sup>{verse_number}</sup> {contents}'
                output_lines.append(res)

    output_file=os.path.join(root_folder,'a.md')
    with open(output_file,encoding='utf-8',mode='w') as f:
        f.write('\n'.join(output_lines))

def perform_automations():
    print("Markdown")
    form_markdown_output()

def monitor_files_for_changes():
    latest_file = max(revision_files, key=os.path.getmtime)
    last_modification_time = os.path.getmtime(latest_file)
    perform_automations()
    while 1:
        latest_file = max(revision_files, key=os.path.getmtime)
        current_modification_time = os.path.getmtime(latest_file)
        if last_modification_time != current_modification_time:
            perform_automations()
            last_modification_time = current_modification_time
        time.sleep(1)

if __name__ == "__main__":
    monitor_files_for_changes()