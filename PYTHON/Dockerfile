FROM python:3.10-alpine

WORKDIR /app

RUN pip install --no-cache-dir django

ENV PYTHONUNBUFFERED=1

COPY project_django/ ./

CMD python /app/manage.py runserver 0.0.0.0:8000
