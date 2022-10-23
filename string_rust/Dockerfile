FROM rust:1.64-slim-buster

ADD . /string
WORKDIR /string

RUN cargo build

EXPOSE 5000

CMD ["cargo", "run"]