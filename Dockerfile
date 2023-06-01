FROM python

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt-get -y update
RUN apt-get -y upgrade

RUN python -m pip install gunicorn

RUN apt install -y nodejs
RUN apt install -y npm
RUN npm install npm@6.14.13 -g
RUN npm install -g @angular/cli

COPY . /code/