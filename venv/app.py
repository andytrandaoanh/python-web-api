from flask import Flask, render_template
from flask import jsonify, request
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
from flask_cors import CORS
import dbconn
from flask import request
from data_process import fetch_data


app = Flask(__name__)
CORS(app)
mysql = MySQL(cursorclass=DictCursor)
dbconn.set_conn_param(app)
mysql.init_app(app)



@app.route('/words')
def words():
	sql_statement = "select * from words order by word_form limit 100;"
	resp = fetch_data(mysql, sql_statement)
	return  resp
		  #return 'hello world!'
@app.route('/query/<word>',  methods = ['GET'])
def query_word(word):
	if request.method == 'GET':
		sql_statement = "select * from  words where word_form like '" + word +"' order by book_id;"
		resp = fetch_data(mysql, sql_statement)
		return  resp 		
	