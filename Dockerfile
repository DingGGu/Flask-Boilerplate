FROM python:3.7

WORKDIR /usr/src/app


ENV PIP_NO_CACHE_DIR false
ENV PYTHONPATH /usr/src/app

RUN pip install pipenv
RUN pip install uWSGI==2.0.18

COPY . .

RUN pipenv install --system --deploy

EXPOSE 9108

CMD uwsgi \
--enable-threads \
--chdir /usr/src/app \
--pythonpath /usr/src/app \
--http-socket :9108 \
--module wsgi:application