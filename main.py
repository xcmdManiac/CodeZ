#CodeZ - main.py
#This is a code ENCODER and DECODER
import tkinter as tk
from PIL import Image, ImageTk
import base64






window = tk.Tk()
window.title("CodeZ")
canvas = tk.Canvas(window, width=600, height=660, bg="#32a893")
canvas.grid(columnspan=13, rowspan=12)
#Function
class En:
    def encode(self, askencode):
        askencode = askencode.encode("utf-8")
        base64_info_encode = base64.b64encode(askencode)
        print("This is your encoded text:", base64_info_encode.decode("utf-8"))
        encoded = base64_info_encode.decode("utf-8")
        outputtexte = tk.Label(window, text=encoded, fg="black", bg="#32a893", font="Raleway")
        outputtexte.grid(column=6, row=4)
        return



class De:
    def decode(self, askdecode):
        askdecode = askdecode.encode()
        base64_info_decode = base64.decodebytes(askdecode)
        print("This is your decoded text:", base64_info_decode)
        decoded = base64_info_decode
        outputtextd = tk.Label(window, text=decoded, fg="black", bg="#32a893", font="Raleway")
        outputtextd.grid(column=6, row=4)
        return


ee = En()
dd = De()
#Logo
logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=6, row =0)


#GUI
e = tk.Entry(window, text="Type something here:", fg="black", width=50, bg="gray")
e.grid(columnspan=12, column=0, row=1)
def DECODEclicked():
    Outputd = e.get()
    dd.decode(Outputd)
    return
button = tk.Button(window, text="DECODE", fg="Blue", font="Arial", padx=50, pady=3, command=DECODEclicked)
button.grid(columnspan=12, column=0, row=3)
def ENCODEclicked():
    Outpute = e.get()
    ee.encode(Outpute)
    return


button2 = tk.Button(window, text="ENCODE", fg="Blue", font="Arial", padx=50, pady=3, command=ENCODEclicked)
button2.grid(columnspan=12, column=0, row=2)



window.mainloop()



