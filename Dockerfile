FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

# -- Install Application into container:
RUN set -ex && mkdir /code
COPY . /code
WORKDIR /code

# -- Adding Pipfiles
ONBUILD COPY Pipfile Pipfile
ONBUILD COPY Pipfile.lock Pipfile.lock

# -- Install dependencies:
RUN set -ex && pip install -U pipenv
RUN set -ex && pipenv install --deploy --system