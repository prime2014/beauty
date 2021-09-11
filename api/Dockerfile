FROM python:3.8-slim-buster

ENV PYTHONBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*


WORKDIR /beauty/

COPY ./api/requirements.txt /beauty/

RUN python -m pip install --upgrade pip

RUN pip install -r ./api/requirements.txt && useradd -ms /bin/bash 1000

COPY --chown=1000:1000 ./api/* /beauty/

USER 1000
