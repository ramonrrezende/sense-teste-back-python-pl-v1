import psycopg2
from psycopg2.extras import RealDictCursor, execute_values
import os


class SenseDB:
    __db_conn = psycopg2.connect(
        host=os.environ.get("POSTGRES_HOST"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD"),
        database=os.environ.get("POSTGRES_DB"),
    )
    __cursor = __db_conn.cursor(cursor_factory=RealDictCursor)

    __date_format = """yyyy-MM-dd"T"HH:mm:ss.SSS"Z" """

    @staticmethod
    def commit():
        SenseDB.__db_conn.commit()

    @staticmethod
    def fetch():
        data = SenseDB.__cursor.fetchall()
        return data

    @staticmethod
    def insert_values(sql, values):
        execute_values(SenseDB.__cursor, sql, values)

    @staticmethod
    def execute_sql(sql):
        SenseDB.__cursor.execute(sql)

    @staticmethod
    def rollback():
        SenseDB.__db_conn.rollback()

    @staticmethod
    def date_format():
        return SenseDB.__date_format
