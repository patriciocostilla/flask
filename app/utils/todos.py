import sqlite3
from .constants import DB_NAME

def fetch_all():
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("select * from todos")
    results = cur.fetchall()
    con.close()
    results = [{"id": result[0], "content": result[1]} for result in results]
    return results

def create(content):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("select max(id) from todos")
    max_id = cur.fetchone()[0]
    if max_id == None:
        max_id = 0
    new_id = max_id + 1
    cur.execute(f"insert into todos values({new_id}, '{content}')")
    con.commit()
    con.close()
    return fetch_one(new_id)

def fetch_one(id):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute(f"select * from todos where id = {id}")
    result = cur.fetchone()
    con.close()
    if result == None:
        return None
    return {"id": result[0], "content": result[1]}

def update(id, content):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute(f"update todos set content = '{content}' where id = {id}")
    con.commit()
    con.close()
    return fetch_one(id)

def delete(id):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute(f"delete from todos where id = {id}")
    con.commit()
    con.close()
    return id