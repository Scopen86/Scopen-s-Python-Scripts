# Import necessary libraries
from pyzbar.pyzbar import decode
import qrcode
import requests
import io

def decode_and_display_qr_code(qr_code_data):
    # Generate and print ASCII QR code
    qr = qrcode.QRCode(border=1)
    qr.add_data(qr_code_data)
    qr.make()
    
    output = io.StringIO()
    qr.print_ascii(out=output)  # Generates ASCII QR code
    qr_text = output.getvalue()
    
    if qr_text is None:
        raise ValueError("Failed to generate ASCII QR code")
    
    print(qr_text)
    return qr_text


