import sqlite3


def create_db():
    conn = sqlite3.connect("archive.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE passwords (password int)""")
    cursor.execute("""CREATE TABLE users (password int, username str, variant str)""")
    conn.commit()
    conn.close()


class WorkWithDB:
    def __init__(self):
        self.conn = sqlite3.connect("archive.db")
        self.cursor = self.conn.cursor()
        self.conn.row_factory = sqlite3.Row

    def add_password(self, password: int):
        self.cursor.execute("""INSERT INTO passwords VALUES (?)""", (password, ))
        self.cursor.execute("""INSERT INTO users VALUES (?, ?, ?)""", (password, "", ""))
        self.conn.commit()

    def delete_password(self, password: int):
        self.cursor.execute(f"""DELETE FROM passwords WHERE password = '{password}'""")
        self.cursor.execute(f"""DELETE FROM users WHERE password = '{password}'""")
        self.conn.commit()

    def get_password(self):
        passwords = self.cursor.execute("""SELECT * FROM passwords""").fetchall()
        return [i[0] for i in passwords]

    def add_user(self, password: int, username: str):
        self.cursor.execute(f"""UPDATE users SET username = ? WHERE password = ?""",
                            (username, password))
        self.conn.commit()

    def change_user(self, password: int, username: str, variant: str):
        self.cursor.execute(f"""UPDATE users 
                                SET variant = '{variant}'
                                WHERE password = '{password}' and username = '{username}'""")
        self.conn.commit()

    def get_users(self):
        users_info = self.cursor.execute("""SELECT * FROM users""").fetchall()
        return [{"password": i[0], "username": i[1], "variant": i[2]} for i in users_info]


if __name__ == '__main__':
    create_db()