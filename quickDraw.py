import quickDraw 
from quickdraw import QuickDrawData
import SptoText as st

tag = st.out
qd = QuickDrawData()
ext = '.jpg'
verb = []

for i in tag:
    if i[1] == 'NN' or i[1] == 'NNP':
        try:
            obj= qd.get_drawing(i[0].lower())
            name = i[0].lower()
            obj.image.save(name + ext)
        except:
            continue
    
    elif i[1] == 'VBG':
        verb.append(i[0])
    
    else:
        continue

for v in verb:
    print(v)


