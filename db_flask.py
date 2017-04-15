from flask import Flask, render_template, jsonify, request
from os import environ
from flaskext.mysql import MySQL
from pymysql import InternalError

mysql = MySQL()

app = Flask(__name__)
db_info = open('db.txt')
app.config["MYSQL_DATABASE_USER"] = db_info.readline().strip('\n')
app.config["MYSQL_DATABASE_PASSWORD"] = db_info.readline().strip('\n')
app.config["MYSQL_DATABASE_DB"] = db_info.readline().strip('\n')
app.config["MYSQL_DATABASE_HOST"] = db_info.readline().strip('\n')
mysql.init_app(app)

conn = mysql.connect()

cursor = conn.cursor()

filething = open("./data/hampshirecolg_indico.csv", 'r')
filething.readline() #skip header

for line in filething:
    fields2 = []
    listOfFields = line.split(',')

    for li in listOfFields:
        li1 = li.lstrip("'")
        li2 = li1.rstrip("'")
        fields2.append(li2)

    tupleFields = tuple(fields2)
    date = tupleFields[0].strip('\n')
    handle = tupleFields[1]
    try:
        cursor.execute(('''
        select * from frontEnd where frontEnd.date = 'April2017' and frontEnd.handle = {}
        ''').format(handle))

        print(str(cursor.fetchall()))
    except:
        cursor.callproc('individualEntry', tupleFields)
        conn.commit()
filething.close()

#cursor.execute(('''select * from frontEnd where frontEnd.handle = {}'''.format("'HackSentivents'")))
cursor.execute(('''
select * from frontEnd where frontEnd.date = 'April2017' and frontEnd.handle = 'stuff'
'''))
cursor.close()
conn.close()
print(str(cursor.fetchall()))



app.run(debug=False, port = 5000)
