# celery_hello_world
Start the following:
	redis-server
	celery -A task worker --pool=solo --loglevel=info
	python app.py
