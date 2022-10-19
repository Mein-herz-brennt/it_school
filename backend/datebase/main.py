import sqlite3


def create_datebase():
    conn = sqlite3.connect("third.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE venue (user_id int, user_name str, data str)""")
    conn.commit()
    conn.close()


class DateBase:
    def __init__(self):
        self.conn = sqlite3.connect("third.db")
        self.cursor = self.conn.cursor()
        self.conn.row_factory = sqlite3.Row

    def add_user_in_table(self, user_id: int, user_name: str, data: str) -> bool:
        """function for add people in datebase"""
        self.cursor.execute("""INSERT INTO users VALUES (?, ?, ?)""", (user_id, user_name, data))
        self.conn.commit()
        self.conn.close()
        return True

    def delete_user(self, user_name: str) -> bool:
        self.cursor.execute(f"""DELETE FROM users WHERE  user_name = '{user_name}' """)
        self.conn.commit()
        self.conn.close()
        return True


if __name__ == '__main__':
    # create_datebase()
    # DateBase().add_user_in_table(1377624, "asfsfsd", "user")
    DateBase().delete_user("asfsfsd")
