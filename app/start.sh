#!/bin/bash
redis-server & 
python3 main.py &
celery -A task worker --pool=solo --loglevel=info