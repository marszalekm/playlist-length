FROM python:3.6-alpine

WORKDIR /usr/src/playlist-length

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/playlist-length/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/playlist-length/
