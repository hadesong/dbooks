#coding:utf-8
import sae
import os , sys
sae.add_vendor_dir('beautifulsoup4-4.4.1')
#sae.add_vendor_dir('Lib/site-packages/lxml.egg/lxml')
from run import app
application = sae.create_wsgi_app(app)
