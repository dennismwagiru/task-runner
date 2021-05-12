FROM python:3.9-alpine
LABEL MAINTAINER="Dennis Joel <dennismwagiru@gmail.com>"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers

RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN adduser -D user
USER user
