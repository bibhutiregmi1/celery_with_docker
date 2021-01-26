from celery import Celery
import time


app = Celery('task',
	backend='redis://127.0.0.1:6379',
	broker='redis://127.0.0.1:6379')

@app.task()
def task():
	print("started some work")
	time.sleep(10)
	print("Task complete")