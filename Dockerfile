FROM phusion/baseimage:0.10.1

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# ...put your own build instructions here...
WORKDIR /app
COPY . /app
# ADD https://bootstrap.pypa.io/get-pip.py /app/get-pip.py
ADD ./socker_listen.py /app
ADD ./script.py /app

RUN add-apt-repository ppa:jonathonf/python-2.7 && \
    apt-get update && \
    apt-get install -y python2.7 &&\
    apt-get -y install netcat

RUN python2.7 get-pip.py
RUN pip install --upgrade pip
RUN pip install requests

RUN chmod -R 777 /app
# CMD ["python2.7", "main.py", "--cmd", "watcher"]
# CMD ["python3", "script.py", port]

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
