import random
from luhn_check import luhn_check


def generate_random():
    acc = random.randrange(1, 10 ** 14)
    return acc


def create_card_number():
    while True:
        card_number = generate_random()
        if luhn_check(card_number):
            # num_string = str(card_number)
            # len_of_str = len(num_string)
            # account_number = int(num_string[len_of_str - 9: len_of_str])
            return card_number


def create_acc_pin():
    pin = random.randint(0, 9999)
    f"{pin:04}"
    return pin
