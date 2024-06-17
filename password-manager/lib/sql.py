import os

import sqlite3
from dotenv import load_dotenv

import lib.crypto as crypto
from lib.resource import resource_path


def __connect_to_db():
    return sqlite3.connect('db.sqlite3')


def create_db():
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()

    path = resource_path('db.sql')
    with open(path, 'r') as f:
        cursor.executescript(f.read())

    db.commit()
    cursor.close()
    db.close()


def insert_data(category, service, login, password):
    load_dotenv()
    db = __connect_to_db()
    cursor = db.cursor()

    password = crypto.encrypt_pass(password, os.getenv('KEY'))

    sql = ('INSERT INTO services (category, service, login, password) '
           'VALUES (?, ?, ?, ?)')
    val = (category, service, login, password)

    cursor.execute(sql, val)
    db.commit()

    cursor.close()
    db.close()


def update_data(id, service, login, password):
    load_dotenv()
    db = __connect_to_db()
    cursor = db.cursor()

    password = crypto.encrypt_pass(password, os.getenv('KEY'))

    sql = (f'UPDATE services SET service=?, login=?, password=?'
           f'where id={id}')
    val = (service, login, password)

    cursor.execute(sql, val)
    db.commit()

    cursor.close()
    db.close()


def delete_data(id):
    db = __connect_to_db()
    cursor = db.cursor()

    sql = 'DELETE FROM services WHERE id=?'
    val = (id,)

    cursor.execute(sql, val)
    db.commit()

    cursor.close()
    db.close()


def get_all_data():
    load_dotenv()
    db = __connect_to_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM services")

    rows = list(cursor.fetchall())

    for i in range(len(rows)):
        new_row = list(rows[i])
        new_row[4] = crypto.decrypt_pass(rows[i][4], os.getenv('KEY'))
        rows[i] = new_row

    cursor.close()
    db.close()

    return rows


def get_by_id(idx):
    load_dotenv()
    db = __connect_to_db()
    cursor = db.cursor()

    cursor.execute(f"SELECT * FROM services WHERE id={idx}")

    row = list(cursor.fetchone())

    row[4] = crypto.decrypt_pass(row[4], os.getenv('KEY'))

    cursor.close()
    db.close()

    return row


def truncate():
    db = __connect_to_db()
    cursor = db.cursor()

    cursor.execute(f"DELETE FROM services")
    db.commit()

    cursor.close()
    db.close()


if __name__ == '__main__':
    create_db()
    insert_data('web', 'test', 'test', 'test')
    insert_data('apps', 'test1', 'test1', 'test1')
    insert_data('web', 'test2', 'test2', 'test2')
