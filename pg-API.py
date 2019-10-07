from flask import Flask
import psycopg2
import json

app = Flask(__name__)


conn = psycopg2.connect(host="192.168.1.21",database="postgres", user="postgres", password="")


cur = conn.cursor()
    
# execute a statement
print('PostgreSQL database version:')
cur.execute('SELECT version()')

# display the PostgreSQL database server version
db_version = cur.fetchone()
print(db_version)
   
   # close the communication with the PostgreSQL
cur.close()

conn.close()
print('Database connection closed.')



def initial():
    conn = psycopg2.connect(host="192.168.1.21",database="postgres", user="postgres", password="")
    cur = conn.cursor()
    cur.execute('SELECT * from axtest')
    db_version = cur.fetchone()
    print(type(db_version))
    print json.dumps(db_version)
    return db_version

initial()

@app.route("/")
def main():
    initial()

if __name__ == '__main__':
    app.run()
