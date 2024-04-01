import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Christian Seidle in 3308!'

app.route('/db_test')
def testing():
    conn = psycopg2.connect('postgres://lab10_sql_user:w9IrSpCQMvqvMCZMF5HVckOnhSbGC4mv@dpg-co5h25uv3ddc73911mh0-a/lab10_sql')
    conn.close()
    return 'Connected to the database!'

app.route('/db_create')
def creating():
    conn = psycopg2.connect('postgres://lab10_sql_user:w9IrSpCQMvqvMCZMF5HVckOnhSbGC4mv@dpg-co5h25uv3ddc73911mh0-a/lab10_sql')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return 'Basketball table created!'
