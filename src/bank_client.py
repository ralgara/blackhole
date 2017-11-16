import grpc
import pdb
import transaction_pb2 as txn
import transaction_pb2_grpc as txn_grpc

request = txn.BankRequest()
request.name = 'Satoshi'
request.account = '0001200-ABF-391'
request.type = txn.CREDIT
request.amount = 3.14

#print request.SerializeToString()
#pdb.set_trace()

print "Opening channel to server"
channel = grpc.insecure_channel('localhost:50051')
print "Creating stub"
stub = txn_grpc.BankStub(channel)
print "Attempting transaction"
reply = stub.Deposit(request)

print "Transaction completed: {0}".format(reply)
