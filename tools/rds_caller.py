import pymysql

from conf import mysql_conf

conn = pymysql.connect(**mysql_conf)
cur = conn.cursor()

def create_db(name):
    resp = cur.execute(f'create database {name}')
    print(resp)
    print(cur.fetchall())
    print('done')

if __name__ == "__main__":
    create_db('paper')
