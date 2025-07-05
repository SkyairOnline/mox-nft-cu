from src import basic_nft
from moccasin.boa_tools import VyperContract

PUG_URI = "QmW16U98JrY9HBY36rQtUuUtDnm6LdEeNdAAggmrx3thMa"

def deploy_basic_nft() -> VyperContract:
    contract = basic_nft.deploy()
    contract.mint(PUG_URI)
    token_uri = contract.tokenURI(0)
    print(f"Token URI: {token_uri}")
    return contract

def moccasin_main():
    return deploy_basic_nft()