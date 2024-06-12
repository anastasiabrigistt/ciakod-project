import sqlite3
import crypto


def __connect_to_db():
    return sqlite3.connect('db.sqlite3')


def create_db():
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()

    with open('db.sql', 'r') as f:
        cursor.executescript(f.read())

    db.commit()
    cursor.close()
    db.close()


def insert_data(category, service, login, password):
    db = __connect_to_db()
    cursor = db.cursor()

    sql = ('INSERT INTO services (category, service, login, password) '
           'VALUES (?, ?, ?, ?)')
    val = (category, service, login, password)

    cursor.execute(sql, val)
    db.commit()

    cursor.close()
    db.close()


def update_data(id, service, login, password):
    db = __connect_to_db()
    cursor = db.cursor()

    sql = (f'UPDATE services SET service=?, login=?, password=?'
           f'where id={id}')
    val = (service, login, password)

    cursor.execute(sql, val)
    db.commit()

    cursor.close()
    db.close()


def get_all_data():
    db = __connect_to_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM services")

    rows = cursor.fetchall()

    cursor.close()
    db.close()

    return rows


if __name__ == '__main__':
    create_db()
    insert_data('web', 'test', 'test', 'test')
    insert_data('apps', 'test1', 'test1', 'test1')
    insert_data('web', 'test2', 'test2', 'test2')
