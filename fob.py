#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
import os
import qrcode
import yaml
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from PIL import Image,ImageDraw,ImageFont
picdir = os.path.dirname(os.path.realpath(__file__))
configfile = os.path.join(os.path.dirname(os.path.realpath(__file__)),'config.yaml')
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M, # medium error connection
    box_size=10,
    border=2,
)
try:
    with open(configfile) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    
    qrstring=config['string'] # gets the string from config.yaml, if it does no already exist, 'cp config_example.yaml config.yaml'
    print("Encoding:",qrstring)
    qr.add_data(qrstring)
    img = qr.make_image(fill_color="black", back_color="white",image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
    img.thumbnail((200,200)) # resize to match the dimensions of the epaper    
    img.save(os.path.join(picdir,"certificateqr.bmp")) # save the image so that it can be transferred using an app
    print('Encoded the string from config.yaml into the QR code in the file certificateqr.bmp')
except IOError as e:
    print(e)