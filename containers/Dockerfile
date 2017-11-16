FROM ubuntu:16.04

COPY . /src
WORKDIR /src

ENV PROTOBUF_TAG v3.4.1

RUN apt-get update

ENV PACKAGES git autoconf automake build-essential gcc python-dev
RUN apt-get install -y $PACKAGES

RUN git clone https://github.com/google/protobuf -b $PROTOBUF_TAG --depth 1

WORKDIR protobuf

RUN apt-get install -y curl unzip

RUN ./autogen.sh && \
    ./configure --prefix=/usr && \
    make -j 3 && \
    make check && \
    make install

WORKDIR /src

RUN rm -rf ./protobuf
