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

    s = input("Enter the URL/text: ")
    if 'www.' in s:
        short = input("Press 1 for short the URL else 0: ")
        if short == '1':
            s = pyshorteners.Shortener().tinyurl.short(s)
            print(s)
    url = ps.create(s)
    name = input("Enter the file name in which you want to save QRcode: ")
    url.png(f'{name}.png', scale=2)


def wifi_QR():
    import wifi_qrcode_generator as qr

    username = input("Enter the username: ")
    password = input("Enter the password: ")
    qr.wifi_qrcode(username, False, 'WPA', password)


if __name__ == '__main__':
    qr_selector = int(input("1. QR code maker\n2. WiFi QR\n3. Read QRcode\nPress any option: "))
    if qr_selector == 1:
        url_QR()
    elif qr_selector == 2:
        wifi_QR()
    elif qr_selector == 3:
        read_QR()
    else:
        print("Select from given option!")
