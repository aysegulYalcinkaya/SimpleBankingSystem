import database
import random

def calculate_sum(number):
    sum = 0
    for index in range(0, len(number), 2):
        n = int(number[index]) * 2
        if (n > 9):
            n = n - 9
        sum += n
    for index in range(1, len(number), 2):
        sum += int(number[index])
    return sum

def check_number(number):
    sum = calculate_sum(number[:-1])
    if (sum % 10) + int(number[-1]) == 10:
        return True
    else:
        return False

class Account:
    account_list = []

    def __init__(self, number=None, pin=None, balance = None):
        if number == None:
            account_number = str(random.randint(1, 999999999))
            account_number = ("0" * (9 - len(account_number))) + account_number
            number = "400000" + account_number

            sum = calculate_sum(number)
            checksum = (10 - (sum % 10)) % 10

            pin = str(random.randint(1000, 9999))

            self.card_number = number + str(checksum)
            self.card_pin = pin
            self.balance = 0

            database.insert_card(self)
        else:
            self.card_number=number
            self.card_pin=pin
            self.balance=balance

    def add_income(self,income):
        self.balance += income
        database.update_balance(self)