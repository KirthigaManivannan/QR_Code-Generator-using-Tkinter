import tkinter as tk
from tkinter import ttk
import qrcode

def generate_qr_code():
    # Get the data from the entry widget
    data = entry.get()

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Display the QR code
    img.save("qrcode.png")
    img.show()

# Create the main window
window = tk.Tk()
window.title("QR Code Generator")

# Create and place widgets
label = ttk.Label(window, text="Enter data:")
label.grid(column=0, row=0, padx=10, pady=10)

entry = ttk.Entry(window)
entry.grid(column=1, row=0, padx=10, pady=10)

button = ttk.Button(window, text="Generate QR Code", command=generate_qr_code)
button.grid(column=0, row=1, columnspan=2, pady=10)

# Start the GUI
window.mainloop()
