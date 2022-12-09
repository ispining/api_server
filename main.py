"""
API for PowerSport CRM system...

"""

from flask import Flask
from flask import request, jsonify
import psycopg2

def  db_use() -> psycopg2:
    db = psycopg2.connect(database="powersport", user="postgres", password="armageddon", host="localhost", port=5432)
    sql = db.cursor()
    return db, sql



app = Flask(__name__)

@app.route('/')
def main_request():
    #db, sql = db_use()
    input_username = request.args.get('username')
    input_password = request.args.get('password')



    return str("PASS")

app.run()
