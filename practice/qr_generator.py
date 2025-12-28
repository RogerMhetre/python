#Never name your file qrcode.py cause there is a orginal library of that file 
#That was the mistake i made 
#gg

import qrcode

url = input("Enter the URL: ").strip()
file_path = "/home/roger/Desktop/Python/Python-Code/qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image() 
img.save(file_path) 

print("QR code was generated")