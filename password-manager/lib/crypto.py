import base64

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os


def encrypt_pass(password, key):
    key = key.encode('utf-8')

    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    encrypted_password = encryptor.update(password.encode()) + encryptor.finalize()
    return base64.b64encode(iv + encrypted_password).decode('utf-8')


def decrypt_pass(encrypted_password, key):
    key = key.encode('utf-8')
    encrypted_password = base64.b64decode(encrypted_password.encode('utf-8'))

    iv = encrypted_password[:16]
    encrypted_password = encrypted_password[16:]

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_password = decryptor.update(encrypted_password) + decryptor.finalize()
    return decrypted_password.decode()


def generate_key():
    return base64.b64encode(os.urandom(24)).decode('utf-8')
