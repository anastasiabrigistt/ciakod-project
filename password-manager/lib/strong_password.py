import random
import string
import re


def check_password_strength(password):
    conditions_met = 0
    comments = ""
    if len(password) >= 8:
        conditions_met += 1
    else:
        comments += "Пароль должен содержать не меньше восьми символов."

    if re.search(r'[a-zа-я]', password):
        conditions_met += 1
    else:
        if comments != "":
            comments = comments.replace(".", ", ", 1)
            comments += "иметь хотя бы одну строчную букву."
        else:
            comments += "Пароль должен иметь хотя бы одну строчную букву."

    if re.search(r'[A-ZА-Я]', password):
        conditions_met += 1
    else:
        if comments != "":
            comments = comments.replace(".", ", ", 1)
            comments += "иметь хотя бы одну заглавную букву."
        else:
            comments += "Пароль должен иметь хотя бы одну заглавную букву."
    if re.search(r'[0-9]', password):
        conditions_met += 1
    else:
        if comments != "":
            comments = comments.replace(".", ", ", 1)
            comments += "иметь хотя бы одну цифру."
        else:
            comments += "Пароль должен иметь хотя бы одну цифру."
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        conditions_met += 1
    else:
        if comments != "":
            comments = comments.replace(".", ", ", 1)
            comments += "иметь хотя бы один специальный символ."
        else:
            comments += "Пароль должен иметь хотя бы один специальный символ."
    if conditions_met == 0:
        return "Ненадёжный", comments
    elif conditions_met == 1 or conditions_met == 2:
        return "Слабый", comments
    elif conditions_met == 3 or conditions_met == 4:
        return "Средний", comments
    else:
        return "Надёжный", ''


def generate_password(length=12):
    if length < 8:
        raise ValueError("Password must be at least 8 characters long")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()"

    all_chars = lower + upper + digits + special

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)

    return ''.join(password)



