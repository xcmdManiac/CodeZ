#CodeZ - main.py
#This is a code ENCODER and DECODER
import tkinter as tk
from PIL import Image, ImageTk
import base64

def encode():
    askencode = input("Type something to encode:")
    askencode = askencode.encode("utf-8")
    base64_info_encode = base64.b64encode(askencode)
    print("This is your encoded text:", base64_info_encode.decode("utf-8"))

def decode():
    askdecode = input("Type something to decode:")
    askdecode = askdecode.encode()
    base64_info_decode = base64.decodebytes(askdecode)
    print("This is your decoded text:", base64_info_decode)



window = tk.Tk()
window.title("CodeZ")
canvas = tk.Canvas(window, width=600, height=660, bg="#32a893")
canvas.grid(columnspan=13, rowspan=12)
#Logo
logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=6, row =0)


#GUI
e = tk.Entry(window, text="Type something here:", fg="black", width=50, bg="gray")
e.grid(columnspan=12, column=0, row=1)
button = tk.Button(window, text="DECODE", fg="Blue", font="Arial", padx=50, pady=3)
button.grid(columnspan=12, column=0, row=3)
def ENCODEclicked():
    Outpute = e.get()
    print(Outpute)
    file = open("EncodedText.html", "w")
    file.write("<html>")
    file.write("<head>")
    file.write(Outpute)
    file.write("</head>")
    file.write("</html>")


button2 = tk.Button(window, text="ENCODE", fg="Blue", font="Arial", padx=50, pady=3, command=ENCODEclicked)
button2.grid(columnspan=12, column=0, row=2)



window.mainloop()



