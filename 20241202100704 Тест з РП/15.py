'''
Прочитати дані з текстового файлу в табличну структуру даних пакету pandas, враховуючи, що дані розділені окличними знаками, а в файлі присутній перший рядок з підписом назв стовпчиків. Відкинути всі записи зі структури, що мають пропущені значення. Одна з характеристик, присутня у кожному записі, має назву rating, представляє рейтинг та має дійсне значення. Додати нову характеристику, значення якої встановити рівною 3, якщо рейтинг не менше 4.5, рівною 2, якщо рейтинг не менше 4, рівною 1, якщо рейтинг не менше 3, та рівною 0 у всіх інших випадках. Якщо початкове значення рейтингу більше 5, то такі записи відкинути з результуючої структури.
'''

import os
import pandas 

root=os.path.dirname(os.path.abspath(__file__))
target_path=os.path.join(root,'data.txt')

data=pandas.read_table(target_path,sep='!')
no_skipped=data.dropna()
f=no_skipped.to_dict()
n=dict()
for id,rating in f['rating'].items():
    v=3 if rating>=4.5 else 2 if rating>=4 else 1 if rating >=3 else 0
    n[id]=v
f['new']=n
data=pandas.DataFrame.from_dict(f).query('rating<5')
print(data)