import pymysql
from pymysql import OperationalError

class DBConnection:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = None
        self.cursor = None

    def __enter__(self):
        try:
            self.connection = pymysql.connect(**self.db_config)
            self.cursor = self.connection.cursor()
            return self.cursor
        except (KeyError, OperationalError) as err:
            print(err.args)
            return None


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection and self.cursor:
            if exc_type:
                print(exc_type)
                print(exc_val)
                self.connection.rollback()
            else:
                self.connection.commit()
            self.cursor.close()
            self.connection.close()
            return True
