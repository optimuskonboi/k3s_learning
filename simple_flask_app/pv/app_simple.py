from flask import Flask
from typing import List, Dict
import mysql.connector
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

@app.route('/hehe')
def hehe():
    return 'Web App with Python Flask HEHE route!'

config = {
        'user': 'root',
        'password': 'phamvandan',
        'host': '10.43.72.2',
        'port': '3306',
        'database': 'my_flask_db'
    }

def test_table() -> List[Dict]:
    results = [{'abc':'123'}]
    connection = mysql.connector.connect(**config)
    print(connection)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM test')
    # for a in cursor:
        # print(a)
    results = [{name: password} for (id, name, password) in cursor]
    print(results)
    cursor.close()
    connection.close()

    return results

@app.route('/table')
def table():
    test_table()
    return json.dumps({'test_table': test_table()})

app.run(host='0.0.0.0', port=8555, debug=True)