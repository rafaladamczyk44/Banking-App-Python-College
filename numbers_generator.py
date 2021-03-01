import random
from luhn_check import luhn_check


def generate_random():
    acc = random.randrange(1, 10 ** 14)
    return acc


def create_card_number():
    while True:
        card_number = generate_random()
        if luhn_check(card_number):
            return card_number


def create_acc_pin():
    pin = random.randint(0, 9999)
    f"{pin:04}"
    return pin
