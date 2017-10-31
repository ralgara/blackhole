# gRPC and protocol buffers

### Prerequisites

* [Download](https://github.com/ralgara/blackhole) this repo (assumed at ~/git/blackhole locally)
* [Download](https://github.com/google/protobuf/releases) and install protobuf distribution

### Compile protobuf

```
cd ~/git/blackhole
SRC_DIR=$(pwd)
protoc -I=$SRC_DIR --python_out=$SRC_DIR/src/python $SRC_DIR/src/protos/transaction.proto
```
