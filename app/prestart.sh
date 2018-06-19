#! /usr/bin/env bash

su -m celery -c "celery -A tasks beat --loglevel=info --pidfile='/tmp/celerybeat.pid'" &
su -m celery -c "celery -A tasks worker --loglevel=warn" &