import qrcode
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


window = Tk()
window.title("QR Code Generator")
window.geometry("508x250")
window.resizable(False, False)
label = Label(window, text="Enter URL to generate QR code:")
label.grid(row=0,column=1, padx=10, pady=10)
entry = Entry(window, width=60)
entry.grid(row=1,column=1, padx=10, pady=10)
button = Button(window, text="Generate QR Code", command=lambda: generate_qr_code())
button.grid(pady=10,padx=10, row=3, column=1)

def generate_qr_code():
    url = entry.get()
    if url:
        img = qrcode.make(url)
        type(img)  # qrcode.image.pil.PilImage
        img.save("your_url.png")
        label.config(text="QR code generated and saved as 'your_url.png'.")
        window.geometry("508x500")  # Adjust window size to fit the image
        image_path = "your_url.png"
        try:
            img = ImageTk.PhotoImage(Image.open(image_path))
        except FileNotFoundError:
            print(f"Error: Image file not found at {image_path}")
            window.destroy() # Close the window if image is not found
            exit()
        image_label = Label(window, image=img)
        image_label.image = img
        image_label.grid(row=30,column=1, padx=10, pady=10,sticky="s")
    else:
        label.config(text="Please enter a valid URL.")
window.mainloop()