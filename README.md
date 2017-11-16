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

### Start the protoc container

```
cd ~/git/blackhole
docker run -it --volume ~/git/blackhole:/workspace -w /workspace blackhole-protoc
```

### Compile protocol buffer into Python
```
protoc --python_out=. transaction.proto
```

### Compile gRPC interfaces
```
python -m grpc_tools.protoc --python_out=. transaction.proto
```
