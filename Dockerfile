FROM python:3.6
 ENV PYTHONUNBUFFERED 1
 RUN mkdir -p /excelplay/excelplay-echo
 WORKDIR /excelplay/excelplay-echo
 ADD requirements.txt /excelplay/excelplay-echo/
 RUN pip install -r requirements.txt
 ADD . /excelplay/excelplay-echo
