import requests
import time
class RedBot(object):
    def __init__(self, throttler):
        self.client = requests.session()
        self.client.headers = {'user-agent': 'u/RedBotITG\'s testbot v 0.000000001'}
        self.throttler = throttler
        self.request_queue = []
        self.completed_requests = []
        self.process_queue()


    def clear_completed_queue(self):
        self.completed_requests = []


    def process_queue(self):
        for i in range(len(self.request_queue)):
            self.send_request(self.request_queue[0])

    def send_request(self, request):
        while True:
            if self.throttler.is_request_allowed:
                self.throttler.request_sent()
                print "request {0} sent".format(request.request_type)
                self.completed_requests.insert(0, request)
                if request in self.request_queue:
                    self.request_queue.remove(request)
                request.process_request(self.client)
                return request
            else:
                print 'Please wait {0} seconds'.format(self.throttler.remaining_time_until_reset())
                time.sleep(1)
