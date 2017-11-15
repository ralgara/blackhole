# gRPC and protocol buffers

### Prerequisites

* [Download](https://github.com/ralgara/blackhole) this repo (assumed at ~/git/blackhole locally)

### Build the development container

```
cd ~/git/blackhole
cd containers/protoc
docker build . -t blackhole-protoc
```

The container is a compact Alpine base into which we clone the protobuf repo and build from source (~15 minutes).

### Compile protobuf

```
cd ~/git/blackhole
docker run -it blackhole-protoc --volumes $(pwd):/workdir -I=$SRC_DIR --python_out=$SRC_DIR/src/python $SRC_DIR/src/protos/transaction.proto

docker run -it --workdir=$(pwd) --volume $(pwd):/workdir blackhole-protoc -I=/workdir --python_out=/workdir/src/python --proto_path=/workdir /workdir/src/protos/transaction.proto

cd ~/git/blackhole
SRC_DIR=$(pwd)
protoc -I=$SRC_DIR --python_out=$SRC_DIR/src/python $SRC_DIR/src/protos/transaction.proto
```
