FROM python

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get upgrade

RUN python -m pip install gunicorn

RUN apt install -y nodejs
RUN apt install -y npm
RUN npm install npm@latest -g
RUN npm install -g @angular/cli

COPY . /code/