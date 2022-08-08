# syntax=docker/dockerfile:1

FROM python:3.6

WORKDIR /app

COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip install flask-mysqldb
RUN pip install flask-mysql

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
