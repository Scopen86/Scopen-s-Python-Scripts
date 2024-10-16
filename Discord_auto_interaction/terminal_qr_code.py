# Import necessary libraries
from pyzbar.pyzbar import decode
import qrcodeT


def decode_and_display_qr_code(element_image):
    # Decode the QR code from the element_image
    decoded_objects = decode(element_image)

    if decoded_objects:
        # Extract the QR code data as a string then print out the QR code
        qr_code_data = decoded_objects[0].data.decode('utf-8')
        print(f"QR code data: {qr_code_data}")
        qrcodeT.qrcodeT(qr_code_data)
    else:
        print("No QR code found in the image.")
