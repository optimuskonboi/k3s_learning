from flask import Flask
from typing import List, Dict
import mysql.connector
import json

DBNAME=  "my_flask_db"
TBNAME = "test"
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
        'host': '42.96.43.141',
        'port': '31000',
        # 'database': DBNAME
    }

def delete_database():
    results = [{'abc':'123'}]
    print('connect')
    connection = mysql.connector.connect(**config)
    print(connection)
    cursor = connection.cursor()
    cursor.execute("DROP DATABASE "+DBNAME)
    return results

def create_database():
    results = [{'abc':'123'}]
    connection = mysql.connector.connect(**config)
    print(connection)
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE "+ DBNAME)
    config["database"] = DBNAME
    return results

def create_table():
    results = [{'abc':'123'}]
    config["database"] = DBNAME
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE {0} (name VARCHAR(255), address VARCHAR(255))".format(TBNAME))
    sql = f"INSERT INTO {TBNAME} (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    cursor.execute(sql, val)
    sql = f"INSERT INTO {TBNAME} (name, address) VALUES (%s, %s)"
    val = ("Johny", "Highway 22")
    cursor.execute(sql, val)
    connection.commit()
    return results

def test_table() -> List[Dict]:
    results = [{'abc':'123'}]
    config["database"] = DBNAME
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {TBNAME}')
    # for a in cursor:
    #     print(a)
    results = [{name: address} for (name, address) in cursor]
    print(results)
    cursor.close()
    connection.close()

    return results

@app.route('/create_new_db')
def create_new_db():
    create_database()
    create_table()
    return "ok"

@app.route('/refresh_database')
def refresh_database():
    delete_database()
    create_database()
    create_table()
    return "ok"

@app.route('/table')
def table():
    test_table()
    return json.dumps({'test_table': test_table()})

app.run(host='0.0.0.0', port=8555, debug=True)

# print(create_database())