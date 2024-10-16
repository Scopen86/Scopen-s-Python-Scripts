import pyqrcode

# Create a QR code instance
qr = pyqrcode.create("Placeholder data")

# Print the QR code to the console
print("\nQR Code:")
print(qr.terminal(quiet_zone=1))

print("QR code displayed in the console.")
