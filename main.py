# Python Modules 
import pandas as pd
import os
from PIL import Image, ImageDraw, ImageFont

student_data = pd.read_csv('list.csv')
font = ImageFont.truetype('arial.ttf', 60)
for index, j in student_data.iterrows():
    new_certificate = Image.open('certificate.png')
    modify = ImageDraw.Draw(new_certificate)
    
