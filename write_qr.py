import qrcode

class config:
    def __init__(self, version = 3, box_size = 10, border = 4,fill_color = '#eb98ef',back_color='#f7f7fa'):
        self.version = version
        self.box_size = box_size
        self.border = border
        self.fill_color = fill_color
        self.back_color = back_color
        
    def conf_qr(self):        
        qr = qrcode.QRCode(
            version = self.version,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=self.box_size,
            border=self.border
        )
        return qr
    def create(self, datos):  
        qr = self.conf_qr()      
        qr.clear()
        data = datos
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=self.fill_color,back_color=self.back_color)
        img.save(f'qr_{datos}.png')