from unittest import result
from flask import Flask,jsonify
import os,ast,logging
import psycopg2

app = Flask(__name__)

# Connecting database
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host='postgres',
            port=5432,
            database='warehouse',
            user='postgres',
            password='postgres'
            )
        return conn
    except Exception as e:
        logging.error('Error connecting database at %s', exc_info=e)

# Get oil price from postgresql
@app.route('/getOilPrice')
def oil_price():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(''' SELECT * FROM oil_price; ''')
        result = {}
        columns = [col[0] for col in cur.description]
        result['status'] = 200
        result['data'] = [dict(zip(columns, row)) for row in cur.fetchall()]
        cur.close()
        conn.close()
        return jsonify(result)
    except Exception as e:
        logging.error('Error get dataset  at %s', exc_info=e)

@app.route('/')
def hello():
    return 'Ok'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
