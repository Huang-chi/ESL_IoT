#FROM phusion/baseimage:0.10.1
From debian:stretch


# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# ...put your own build instructions here...
WORKDIR /app
COPY . /app
ADD https://bootstrap.pypa.io/get-pip.py /app/get-pip.py
# ADD .socker_listen.py /app/socker_listen.py
# ADD .script.py /app/script.py

RUN apt-get update && \
    apt-get install -y python3 &&\
    apt-get -y install netcat

RUN apt-get install vim -y

RUN python3 get-pip.py
RUN pip install --upgrade pip
RUN pip install requests

RUN chmod -R 777 /app
# CMD ["python2.7", "main.py", "--cmd", "watcher"]


# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 8002

WORKDIR /app
CMD ["python3", "./socket/script.py", "out"]
