#!/bin/bash
python excelplay-echo/excelplay_echo/manage.py makemigrations && \
	python excelplay-echo/excelplay_echo/manage.py migrate
cd excelplay-dalalbull/excelplay_dalalbull
gunicorn excelplay_dalalbull.wsgi --bind 0.0.0.0:8003
