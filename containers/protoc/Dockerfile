FROM alpine:3.2

COPY . /src
WORKDIR /src

ENV PROTOBUF_TAG v3.4.1

RUN ./build.sh

ENTRYPOINT ["protoc"]
