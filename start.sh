#!/bin/bash

python manage.py makemigrations users
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py createsuperuser
gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000