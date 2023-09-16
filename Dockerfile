FROM python:latest

WORKDIR /my-flask-app

COPY /application ./application
COPY app.py create.py requirements.txt commands.sh ./

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["./commands.sh"]