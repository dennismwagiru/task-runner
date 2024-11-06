Task Runner
==============

![CI Workflow](https://github.com/dennismwagiru/task-runner/actions/workflows/main.yml/badge.svg)

### Background

Implement a background task that will read the tasks from mongo db and execute it and then save the output to db

* Python flask server should run in a docker container.

### Tech-stack

* Tech-stack
    * [Docker](https://www.docker.com/) - a tool designed to make it easier to create, deploy, and run applications by using containers.
    * [Python 3](https://docs.python.org/3/) - an interpreted high-level general-purpose programming language
    * [Flask](https://flask.palletsprojects.com/en/2.0.x/) - a micro web framework written in python.
        * [MongoDB](https://www.mongodb.com/) - a cross platform document-oriented(NoSQL) database program
        * [Redis](https://redis.io/) - an in-memory data structure store used as a message broker.
        * [Celery](https://docs.celeryproject.org/en/stable/index.html) - an asynchronous task queue based on distributed message passing.

* Tests
    * [pytest](https://docs.pytest.org/en/6.2.x/) - a testing framework for python

###Install
___

    # clone the repository
    $ git clone https://github.com/dennismwagiru/task-runner
    $ cd task-runner

###Build and run image
___

    $ docker-compose up --build -d

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/8922e010ca1b9d8cb894?action=collection%2Fimport)

###Test
___

    $ docker-compose run --rm api sh -c "pytest && flake8"

###Test Coverage
___

    $ docker-compose run --rm api sh -c "pytest --cov-report term --cov=src/app src/tests/"

More tests can be added

## License
```
MIT License

Copyright (c) 2021 Dennis Joel Mwagiru

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF  TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```