from flask import *
import pr11.py
    from functools import wraps
    import pymysql

    app = Flask(__name__)
    @app.route('/')
    def home():
       return render_template('index.html')

    @app.route('/generate')
	def generate():
  	 	print 'Hello World!'
   		return render_template('process.html')