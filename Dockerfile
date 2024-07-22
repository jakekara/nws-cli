# Use to test that the Python package builds

FROM python:3.12-alpine

COPY . /code

WORKDIR /code

RUN pip install .

WORKDIR /

RUN rm -rf /code

RUN nws --help

ENTRYPOINT ["nws"]