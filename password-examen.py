import sqlite3
import hashlib
from flask import Flask, request

app = Flask(__name__)
db_name = 'examen.db'

@app.route('/')
def index():
    return 'Examen – Gestión de claves y hash'

@app.route('/signup', methods=['POST'])
def signup():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS INTEGRANTES_HASH
           (USERNAME  TEXT    PRIMARY KEY NOT NULL,
            HASH      TEXT    NOT NULL);''')
    conn.commit()
    try:
        hash_value = hashlib.sha256(request.form['password'].encode()).hexdigest()
        c.execute("INSERT INTO INTEGRANTES_HASH (USERNAME, HASH) "
                  "VALUES (?, ?)", (request.form['username'], hash_value))
        conn.commit()
    except sqlite3.IntegrityError:
        return "Usuario ya registrado."

    print('Usuario:', request.form['username'], 'Hash:', hash_value)
    return "Registro exitoso"

@app.route('/login', methods=['POST'])
def login():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    query = "SELECT HASH FROM INTEGRANTES_HASH WHERE USERNAME = ?"
    c.execute(query, (request.form['username'],))
    record = c.fetchone()
    conn.close()
    if record and record[0] == hashlib.sha256(request.form['password'].encode()).hexdigest():
        return "Login exitoso"
    else:
        return "Usuario o contraseña incorrectos"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5800, ssl_context='adhoc')
