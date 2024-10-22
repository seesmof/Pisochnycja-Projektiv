import os 
import json 
this_folder=os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(this_folder,"chapters.json")) as f: chapters=json.load(f)
with open(os.path.join(this_folder,"lists.json")) as f: lists=json.load(f)
with open(os.path.join(this_folder,"names.json")) as f: names=json.load(f)

def move_to_next_reading_on_list(list_number:int):
    if lists[list_number]['chapter'] < chapters[str(lists[list_number]['Books'][lists[list_number]['Book']])]:
        lists[list_number]['chapter']+=1
    else: 
        lists[list_number]['chapter']=1
        lists[list_number]['Book']=lists[list_number]['Book']+1 if lists[list_number]['Book']<len(lists[list_number]['Books'])-1 else 0

def show_current_reading_for_list(list_number:int):
    print(names[str(lists[list_number]['Books'][lists[list_number]['Book']])], lists[list_number]['chapter'])

def get_readings_for_next_day():
    for list_number in range(10):
        move_to_next_reading_on_list(list_number)
        show_current_reading_for_list(list_number)

def get_readings_for_specified_day(day:int):
    global lists
    lists_copy=lists
    print(lists_copy)
    lists=lists_copy
    for _ in range(day): get_readings_for_next_day()
    lists=lists_copy

get_readings_for_specified_day(47)
get_readings_for_specified_day(1)

with open(os.path.join(this_folder,"lists.json"),'w') as f: json.dump(lists,f,indent=2)