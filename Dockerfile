FROM python:3.9-alpine
LABEL MAINTAINER="Dennis Joel <dennismwagiru@gmail.com>"

# set work directory
WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt  .
#RUN apk add --update --no-cache --virtual .tmp-build-deps \
#      gcc libc-dev linux-headers

RUN pip install -r requirements.txt
#RUN apk del .tmp-build-deps

# copy project
COPY . .
