import transaction_pb2 as txn
import pdb

request = txn.BankRequest()
request.name = 'Satoshi'
request.account = '0001200-ABF-391'
request.type = txn.CREDIT
request.amount = 3.14
#print request.SerializeToString()
#pdb.set_trace()
