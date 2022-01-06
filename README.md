![Action Shot](/fobbed.jpg)

[![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCz5BOU9J9pB_O0B8-rDjCWQ?label=YouTube&style=social)](https://www.youtube.com/channel/UCz5BOU9J9pB_O0B8-rDjCWQ)

# Fob 

A few lines of code that will generate a small bmp qr code that can then be transferred to an epd keyfob, so you have a copy of the latest version of your certificate on your keychain. 

It uses one of these: LINK TO FOB. Tested on Swiss covid certificate only.

## Installation

Install the required module, clone this repositiory, move into the cloned directory and copy the example config file with 
```
pip3 install qrcode
git clone https://github.com/veebch/fob
cd fob
cp config_example.yaml config.yaml
```

## Code Generation

- Scan your covid certificate QR code (eg using an app on a smartphone).

- Scanning will produce a long string of text. Put the text  (It starts with HC1:) into the file config.yaml and save it. 

- Run the code `python3 fob.py`

- The code will generate a 200x200 bmp image file (called `certificateqr.bmp`) that you can now copy to the keyfob using an app like NFCTAG

## License

Published under a GPL 3.0 licence
