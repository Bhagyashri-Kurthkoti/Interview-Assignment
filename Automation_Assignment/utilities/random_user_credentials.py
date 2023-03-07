import random
import string


def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    domain = 'aol.com'
    return f"{username}@{domain}"


def generate_random_name(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length)).capitalize()


def generate_random_first_name():
    return generate_random_name(6)


def generate_random_last_name():
    return generate_random_name(6)


def generate_random_password():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    password = random.choice(lowercase) + random.choice(uppercase) + random.choice(digits) + random.choice(special)
    password += ''.join(random.choices(lowercase + uppercase + digits + special, k=4))
    return password


def generate_random_pincode():
    return ''.join(random.choices(string.digits, k=4))
