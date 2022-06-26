from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import psycopg2 #pip install psycopg2 
import psycopg2.extras
# from flask_migrate import Migrate

conn = psycopg2.connect(
    database = 'melex',
    user     = 'intern', 
    password = 'BAIT305C', 
    host     = '10.123.51.100', 
    port     = '5432'
    )

db = ""

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dnsdvberjvgrtbod'

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://intern:BAIT305C@10.123.51.100:5432/melex"
    db=SQLAlchemy(app)
    # migrate = Migrate(app, db)

    from .views import views
    app.register_blueprint(views,url_prefix='/')

    # from .actions import actions
    # app.register_blueprint(actions,url_prefix='/')

    return app 

