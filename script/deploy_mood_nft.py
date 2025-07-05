from src import mood_nft
import base64
from moccasin.boa_tools import VyperContract

PUG_URI = "QmW16U98JrY9HBY36rQtUuUtDnm6LdEeNdAAggmrx3thMa"

def deploy_mood_nft() -> VyperContract:
    happy_svg_uri = ""
    sad_svg_uri = ""
    with open("./images/happy.svg", "r") as f:
        happy_svg = f.read()
        happy_svg_uri = svg_to_base64_uri(happy_svg)
    with open("./images/sad.svg", "r") as f:
        sad_svg = f.read()
        sad_svg_uri = svg_to_base64_uri(sad_svg)
    mood_contract = mood_nft.deploy(happy_svg_uri, sad_svg_uri)
    mood_contract.mint_nft()
    print(f"TokenURI: {mood_contract.tokenURI(0)}")
    return mood_contract

def moccasin_main():
    return deploy_mood_nft()

def svg_to_base64_uri(svg):
    svg_bytes = svg.encode('utf-8')
    base64_svg = base64.b64encode(svg_bytes).decode('utf-8')
    return f"data:image/svg+xml;base64,{base64_svg}"