#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
import os
import qrcode
import time
from PIL import Image,ImageDraw,ImageFont

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

try:
    qrstring="REPLACE THIS WITH THE LONG STRING THAT STARTS WITH HC1"
    img = qrcode.make(qrstring,border=2)    
    img.thumbnail((200,200)) # resize to match the dimensions of the epaper    
    img.save(os.path.join(picdir,"covidqr.bmp")) # save the image so that it can be transferred using an app

except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    exit()
