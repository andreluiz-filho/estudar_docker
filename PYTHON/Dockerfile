FROM python:3.8-bullseye

WORKDIR /app

#RUN pip install django psycopg2
RUN pip install django
RUN pip install psycopg2

ENV PYTHONUNBUFFERED=1

COPY project_django ./

CMD python /app/manage.py runserver 0.0.0.0:8000
