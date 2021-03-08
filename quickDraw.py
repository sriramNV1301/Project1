import quickDraw 
from quickdraw import QuickDrawData
import SptoText as st

tag = st.out
qd = QuickDrawData()
ext = '.jpg'

for i in tag:
    if i[1] == 'NN' or i[1] == 'NNP':
        obj= qd.get_drawing(i[0].lower())
        name = i[0].lower()
        obj.image.save(name + ext)
    else: 
        continue

