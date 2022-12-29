FROM python:3.9-alpine3.13
LABEL maintainer="oscar.cerda.acuna@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    # Upgrade pip.
    /py/bin/pip install --upgrade pip && \
    # Install packages for Psycopg2 adaptor. \
    # - Install used dependencies (use and installation).
    apk add --update --no-cache postgresql-client && \
    # - Install installation dependencies (temporal).
    apk add --update --no-cache --virtual .tmp-build-deps \
      build-base postgresql-dev musl-dev && \
    # Install requirements.
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    # Remove temporal files.
    rm -rf /tmp && \
    # Remove temporal dependencies for installing psycopg2.
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user
