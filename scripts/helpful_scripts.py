from brownie import accounts, network , MockV3Aggregator
import os
FORKED_LOCAL_ENVIRONMENTS = ['mainnet-fork-dev', 'mainnet-fork']
# too mainnet ma niazi be mock nadarim choon khodesh price fee ro roo shabakash dare
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", 'ganache-local']


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS :
        return accounts[0]
    else:
        return accounts.add(os.getenv("PRIVATE_KEY"))


def deploy_Mock():
    print(f"the active network is {network.show_active()}")
    print("deploying mock...")
    # deghat kon ke mock ie contracte , pas mese liste , ghablan dashtim ke age deploy konim , contract save mishe va mitoonim azash estefade konim
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(8, 200000000, {"from": get_account()})
    print("mock deployed!!!")
