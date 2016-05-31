#coding:utf-8
from app_package import app
from flask import render_template , request 
import urllib2 , urllib 
from search import search_blue
from search import today
import sys


reload(sys)
sys.setdefaultencoding( "utf-8" )


app.register_blueprint(search_blue)


@app.errorhandler(404)
def page_not_found(value):
    return render_template('404.html') , 404


@app.route('/')
@app.route('/index')
def index():
    html =today()
    return render_template('index.html' , html  = html)













