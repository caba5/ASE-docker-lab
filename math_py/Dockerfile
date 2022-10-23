FROM python:3.8-slim-buster

ADD . /math_py
WORKDIR /math_py

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]