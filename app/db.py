# from . import mysql
import pymysql
from config import DB_CONFIG


def insert_url(long_url, short_code):
    # cur = mysql.connection.cursor()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO urls (long_url, short_code) VALUES (%s, %s)", (long_url, short_code))
    conn.commit()
    cur.close()

def get_long_url(short_code):
    # cur = mysql.connection.cursor()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT long_url FROM urls WHERE short_code = %s", (short_code,))
    result = cur.fetchone()
    cur.close()
    return result

def is_short_code_exists(short_code):
    # cur = mysql.connection.cursor()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM urls WHERE short_code = %s", (short_code,))
    exists = cur.fetchone() is not None
    cur.close()
    return exists


# db.py


def get_db_connection():
    return pymysql.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        db=DB_CONFIG["db"],
        charset=DB_CONFIG["charset"],
        cursorclass=pymysql.cursors.DictCursor,
        connect_timeout=DB_CONFIG["connect_timeout"],
        read_timeout=DB_CONFIG["read_timeout"],
        write_timeout=DB_CONFIG["write_timeout"],
    )
    
    
    

if __name__ == '__main__':
    insert_url("1234567890qwertyuiop121","qweqwe1")
    
    
    result = get_long_url("st")
    print(result["long_url"])
    
    result = is_short_code_exists("st")
    print(result)
    # # pass
