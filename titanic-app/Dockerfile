FROM python:3.6

LABEL maintainer "Calvin Tran <trandcanh@gmail.com>"

ENV APP_HOME /app

RUN mkdir -p $APP_HOME

WORKDIR $APP_HOME

COPY requirements.txt $APP_HOME

RUN apt-get update && \
    pip install -I --no-cache-dir -r requirements.txt && \
    rm requirements.txt && \
    rm -rf /var/lib/apt/list/*


COPY app.py $APP_HOME
COPY model.pkl $APP_HOME

CMD gunicorn -w 3 -b 0.0.0.0:5000 --timeout=120 --reload "app:app"

VOLUME $APP_HOME
