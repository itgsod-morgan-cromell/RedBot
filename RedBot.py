from request_types import *
import requests
from throttler import Throttler

class RedBot(object):
    def __init__(self, throttler):
        self.client = requests.session()
        self.client.headers = {'user-agent': 'u/RedBotITG\'s testbot v 0.000000001'}
        self.throttler = throttler
        self.request_queue = [LoginRequest('RedbotITG', 'itgitg')]
        self.completed_requests = []
        self.process_queue()


    def process_queue(self):
        for i in range(len(self.request_queue)):
            self.send_request(self.request_queue[0])

    def send_request(self, request):
        if self.throttler.is_request_allowed:
            self.throttler.request_sent()
            print "request {0} sent".format(request.request_type)
            self.completed_requests.append(request)
            if request in self.request_queue:
                self.request_queue.remove(request)
            request.process_request(self.client)
        else:
            print 'Please wait {0} seconds'.format(self.throttler.remaining_time_until_reset())


r = RedBot(Throttler(30, 60))