import Account
import database
conn = None

def display_main_menu():
    print('''1. Create an account
2. Log into account
0. Exit''')


def display_account_menu():
    print('''1. Balance
2. Add Income
3. Do Transfer
4. Close Account
5. Log out
0. Exit''')


def account_operations(account):
    display_account_menu()
    ch = int(input())
    while ch != 0:
        if ch == 1:
            print("Balance: {}".format(account.balance))
        if ch == 2:
            print("Enter income:")
            income = int(input())
            account.balance+=income
            database.update_balance(account)
        if ch == 3:
            print("Transfer")
            print("Enter card number:")
            transfer_card_number = input()
            if Account.check_number(transfer_card_number):
                transfer_account = database.select_card(transfer_card_number)
                if transfer_account:
                    if transfer_account.card_number == account.card_number:
                        print("You can't transfer money to the same account!")
                    else:
                        print("Enter how much money you want to transfer:")
                        amount = int(input())
                        if amount > account.balance:
                            print("Not enough money!")
                        else:
                            transfer_account.balance += amount
                            account.balance -= amount
                            database.update_balance(account)
                            database.update_balance(transfer_account)
                else:
                    print("Such a card does not exist.")
            else:
                print("Probably you made a mistake in the card number. Please try again!")
        elif ch == 4:
            database.delete_card(account)
            print("The account has been closed!")
            account = None
            return 2
        elif ch == 5:
            account = None
            print("You have successfully logged out!")
            return 2
        elif ch == 0:
            continue
        else:
            print("Wrong selection!")
        display_account_menu()
        ch = int(input())
    print("Bye!")
    return 0


database.create_table()

display_main_menu()
choice = int(input())

while choice != 0:
    if choice == 1:
        account = Account.Account()
        print("Your card has been created")
        print("Your card number:")
        print(account.card_number)
        print("Your card PIN:")
        print(account.card_pin)
    elif choice == 2:
        print("Enter your card number:")
        input_card_number = input()
        print("Enter your PIN:")
        input_pin = input()
        account = database.login(input_card_number, input_pin)
        if account:
            print("You have successfully logged in!")
            state = account_operations(account)
            if state == 0:
                break
        else:
            print("Wrong card number or PIN!")
    elif choice == 0:
        continue
    else:
        print("Wrong selection!")
    display_main_menu()
    choice = int(input())
print("Bye!")
