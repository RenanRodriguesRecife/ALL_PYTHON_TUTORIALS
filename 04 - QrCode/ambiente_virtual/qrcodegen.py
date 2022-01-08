import qrcode

def gera(data, img = "QrCode.png"):
    img_code = qrcode.make(data)
    img_code.save(img)
    return img_code

url = 'https://www.facebook.com/HL2Epistle3'
gera(url)