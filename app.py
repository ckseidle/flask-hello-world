
from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Christian Seidle in 3308!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect('postgres://lab10_sql_user:w9IrSpCQMvqvMCZMF5HVckOnhSbGC4mv@dpg-co5h25uv3ddc73911mh0-a/lab10_sql')
    conn.close()
    return 'Connected to the database!'

@app.route('/db_create')
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

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect('postgres://lab10_sql_user:w9IrSpCQMvqvMCZMF5HVckOnhSbGC4mv@dpg-co5h25uv3ddc73911mh0-a/lab10_sql')
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number Values)
        VALUES ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'Golden State', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return 'Basketball table populated!'

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect('postgres://lab10_sql_user:w9IrSpCQMvqvMCZMF5HVckOnhSbGC4mv@dpg-co5h25uv3ddc73911mh0-a/lab10_sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Basketball')
    records = cur.fetchall()
    conn.close()
    response_string = ''
    response_string+='<table>'
    for player in records:
        response_string+='<tr>'
        for info in player:
            response_string+='<td>{}</td>'.format(info)
        response_string+='</tr>'
    response_string+='</table>'
    return response_string

app.route('/db_drop')

