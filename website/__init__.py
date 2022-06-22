from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras

conn = psycopg2.connect(
    database = 'melex',
    user     = 'intern', 
    password = 'BAIT305C', 
    host     = '10.123.51.100', 
    port     = '5432'
    )

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dnsdvberjvgrtbod'

    from .views import views
    app.register_blueprint(views,url_prefix='/')

    return app 

