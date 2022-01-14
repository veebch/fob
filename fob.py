#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
import os
import qrcode
import yaml
from PIL import Image,ImageDraw,ImageFont
picdir = os.path.dirname(os.path.realpath(__file__))
configfile = os.path.join(os.path.dirname(os.path.realpath(__file__)),'config.yaml') 

try:
    with open(configfile) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    
    qrstring=config['string'] # gets the string from config.yaml, if it does no already exist, 'cp config_example.yaml config.yaml'
    img = qrcode.make(qrstring)    
    img=img.thumbnail((200,200)) # resize to match the dimensions of the epaper    
    img.save(os.path.join(picdir,"certificateqr.bmp")) # save the image so that it can be transferred using an app
    print('Encoded the string from config.yaml into the QR code in the file certificateqr.bmp')
except IOError as e:
    print(e)