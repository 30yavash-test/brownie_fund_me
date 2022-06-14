from brownie import Fund
from scripts.helpful_scripts import get_account

def fund():
    fund_me = Fund[-1]
    account = get_account()
    entrace_fee = fund_me.getEntranceFee()
    print(entrace_fee)
    print('FUNDING...')
    fund_me.fund_me({'from':account , 'value':entrace_fee})
    print(fund_me.memoryAddress())


def withdraw():
    fund_me = Fund[-1]
    account = get_account()
    print('WITHDRAWING...')
    fund_me.Withdraw({'from':account})
    print(fund_me.memoryAddress())




def main():
    fund()
    withdraw()