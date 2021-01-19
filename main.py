def read_QR():
    from pyzbar.pyzbar import decode
    from PIL import Image

    d = decode(Image.open(input("Enter the name of QRcode: ")))
    print(d[0].data.decode('ascii'))


def url_QR():
    import pyqrcode as ps
    import pyshorteners
    import png
    from pyqrcode import QRCode

    s = input("Enter the URL: ")
    short = input("Press 1 for short the URL else 0: ")
    if short == '1':
        s = pyshorteners.Shortener().tinyurl.short(s)
        print(s)
    url = ps.create(s)
    name = input("Enter the file name in which you want to save QRcode: ")
    url.png(f'{name}.png', scale=2)


if __name__ == '__main__':
    qr_selector = int(input("1. Url\n2. Read QRcode\nPress any option: "))
    if qr_selector == 1:
        url_QR()
    elif qr_selector == 2:
        read_QR()
    else:
        print("Select from given option!")
