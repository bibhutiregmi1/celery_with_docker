FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get install -y redis-server
WORKDIR /opt/demo/
COPY /app .
RUN pip3 install -r requirements.txt
RUN chmod +x start.sh
RUN service redis-server restart
ENTRYPOINT ./start.sh