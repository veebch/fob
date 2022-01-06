![Action Shot](/fobbed.jpg)

[![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCz5BOU9J9pB_O0B8-rDjCWQ?label=YouTube&style=social)](https://www.youtube.com/channel/UCz5BOU9J9pB_O0B8-rDjCWQ)

# Fob 

A few lines of code that will generate a small bmp qr code that can then be transferred from a smartphone (which can run out of power) to an epaper key-fob (that does not have a battery, so will never run out of power).

The code has been tested on a Swiss Covid Vaccination certificate, but the same method could be used to encode any information in a QR code. 

## Hardware

It uses one of these: LINK TO FOB.

## Installation

Install the required module, clone this repositiory, move into the cloned directory and copy the example config file with 
```
pip3 install qrcode
git clone https://github.com/veebch/fob
cd fob
cp config_example.yaml config.yaml
```

## Code Generation

- Scan your QR code (eg your COVID vaccination certificate, using an QR-code reader app on a smartphone ([iPhone](https://apps.apple.com/us/app/qr-reader-for-iphone/id368494609) | [Android](https://play.google.com/store/apps/details?id=com.gamma.scan&hl=en&gl=US))).

- Scanning will produce a long string of text. Place this string of text into the file `config.yaml` and save it. 

- Run the code `python3 fob.py`

- The code will generate a 200x200 bmp image file (called `certificateqr.bmp`) that you can now copy to the keyfob using an app (iPhone | Android)

## License

Published under a GPL 3.0 licence
