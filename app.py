from flask import Flask, app
import time
from flask_restful import Api, Resource
from task import task


app=Flask(__name__)
api = Api(app)


class Main(Resource):
	def get(self):
		task.delay()
		return 'Hello World' 


api.add_resource(Main,'/')

if __name__ == '__main__':
	app.run()

