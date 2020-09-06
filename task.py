from celery import Celery
import time


app = Celery('task',
	backend='redis://localhost:6379',
	broker='redis://localhost:6379')


@app.task()
def task():
	print("started some work")
	time.sleep(10)
	print("Task complete")