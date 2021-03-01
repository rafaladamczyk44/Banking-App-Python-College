# PIN - 4 digits
# Account number - 9 numbers
# Credit card number - 13 numbers

# TODO database connection for new account, pin and balance

from luhn_check import luhn_check
from numbers_generator import create_card_number, create_acc_pin


class Account:
    def __init__(self, number, pin, balance):
        self.number = number
        self.pin = pin
        self.balance = balance

    def balance_operations(self):
        # 1 - add, 2 - decrease
        operation = int(input('Please choose what do you want to do with balance: '))
        if operation == 1:
            amount = int(input('Please provide the amount you want to add: '))
            self.balance = self.balance + amount
        elif operation == 2:
            amount = int(input('Please provide the amount you want to decrease: '))
            if self.balance <= 0:
                print("Your balance is too low to do this operation.")
            else:
                self.balance = self.balance - amount
        else:
            print("Incorrect option, try again or press '0' to quit")

        print(f'Your current balance is {self.balance}')


def create_account():
    balance = 0
    number = create_card_number()
    pin = create_acc_pin()
    acc = Account(number, pin, balance)

    print(f'Your account was successfully created!\nYour account number is {number}\nYour pin is {pin}')
    print(f'Your balance is {balance}')
    return acc


while True:
    print("Please choose one of the below options 1-3: ")

    entry_decision = int(input(f'1. Create an account\n2. Log into account\n0. Exit\nInput: '))

    if entry_decision == 1:
        print("Creating account")
        new_account = create_account()

    elif entry_decision == 2:
        while True:
            logging_acc_number = int(input("Please provide your account number: "))
            logging_pin = int(input("Please provide your PIN number: "))

            # validate = luhn_check(logging_acc_number) - not needed now

            if logging_acc_number == new_account.number and logging_pin == new_account.pin:
                print("Login successful! ")
                new_account.balance_operations()
                break
            else:
                login_input = input("Do you want to try again? [Y/N]: ")
                if login_input == 'n' or login_input == 'N':
                    break
                else:
                    pass

    elif entry_decision == 0:
        print("Goodbye!")
        break

    else:
        print("Wrong input, please try again")
