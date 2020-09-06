from flask import Flask
from task import task
import time


app=Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
	task.delay()
	return 'Hello World' 


if __name__ == '__main__':
	app.run()