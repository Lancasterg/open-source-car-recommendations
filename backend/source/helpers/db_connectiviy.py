import sqlite3 as sl


class DbAccess:

    def __init__(self, env: str):
        if env == "local":
            self.con = sl.connect('my-test.db')
