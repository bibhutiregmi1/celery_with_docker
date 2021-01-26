# celery_hello_world
Start the following:
	redis-server
	celery -A task worker --pool=solo --loglevel=info
	python app.py

check ip using
sudo docker network inspect bridge
http://172.17.0.2:5000/home