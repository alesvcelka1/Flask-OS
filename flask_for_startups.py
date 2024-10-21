from flask import Flask, request, jsonify
import MySQLdb

app = Flask(__name__)

# Připojení k databázi
def get_db_connection():
    return MySQLdb.connect(
        host='db',  # název služby v docker-compose
        user='root',
        password='rootpassword',
        database='mydatabase'
    )

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/add', methods=['POST'])
def add_entry():
    data = request.json
    name = data.get('name')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO entries (name) VALUES (%s)', (name,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'status': 'success', 'name': name})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

