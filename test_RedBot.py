from nose.tools import assert_equals
from mock import *

from RedBot.RedBot import RedBot, Throttler


def test_redbot_send_request():
    m = Mock()
    r = RedBot(m)
    r.send_request('test')
    m.request_sent.assert_called_with()


def test_redbot_request_queue():
    r = RedBot(Throttler(3, 2))
    queue = [1, 2, 3, 4, 5, 6]
    r.request_queue = queue
    r.run()
    assert_equals([1, 2, 3, 4, 5, 6], r.completed_requests)