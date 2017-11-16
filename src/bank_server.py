from concurrent.futures import *
import grpc
import pdb
import time
import transaction_pb2 as txn
import transaction_pb2_grpc as txn_grpc

ledger = {}

class DemoBankServicer(txn_grpc.BankServicer):
    def Deposit(self, request, context):
        if ledger.has_key(request.account):
            print "Account {0} exists".format(request.account)
        else:
            # Create account if not found
            ledger[request.account] = {
                'account': request.account,
                'balance': 0
            }
            print "Created account {0} for {1}".format(request.account, request.name)
        print "Before transaction: {0}".format(ledger[request.account])
        ledger[request.account]['balance'] += request.amount
        print "After transaction: {0}".format(ledger[request.account])
        return txn.BankReply(message="Successful", balance=ledger[request.account]['balance'])


server = grpc.server(
    ThreadPoolExecutor(max_workers=10))

txn_grpc.add_BankServicer_to_server(
    DemoBankServicer(),
    server)

server.add_insecure_port('[::]:50051')

server.start()

print "------------------------------------"
print "Bank server started. All balances $0"
print "------------------------------------"

try:
    while True:
        time.sleep(3600 * 24)
except KeyboardInterrupt:
    server.stop(0)

print "\n------------------------------------"
print "Bank server stopped"
print "------------------------------------"
