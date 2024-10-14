import os 
import json 

teka=os.path.dirname(os.path.abspath(__file__))
data=os.path.join(teka,"data")

def cycle(a,start=0):
    start=0 if not start else a.index(start)
    while 1:
        yield a[start]
        start=(start+1)%len(a)

plan='''
Matthew, Mark, Luke, John
Genesis, Exodus, Leviticus, Numbers, Deuteronomy
Romans, 1 Corinthians, 2 Corinthians, Galatians, Ephesians, Philippians, Colossians, Hebrews
1 Thessalonians, 2 Thessalonians, 1 Timothy, 2 Timothy, Titus, Philemon, James, 1 Peter, 2 Peter, 1 John, 2 John, 3 John, Jude, Revelation
Job, Ecclesiastes, Song of Songs
Psalms
Proverbs
Joshua, Judges, Ruth, 1 Samuel, 2 Samuel, 1 Kings, 2 Kings, 1 Chronicles, 2 Chronicles, Ezra, Nehemiah, Esther
Isaiah, Jeremiah, Lamentations, Ezekiel, Daniel, Hosea, Joel, Amos, Obadiah, Jonah, Micah, Nahum, Habakkuk, Zephaniah, Haggai, Zechariah, Malachi
Acts
'''
lists=[[n for n in l.split(", ")] for l in plan.split("\n") if l]
lists_cycle=cycle(lists)
for _ in range(12): print(next(lists_cycle))