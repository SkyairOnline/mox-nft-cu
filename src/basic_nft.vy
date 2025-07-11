# pragma version 0.4.3

"""
# @license MIT
# @title Puppy NFT
# @author Aldo Surya Ongko
# @description A simple NFT contract that allows minting and transferring of NFTs.
"""

from snekmate.tokens import erc721
from snekmate.auth import ownable

initializes: ownable
initializes: erc721[ownable := ownable]

exports: erc721.__interface__

# State Variables
NAME: constant(String[25]) = "Puppy NFT"
SYMBOL: constant(String[5]) = "PNFT"
BASE_URI: constant(String[7]) = "ipfs://"
EIP_712_VERSION: constant(String[1]) = "1"

# Function
@deploy
def __init__():
    ownable.__init__()
    erc721.__init__(NAME, SYMBOL, BASE_URI, NAME, EIP_712_VERSION)

@external
def mint(uri: String[432]):
    token_id: uint256 = erc721._counter
    erc721._counter = token_id + 1
    erc721._safe_mint(msg.sender, token_id, b"")
    erc721._set_token_uri(token_id, uri)

@external
@view
def get_base_uri() -> String[7]:
    return BASE_URI