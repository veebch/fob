![Action Shot](/chess.jpg)

[![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCz5BOU9J9pB_O0B8-rDjCWQ?label=YouTube&style=social)](https://www.youtube.com/channel/UCz5BOU9J9pB_O0B8-rDjCWQ)

# Fob

Tools and intructions to put important QR codes and other images onto a small, light, always-on, never-runs-out-of-power epaper keyring.

The method could be used to encode any information in a QR code eg Boarding Pass, Concert Ticket, etc or a small image (see chess puzzle use-case in photo)

## Hardware (and where to get one)

A NFC powered epaper display. You can get one [here](https://www.veeb.ch/store/p/fob).

## Installation

Install the required module, clone this repositiory, move into the cloned directory and copy the example config file with 
```
pip3 install qrcode
git clone https://github.com/veebch/fob
cd fob
cp config_example.yaml config.yaml
```

## Reading a code and transferring it to fob

## Image Generation

### QR code

- Scan your QR code using a QR-code reader app on a smartphone ( [iPhone](https://apps.apple.com/us/app/qr-reader-for-iphone/id368494609) | [Android](https://play.google.com/store/apps/details?id=com.gamma.scan&hl=en&gl=US) )

- Scanning the code will produce a long string of text. Place this string of text into the file `config.yaml` and save it

- Run the code `python3 fob.py', this will produce an image of a QR code.

### Other image

Scale a Black/White/Red image to a 200 x 200 picture. <TODO:  Insert the url for the chess image generator>

## Image upload

- The code will generate an image file (called `certificateqr.bmp`) that you can now copy to the fob using an NFC writer app ( [iPhone](https://apps.apple.com/us/app/nfc-e-tag/id1518982217) | [Android](https://www.waveshare.com/w/upload/NFCTag_EN.apk) )

## License

Code published under a GPL 3.0 licence
