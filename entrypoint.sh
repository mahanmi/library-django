#! /usr/bin/env bash

BASE_DIR="$(dirname "$0")"

python "$BASE_DIR/src/manage.py" migrate

cd src

gunicorn \
    --bind 0.0.0.0:8000 \
    --workers "${GUNICORN_WORKERS:-3}" \
    library.wsgi:application
