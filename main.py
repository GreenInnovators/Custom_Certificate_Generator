# Python Modules 
import pandas as pd
import os
from PIL import Image, ImageDraw, ImageFont

student_data = pd.read_csv('list.csv')
font = ImageFont.truetype('arial.ttf', 60)
for index, j in student_data.iterrows():
    new_certificate = Image.open('source/certificate.png')
    modify = ImageDraw.Draw(new_certificate)
    modify.text(xy=(150, 250),
              text='{}'.format(j['name']),
              fill=(0, 0, 0),
              font=font)
    new_certificate.save('certificates/{}.png'.format(j['name']))
