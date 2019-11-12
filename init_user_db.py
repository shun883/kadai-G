import sqlite3


def main():
    connection = sqlite3.connect('user_db')
    cursor = connection.cursor()
    sql = 'CREATE TABLE user (name text, age integer)'
    cursor.execute(sql)
    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
