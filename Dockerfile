# syntax=docker/dockerfile:1

# local
# FROM python:alpine
# WORKDIR /code
# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0
# RUN apk add --no-cache gcc musl-dev linux-headers
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt
# EXPOSE 5000
# COPY . .
# CMD ["flask", "run"]

# CloudRun
FROM python:3.10-slim
ENV PYTHONNUNBUFFERED True
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
RUN pip install --no-cache-dir -r requirements.txt
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app