FROM m.docker-registry.ir/python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=utf-8

ADD ./requirements.txt /temp/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /temp/requirements.txt
RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get install -y netcat

RUN mkdir -p /home/organization


WORKDIR /home/organization
COPY . .

EXPOSE 8081

CMD ["python", "manage.py", "runserver", "0.0.0.0:8081"]




