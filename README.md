![Action Shot](/fobbed.jpg)

[![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCz5BOU9J9pB_O0B8-rDjCWQ?label=YouTube&style=social)](https://www.youtube.com/channel/UCz5BOU9J9pB_O0B8-rDjCWQ)

# Fobbed 

A few lines of code that will generate a small bmp qr code that can then be transferred to an epd keyfob, so you have a copy of the latest version of your certificate on your keychain. 

It uses one of these: LINK TO FOB. Tested on Swiss covid certificate only.

## Installation

Install the required module, clone this repositiory and move into the cloned directory with 
```
pip3 install qrcode
git clone https:github.com/veebch/fobbed
cd fobbed
```

## Code Generation

- Scan your covid certificate QR code.

- It will produce a long string. Put the string  (It starts with HC1:) into the file config.yaml

- Run this code

- It will generate a 200x200 bmp image file (called `certificateqr.bmp`) that you can now copy to the keyfob using an app like NFCTAG
