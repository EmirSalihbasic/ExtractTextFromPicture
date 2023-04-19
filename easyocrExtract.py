# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 12:23:17 2023

@author: Korisnik
"""

import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

from PIL import Image
import easyocr

image = Image.open('image.jpg')   #if you want to add a picture, just change the part in this bracket.
reader = easyocr.Reader(['ch_sim'])
results = reader.readtext(image)

for result in results:
    print(result[1])