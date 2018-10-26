from flask import Flask
# from flask_script import Manager
from flask import render_template
from flask_bootstrap import Bootstrap
from flask import url_for
import os
import sys
# reload(sys) 
# sys.setdefaultencoding('utf8')

app = Flask(__name__)


@app.route('/')
def index():
	return 'INDEX';

@app.route('/<cname>/<sname>')
def category(cname, sname):
	return cname + ":" + sname
	pass



if __name__ == '__main__':
	Billboard = 'sadfasdfdafasdfasdfad';

	app.run(debug = True)

