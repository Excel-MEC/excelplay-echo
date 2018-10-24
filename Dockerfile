FROM python:3.7
 
 ENV PYTHONUNBUFFERED 1
 
 RUN mkdir -p /excelplay/excelplay-echo
 WORKDIR /excelplay/excelplay-echo
 RUN pip install --upgrade pip
 RUN pip install pipenv
 ADD Pipfile /excelplay/excelplay-echo/
 ADD Pipfile.lock /excelplay/excelplay-echo/
 RUN pipenv install --deploy --system --skip-lock --dev
 ADD . /excelplay/excelplay-echo
