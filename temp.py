import qrcode

qr = qrcode.QRCode(border=1)
qr.add_data("https://example.com")
qr.make()

qr_text = qr.print_ascii()  # Generates ASCII QR code
print(qr_text)