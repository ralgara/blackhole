import grpc
import pdb
import os
import sys
import transaction_pb2 as txn
import transaction_pb2_grpc as txn_grpc

request = txn.BankRequest()
request.name = 'Satoshi'
request.account = '0001200-ABF-391'
request.type = txn.CREDIT
request.amount = 3.14

server_endpoint = '{BANK_SERVER}:50051'.format(**os.environ)
print "Opening channel to server: %s" % server_endpoint

channel = grpc.insecure_channel(server_endpoint)
print "Creating stub"
stub = txn_grpc.BankStub(channel)
print "\n---Attempting transaction:\n%s" % request
reply = stub.Deposit(request)

print "Transaction completed: {0}".format(reply)
