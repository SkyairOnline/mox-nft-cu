import pytest

from script.deploy_basic_nft import deploy_basic_nft
from script.deploy_mood_nft import deploy_mood_nft

@pytest.fixture
def basic_nft():
    return deploy_basic_nft()


@pytest.fixture
def mood_nft():
    return deploy_mood_nft()