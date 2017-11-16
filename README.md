# gRPC and protocol buffers

### Prerequisites

* [Download](https://github.com/ralgara/blackhole) this repo (assumed at ~/git/blackhole locally)

### Build the development container

```
cd ~/git/blackhole
cd containers
docker build . -t blackhole-protoc
```

The container is roughly: 

* Ubuntu
* C++ build chain
* git
* Clone protobuf repo and build from source (~15 minutes)
* pip + pip install grpcio-tools

### Start the protoc container and step into it

```
docker run -it --name bank-server --volume ~/git/blackhole:/workspace -w /workspace blackhole-protoc
```

*All steps below are in the container's shell unless indicated otherwise*

### The protoc compiler
```
protoc
protoc --version
```

### Compile bank demo app protocol buffers into Python
```
cd /workspace/src/bank
rm *_pb2.py* # remove any prior outputs
ls -l       # before compilation
protoc --python_out=. transaction.proto
ls -l       # after compilation
```

We now have generated protobuf boilerplate: `transaction_pb2.py`

### Compile gRPC interfaces
```
cd /workspace/src/bank
rm *_pb2{,._grpc}.py* # remove any prior outputs
ls -l       # before compilation
python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. transaction.proto
ls -l       # after compilation, notice 
```

We now also have a gRPC stub: `transaction_pb2_grpc.py`

## Bank demo application

Now a simple demo (and some very questionable financial practices...)

### Start the server
```
cd /workspace/src/bank
python bank_server.py
```

### Run the client
```
# >>> Change to host shell
# start client container
docker run --rm -it \
   --name bank_client \
   --volume ~/git/blackhole:/workspace \
   -w /workspace/src/bank \
   --env BANK_SERVER=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' bank-server) \
   blackhole-protoc
# <<< end of host shell context

# inside new container:
python bank_client.py

# better yet: 
python bank_client_fancy.py satoshi 3.14
```




