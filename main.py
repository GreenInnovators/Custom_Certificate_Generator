# Python Modules 
import pandas as pd
import os
from PIL import Image, ImageDraw, ImageFont

student_data = pd.read_csv('list.csv')
font = ImageFont.truetype('arial.ttf', 120)
for index, j in student_data.iterrows():
    new_certificate = Image.open('source/certificate.png')
    modify = ImageDraw.Draw(new_certificate)
    modify.text(xy=(680, 600),
              text='{}'.format(j['name']),
              fill=(127, 81, 146),
              font=font)
    new_certificate.save('certificates/{}.png'.format(j['name']))
