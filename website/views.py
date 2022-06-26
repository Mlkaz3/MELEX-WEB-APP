from logging import error
import re
from unicodedata import category
from flask import Blueprint, jsonify,request, render_template, flash, redirect, url_for
from graphviz import render
import psycopg2 #pip install psycopg2 
import psycopg2.extras
from . import conn
import string


views = Blueprint('views', __name__)

@views.route('/',methods=['GET', 'POST'])
def Index():
    language = ""
    oov  =""
    wordstatus =""
    list_users = []
    return render_template('index.html',list_users = list_users,language=language,oov=oov,wordstatus=wordstatus)


@views.route('/filter',methods=['GET', 'POST'])
def filter():
    language = ""
    oov  =""
    wordstatus =""

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM tokens FETCH FIRST 50 ROWS ONLY"
    cur.execute(s) # Execute the SQL
    list_users = cur.fetchall()

    if request.method == 'POST':
        # get value of each radio button
        language = request.form.get('language')
        oov = request.form.get('oov')
        wordstatus = request.form.get('wordstatus')

        if language!=None and oov!=None and wordstatus!=None:
            s = "SELECT * FROM tokens WHERE langid = " + language + " AND oov = " + oov + " AND tokenstatus = '" + wordstatus + "' FETCH FIRST 50 ROWS ONLY"
        elif language!=None and oov!=None:
            s = "SELECT * FROM tokens WHERE langid = '" + language + "' AND oov = " + oov + " FETCH FIRST 50 ROWS ONLY"
        elif oov!=None and wordstatus!=None:
            s = "SELECT * FROM tokens WHERE oov = " + oov + " AND tokenstatus = '" + wordstatus + "' FETCH FIRST 50 ROWS ONLY"
        elif language!=None and wordstatus!=None:
            s = "SELECT * FROM tokens WHERE langid = '" + language + " AND tokenstatus = '" + wordstatus + "' FETCH FIRST 50 ROWS ONLY"
        elif language!=None:
            s = "SELECT * FROM tokens WHERE langid = " + language + " FETCH FIRST 50 ROWS ONLY"
        elif oov!=None:
            s = "SELECT * FROM tokens WHERE oov = " + oov + " FETCH FIRST 50 ROWS ONLY"
        elif wordstatus!=None:
            s = "SELECT * FROM tokens WHERE tokenstatus = '" + wordstatus + "' FETCH FIRST 50 ROWS ONLY"
        
        cur.execute(s) # Execute the SQL
        list_users = cur.fetchall()

    return render_template('filter.html', list_users = list_users,language=language,oov=oov,wordstatus=wordstatus)


@views.route('/search',methods=['GET', 'POST'])
def search():
    token=""
    if request.method == 'POST':
        search_term = request.form.get('search')

        if len(search_term)<1:
            flash('Search term is too short', category='error')
        else:
            cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            s = "SELECT *, CASE WHEN langID='1' THEN 'English' WHEN langID='2' THEN 'Malay'  WHEN langID='3' THEN 'Chinese' WHEN langID='4' THEN 'Others' END FROM tokens WHERE token = '" + search_term.lower() + "'"
            cur.execute(s) # Execute the SQL
            token = cur.fetchall()
            flash('Searched!', category='success')

    return render_template('search.html', token=token)

@views.route('/library', methods=['GET','POST'])
def library():
    alphabet = None
    letter = string.ascii_lowercase

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM tokens FETCH FIRST 50 ROWS ONLY"
    cur.execute(s) # Execute the SQL
    output_list = cur.fetchall()

    if request.method == 'POST':
        alphabet = request.form.get('alphabet')

        if alphabet!=None: 
            s = "SELECT * FROM tokens WHERE token LIKE '" + alphabet+ "%' ORDER BY token FETCH FIRST 50 ROWS ONLY "
            cur.execute(s) # Execute the SQL
            output_list = cur.fetchall()

    return render_template('library.html', letter=letter, output_list=output_list, alphabet=alphabet)



# @views.route('/search',methods=['GET', 'POST'])
# def search():
#     token=""
#     if request.method == 'POST':
#         search_term = request.form.get('search')

#         if len(search_term)<1:
#             flash('Search term is too short', category='error')
#         else:
#             cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#             s = "SELECT * FROM tokens WHERE token = '" + search_term.lower() + "'"
#             cur.execute(s) # Execute the SQL
#             token = cur.fetchall()
#             flash('Searched!', category='success')

#     return render_template('search.html', token=token)



