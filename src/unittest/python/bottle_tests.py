import twittercode.bottle_twitter
from boddle import boddle

def test_health_check():
    with boddle(params={'name':'sfabig'}):
        assert bottle_twitter.health_check() == 'Hi sfabig! I am good!'