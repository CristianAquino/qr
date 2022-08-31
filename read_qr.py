from pyzbar.pyzbar import decode
from PIL import Image

image = Image.open('hola.png')
qr_code = decode(image)[0]
data = qr_code.data.decode('utf8').encode('shift-jis').decode('utf-8')
print(data)