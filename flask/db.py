from flask import Flask, request, jsonify, make_response
from flaskext.mysql import MySQL
import pymysql 
import flask
app = Flask(__name__)

mysql = MySQL()
   
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'demo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/add/<word>/<definition>', methods =['POST'])
def register(word, definition):
        w = word 
        d = definition
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('INSERT INTO WORDDEF VALUES(%s, %s)', (w, d))
        conn.commit()
        print("Connected")
        return flask.Response(status=200)
if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)

