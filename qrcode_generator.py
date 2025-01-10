import pyqrcode
import png
from pyqrcode import QRCode


s=input("type url")
url=pyqrcode.create(s)

url.png('myqr.png',scale=6)
