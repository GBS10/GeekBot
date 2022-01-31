from flask import Flask, request, jsonify, make_response
from flaskext.mysql import MySQL
import pymysql 
import flask

#Creating flask instance
app = Flask(__name__)

#Initiating MySQL
mysql = MySQL()
   
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'demo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

#Function to enter a new word and its definition into te WORDDEF table
@app.route('/add/<word>/<definition>', methods =['POST'])
def register(word, definition):
        w = word 
        d = definition
        conn = mysql.connect() #Establishing connection with MySQL server
        cursor = conn.cursor(pymysql.cursors.DictCursor) #Creating a cursor
        cursor.execute('INSERT INTO WORDDEF VALUES(%s, %s)', (w, d)) #Executing insert command
        conn.commit() #Commiting the changes to end the transaction
        print("Connected")
        return flask.Response(status=200)
if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)

