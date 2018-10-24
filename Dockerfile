FROM python:3.7 
 
 ENV PYTHONUNBUFFERED 1

 RUN mkdir -p /excelplay/excelplay-echo
 WORKDIR /excelplay/excelplay-echo

 RUN pip install --upgrade pip
 COPY ./Pipfile /excelplay/excelplay-echo/
 RUN pip install pipenv
 RUN pipenv install --deploy --system --skip-lock --dev
 ADD . /excelplay/excelplay-echo

