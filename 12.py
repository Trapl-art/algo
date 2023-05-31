from flask import Flask, request

app = Flask(__name__)
import sqlite3



@app.route('/store/<id>/', methods=['GET'])
def store_id(id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    sqlite_select_query = """SELECT * from STORE"""
    cursor.execute(sqlite_select_query)
    rec = cursor.fetchall()
    f, t = False, ''
    for row in rec:
        if str(row[1]) == str(id):
            f, t = True, row[0]
    cursor.close()
    print({'status': 'ok', 'exist': f, 'name': t})
    return {'status': 'ok', 'exist': f, 'name': t}




@app.route('/store/', methods=['POST'])
def new_store():
    id = request.json['id']
    name = request.json['name']
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    sqlite_select_query = """SELECT * from STORE"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    for row in records:
        if id in row:
            return {'status': 'ok'}
    sqlite_select_param = '''INSERT INTO STORE (id, name) VALUES (?, ?);'''
    data = (id, name)
    cursor.execute(sqlite_select_param, data)
    connection.commit()
    return {'status': 'ok'}


@app.route('/product/<id>/', methods=['GET'])
def check_product(id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    sqlite_select_query = """SELECT * from PRODUCT"""
    cursor.execute(sqlite_select_query)
    rec = cursor.fetchall()
    f, t = False, ''
    for row in rec:
        if str(row[1]) == str(id):
            f, t = True, row[0]
    cursor.close()
    print({'status': 'ok', 'exist': f, 'name': t})
    return {'status': 'ok', 'exist': f, 'name': t}



@app.route('/product/', methods=['POST'])
def aa():
    id = request.json['id']
    name = request.json['name']
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    sqlite_select_query = """SELECT * from PRODUCT"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    for row in records:
        if id in row:
            return {'status': 'ok'}
    sqlite_select_param = '''INSERT INTO PRODUCT (id, name) VALUES (?, ?);'''
    data = (id, name)
    cursor.execute(sqlite_select_param, data)
    connection.commit()
    return {'status': 'ok'}



app.run(host='0.0.0.0', port='5001')