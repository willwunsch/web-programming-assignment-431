from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

host = 'http://127.0.0.1:5000/'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/delete', methods=['POST','GET'])
def delete():
    error = None

    # Show all patients in database immediately when you go to /delete page
    if request.method == 'GET':
        connection = sql.connect('database.db')
        cursor = connection.execute('SELECT * FROM users')
        return render_template('delete.html', error=error, result=cursor.fetchall())

    # POST request happens when you click button on /delete it will trigger this
    if request.method == 'POST':
        # Get name that is typed in the input
        first_name = request.form['FirstName']
        last_name = request.form['LastName']
        connection = sql.connect('database.db')
        cursor = connection.execute('SELECT * FROM users WHERE firstname = ? AND lastname = ?;',(first_name, last_name))

        if cursor.fetchone(): #RETURNS a Patient tuple if patient is in database
            connection.execute('DELETE FROM users WHERE firstname = ? AND lastname = ?; ',(first_name, last_name))
            connection.commit()
            cursor = connection.execute('SELECT * FROM users;')
            return render_template('delete.html', error=error, result=cursor.fetchall())
        else: #Returns nothing, = false if name isn't present
            error = 'Patient not in database'
            cursor = connection.execute('SELECT * FROM users;')
            return render_template('delete.html', error=error, result=cursor.fetchall())

    return render_template('delete.html', error=error)

@app.route('/name', methods=['POST', 'GET'])
def name():
    error = None
    if request.method == 'POST':
        result = valid_name(request.form['FirstName'], request.form['LastName'])
        if result:
            return render_template('input.html', error=error, result=result)
        else:
            error = 'invalid input name'
    return render_template('input.html', error=error)

def valid_name(first_name, last_name):
    connection = sql.connect('database.db')
    # AUTOINCREMENT will always give users a unique PID, always increasing in the database
    connection.execute(''
                       'CREATE TABLE IF NOT EXISTS users'
                       '(pid INTEGER PRIMARY KEY AUTOINCREMENT,'
                       ' firstname TEXT NOT NULL,'
                       ' lastname TEXT NOT NULL);')
    connection.execute(''
                       'INSERT INTO users (firstname, lastname) '
                       'VALUES (?,?);', (first_name, last_name))

    connection.commit()
    cursor = connection.execute('SELECT * FROM users;')
    return cursor.fetchall()


if __name__ == "__main__":
    app.run()


