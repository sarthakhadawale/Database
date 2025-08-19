from flask import Flask, render_template, request,render_template_string
import sqlite3

app = Flask(__name__)

# Create database table if not exists
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        phone TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        gender TEXT NOT NULL,
                        salary REAL NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        age = request.form['age']
        gender = request.form['gender']
        salary = request.form['salary']

        # Insert data into database
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, phone, age, gender, salary) VALUES (?, ?, ?, ?, ?)",
                       (name, phone, age, gender, salary))
        conn.commit()
        conn.close()

        return render_template_string (f"""
            <h1> {name},Your data is daved succesfully... </h1>
            <h3> Thank you...</h3>
        """)

if __name__ == '__main__':
    init_db()  # Initialize database before starting app
    app.run(debug=True)
