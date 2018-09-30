#!/bin/bash

# Collect static files
python manage.py migrate

# Migrate database
python manage.py migrate

# Run dev server
python manage.py runserver 0.0.0.0:8000
