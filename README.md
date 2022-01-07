![Action Shot](/fobbed.jpg)

[![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCz5BOU9J9pB_O0B8-rDjCWQ?label=YouTube&style=social)](https://www.youtube.com/channel/UCz5BOU9J9pB_O0B8-rDjCWQ)

# Fob

Put important QR codes onto a little always-on, never-runs-out-of-power epaper keyring.

This repository contains tools and intructions to do that. It has been tested on a Swiss Covid19 Vaccination certificate, but the same method could be used to encode any information in a QR code eg Boarding Pass, Concert Ticket, etc 

## Hardware

It uses one of [these](https://veeb.ch/).

## Installation

Install the required module, clone this repositiory, move into the cloned directory and copy the example config file with 
```
pip3 install qrcode
git clone https://github.com/veebch/fob
cd fob
cp config_example.yaml config.yaml
```

## Reading a QR code and transferring it to fob

- Scan your QR code (for example, a COVID vaccination certificate) using a QR-code reader app on a smartphone ( [iPhone](https://apps.apple.com/us/app/qr-reader-for-iphone/id368494609) | [Android](https://play.google.com/store/apps/details?id=com.gamma.scan&hl=en&gl=US) )

- Scanning will produce a long string of text. Place this string of text into the file `config.yaml` and save it

- Run the code `python3 fob.py`

- The code will generate an image file (called `certificateqr.bmp`) that you can now copy to the fob using an app ( [iPhone](https://apps.apple.com/us/app/nfc-e-tag/id1518982217) | [Android](https://www.waveshare.com/w/upload/NFCTag_EN.apk) )

## License

Code published under a GPL 3.0 licence
