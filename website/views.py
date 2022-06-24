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
    s = "SELECT * FROM tokens FETCH FIRST 50 ROWS ONLY"
    cur.execute(s) # Execute the SQL
    list_users = cur.fetchall()
    return render_template('index.html', list_users = list_users)

@views.route('/search',methods=['GET', 'POST'])
def search():
    token=""
    if request.method == 'POST':
        search_term = request.form.get('search')

        if len(search_term)<1:
            flash('Search term is too short', category='error')
        else:
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            s = "SELECT * FROM tokens WHERE token = '" + search_term.lower() + "'"
            cur.execute(s) # Execute the SQL
            token = cur.fetchall()
            flash('Searched!', category='success')

    return render_template('search.html', token=token)



