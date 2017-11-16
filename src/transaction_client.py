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

channel = grpc.insecure_channel('localhost:50051')
stub = txn_grpc.BankStub(channel)
reply = stub.Deposit(request)

print "Transaction completed: {message}, balance: {balance}".format(**reply)
