import qrcode


qr = qrcode.QRCode(
    version = 3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr.clear()
hola = 'hola'
qr.add_data(hola)

qr.make(fit=True)

img = qr.make_image(fill_color='#eb98ef',back_color='#f7f7fa')
img.save(f'{hola}.png')