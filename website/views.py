from unicodedata import category
from flask import Blueprint, jsonify,request, render_template, flash
from graphviz import render
import psycopg2 #pip install psycopg2 
import psycopg2.extras
from . import conn

views = Blueprint('views', __name__)

@views.route('/',methods=['GET', 'POST'])
def Index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM tokens FETCH FIRST 5 ROWS ONLY"
    cur.execute(s) # Execute the SQL
    list_users = cur.fetchall()
    return render_template('index.html', list_users = list_users)

@views.route('/test',methods=['GET', 'POST'])
def Testing():
    return render_template('test.html')

