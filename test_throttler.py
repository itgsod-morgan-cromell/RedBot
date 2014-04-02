from nose.tools import assert_equals
from RedBot.throttler import Throttler


def test_throttler_request_allowed():
    t = Throttler(10, 10)
    assert_equals(True, t.is_request_allowed)
