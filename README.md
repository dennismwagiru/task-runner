Task Runner
==============

![CI Workflow](https://github.com/dennismwagiru/task-runner/actions/workflows/main.yml/badge.svg)

This is an interview project.

Install
--------
    # clone the repository
    $ git clone https://github.com/dennismwagiru/task-runner
    $ cd task-runner

Build Docker image

    $ docker-compose build

#Run
___

    $ docker-compose up -d

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/8922e010ca1b9d8cb894?action=collection%2Fimport)

#Test
___

    $ docker-compose run --rm api sh -c "pytest && flake8"
