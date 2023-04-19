# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 12:25:39 2023

@author: Korisnik
"""

import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

from PIL import Image
import easyocr

image = Image.open('C:/Users/Korisnik/Desktop/FuEId13acAI-t8z.jpg')
reader = easyocr.Reader(['ch_sim'], gpu=True)
results = reader.readtext(image)

for result in results:
    print(result[1])