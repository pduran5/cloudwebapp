from flask import Flask, render_template, request, redirect, url_for
import pymysql
from config import HOST, USER, PASSWORD, DATABASE

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

@app.route('/')
def index():
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        usuarios = cursor.fetchall()
    finally:
        conn.close()
    
    return render_template('index.html', usuarios=usuarios)

@app.route('/agregar', methods=['POST'])
def agregar():
    name = request.form['name']
    email = request.form['email']

    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
        conn.commit()
    finally:
        conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
