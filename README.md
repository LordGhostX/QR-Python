# QR

QR code generator in Python with Google Chart API

Generates QR codes from links

## Usage
Generating QR for a site
```bash
$ qr.py google.com
```
Generating a link specifying the size and file name to save with; Default size is 200px
```bash
$ qr.py google.com 200 google_qr.png
```
Running the script normally
```bash
$ qr.py
"Enter Destination URL: google.com"
"Enter image size in px (Leave empty for 200px): 200"
"Enter Filename (Leave empty for site name): google_qr.png"
```
Importing from another script
```python
from qr import generate_qr

if generate_qr("google.com"):
    print("QR generated successfully!")
else:
    print("Error generating QR!")
```

## Requirements
* Python
* Internet Connection
* Requests module

## LICENSE
* [WTFPL](http://www.wtfpl.net/)
