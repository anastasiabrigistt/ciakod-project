import random

def encrypt_pass(password, key):
    encstr = ""
    for i in password:
        if (ord(i)) >= 65 and (ord(i) <= 90):
            temp = (ord(i) + key)
            if temp > 90:
                temp = temp % 90 + 64
            encstr = encstr + chr(temp)
        elif (ord(i)) >= 97 and (ord(i) <= 122):
            temp = (ord(i) + key)
            if temp > 122:
                temp = temp % 122 + 96
            encstr = encstr + chr(temp)
        else:
            encstr = encstr + chr(ord(i) + key)
    return encstr


def decrypt_pass(enc_password, key):
    decstr = ""
    for i in enc_password:
        if ((ord(i)) >= 65) and (ord(i)) <= 90:
            decstr = decstr + chr((ord(i) - key - 65) % 26 + 65)
        elif ((ord(i)) >= 97) and (ord(i)) <= 122:
            decstr = decstr + chr((ord(i) - key - 97) % 26 + 97)
        else:
            decstr = decstr + chr(ord(i) - key)
    return decstr



