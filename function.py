import sqlite3


def register_user(name, age):
    connection = sqlite3.connect('user_db')
    cursor = connection.cursor()
    sql = f'INSERT INTO user (name, age) VALUES ("{name}", {age})'
    try:
        cursor.execute(sql)
        connection.commit()
        connection.close()
        return True
    except sqlite3.IntegrityError:
        print(f'Duplicated user name {name}')
        connection.close()
        return False


def all_show_user():
    connection = sqlite3.connect('user_db')
    cursor = connection.cursor()
    sql = 'SELECT * FROM user'
    users = cursor.execute(sql).fetchall()
    connection.close()

    for user in users:
        print(f'Name: {user[0]} Age: {user[1]}')


def one_show_user(name):
    connection = sqlite3.connect('user_db')
    cursor = connection.cursor()
    sql = f'SELECT * FROM user WHERE name = "{name}"'
    users = cursor.execute(sql).fetchall()
    connection.close()

    print(f'Name: {users[0][0]} Age: {users[0][1]}')


def one_show_age(name):
    connection = sqlite3.connect('user_db')
    cursor = connection.cursor()
    sql = f'SELECT age FROM user WHERE name = "{name}"'
    users = cursor.execute(sql).fetchall()
    connection.close()

    return users[0][0]


def update_user(old_name, new_name, age):
    connection = sqlite3.connect('user_db')
    cursor = connection.cursor()
    sql = f'UPDATE user SET name = "{new_name}", age = {age} WHERE name = "{old_name}"'
    cursor.execute(sql)
    connection.commit()
    connection.close()

    print(f'Update user: {new_name}')


def delete_user(name):
    connection = sqlite3.connect('user_db')
    cursor = connection.cursor()
    sql = f'DELETE FROM user WHERE name = "{name}"'
    cursor.execute((sql))
    connection.commit()
    connection.close()
