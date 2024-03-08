FROM --platform=amd64 python:3.12-alpine3.19

# ENV FLASK_RUN_PORT=8000
ENV FLASK_RUN_HOST="0.0.0.0"
ENV FLASK_DEBUG=1

COPY . /srv
WORKDIR /srv

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_APP=rinha


CMD ["flask","--app", "wsgi.py", "run"]
