from flask import Flask
from task import task
import time


app=Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
	return 'Hello World' 

@app.route('/home', methods=['GET'])
def home():
	task.delay()
	return 'home World' 


if __name__ == '__main__':
	app.run(host='0.0.0.0')