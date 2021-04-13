import pymysql

from conf import mysql_conf

conn = pymysql.connect(**mysql_conf)
cur = conn.cursor()

def create_db(name):
    resp = cur.execute(f'create database {name}')
    print(resp)
    print(cur.fetchall())
    print('done')

def delete_db(name):
    resp = cur.execute(f'drop database {name}')
    print(resp)
    print(cur.fetchall())
    print('done')

if __name__ == "__main__":
    # delete_db('paper')
    create_db('paper')
