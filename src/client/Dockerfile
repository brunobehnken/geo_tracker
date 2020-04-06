FROM python:3.9.0a4-buster

# Install necessary packages
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y apt-utils
RUN apt-get install -y python-pip python-dev

# copy client source into container
COPY . .

# install requirements
#RUN pip install -r requirements.txt

# exposes the port that will be used by the container to send data to server
EXPOSE 5678

########################### FOR TEST PURPOSES
RUN apt-get install -y net-tools iputils-ping curl vim
########################### END FOR TEST PURPOSES

# run the client program
ENTRYPOINT ["python"]
CMD ["node_client.py"]
