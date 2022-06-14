from brownie import Fund, MockV3Aggregator , accounts, network, config
import os
from scripts.helpful_scripts import get_account, deploy_Mock, LOCAL_BLOCKCHAIN_ENVIRONMENTS

def deploy_Fund():

    account = get_account()
    print(f'my account address is {network.show_active()}')
    # dar ghesmate deploy , constructor ro pass midim be contract   
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS :
        price_fee_address = config['networks'][network.show_active()]["eth_usd_price"]
    else:
        deploy_Mock()
        price_fee_address = MockV3Aggregator[-1].address
    
    fund_me = Fund.deploy(
    price_fee_address,
    {"from": account},
    publish_source=config["networks"][network.show_active()].get('verify'))

    print(f"contract deployed to {fund_me.address}")

def main():
    deploy_Fund()

# *** ie nokte : baad az har bar ke az ganache estefade mikonim , va barname ro bebandim , etela'at mire , bayad az contract , deployments , pushe 1337 ro pak konim , az too map.json ham ghesmate 1337 delete konim va az aval contract ro deploy konim
