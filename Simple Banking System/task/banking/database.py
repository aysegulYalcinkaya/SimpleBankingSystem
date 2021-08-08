import sqlite3

import Account


def create_table():
    global conn
    conn = sqlite3.connect("card.s3db")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS card")
    cur.execute("CREATE TABLE card(id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)")
    conn.commit()


def insert_card(new_account):
    cur = conn.cursor()
    sql = "INSERT INTO card(number,pin,balance) VALUES ({},{},{})".format(new_account.card_number, new_account.card_pin,
                                                                          new_account.balance)
    cur.execute(sql)
    conn.commit()


def update_balance(account):
    cur = conn.cursor()
    sql = "UPDATE card SET balance={} where number={}".format(account.balance, account.card_number)
    cur.execute(sql)
    conn.commit()


def select_card(number):
    cur = conn.cursor()
    sql = "SELECT number,pin,balance FROM card where number={}".format(number)
    cur.execute(sql)
    data = cur.fetchone()
    if data:
        return Account.Account(*data)
    return False


def delete_card(account):
    cur = conn.cursor()
    sql = "DELETE FROM card where number={}".format(account.card_number)
    cur.execute(sql)
    conn.commit()


def login(card_number, pin):
    cur = conn.cursor()
    sql = "SELECT number,pin,balance FROM card where number={} and pin={}".format(card_number, pin)
    cur.execute(sql)
    data = cur.fetchone()
    if data:
        return Account.Account(*data)
    return False
