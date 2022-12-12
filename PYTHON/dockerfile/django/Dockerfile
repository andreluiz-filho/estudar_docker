FROM python:3.8-bullseye

WORKDIR /app

RUN pip install --no-cache-dir django psycopg2

ENV PYTHONUNBUFFERED=1

COPY project_django ./

CMD python /app/manage.py runserver 0.0.0.0:8000
