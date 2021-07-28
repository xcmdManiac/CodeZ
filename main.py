#CodeZ - main.py
#This is a code ENCODER and DECODER
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





def menu():
    print("Welcome to the python text encoder")
    print("1 - encode")
    print("2 - decode")
    menuask = int(input("Choose:"))
    if menuask == 1:
        encode()
    elif menuask == 2:
        decode()
    else:
        print("Error")


menu()