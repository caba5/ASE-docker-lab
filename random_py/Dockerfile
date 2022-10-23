FROM python:3.8-slim-buster

ADD . /random_py
WORKDIR /random_py

RUN pip3 install -r requirements.txt

EXPOSE 8082

CMD ["flask", "run", "--host=0.0.0.0", "--port=8082"]