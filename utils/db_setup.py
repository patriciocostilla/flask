import sqlite3
from .constants import DB_NAME

create_table_sql = """
    create table todos(
        id int,
        content text
    )
"""

con = sqlite3.connect(DB_NAME)

cur = con.cursor()

cur.execute(create_table_sql)

