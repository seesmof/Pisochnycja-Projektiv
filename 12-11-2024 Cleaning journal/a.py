import glob
import os
from datetime import datetime

root=os.path.dirname(os.path.abspath(__file__))
target_folder=os.path.join(root,"entries")
target_files=os.listdir(target_folder)
def get_formatted_date(date:str):
    day,month,year=date.replace('.md','').split('-')
    return year,month,day
target_files.sort(key=get_formatted_date)

gls=[]
for f in target_files:
    file_path=os.path.join(target_folder,f)
    with open(file_path,encoding='utf-8',mode='r') as fr:
        ls=fr.readlines()
    day_name=f.replace('.md','')
    day_header='### ' + day_name + '\n'
    ls.insert(0,day_header)
    print(ls)
    gls+=ls