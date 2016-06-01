#coding:utf-8
import sae
import os , sys
app_root = os.path.dirname(__file__) 
sys.path.insert(0, os.path.join(app_root, 'beautifulsoup4-4.4.1')) 
#sae.add_vendor_dir('Lib/site-packages/lxml.egg/lxml')
from run import app
application = sae.create_wsgi_app(app)
