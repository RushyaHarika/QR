import pyqrcode
x=input("Enter the url to which QR Code is to be generated:\n")
qr=pyqrcode.create(x)
qr.show()