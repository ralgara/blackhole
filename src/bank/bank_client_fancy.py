import grpc
import pdb
import os
import sys
import transaction_pb2 as txn
import transaction_pb2_grpc as txn_grpc

def hash(s):
    import md5
    m = md5.new()
    m.update(s)
    return m.hexdigest()

request = txn.BankRequest()
request.name = sys.argv[1]
request.account = hash(request.name)
request.type = txn.CREDIT
request.amount = float(sys.argv[2])

print '\n---------------------- Start transaction'
server_endpoint = '{BANK_SERVER}:50051'.format(**os.environ)
print "Opening channel to server: %s" % server_endpoint

channel = grpc.insecure_channel(server_endpoint)
print "Creating stub"
stub = txn_grpc.BankStub(channel)
print "Attempting transaction"
reply = stub.Deposit(request)

print "Transaction completed: {0}".format(reply)

print "Toying with serialization"

txnStr = request.SerializeToString()
print "Serialized request: %s\n" % txnStr

newTxn = txn.BankRequest()
newTxn.ParseFromString(txnStr)
newTxn.name = newTxn.name + " (copy)"
print "New deserialized and modified request: %s" % newTxn
print '---------------------- End transaction'
