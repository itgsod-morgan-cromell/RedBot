from RedBot import request


class RedBot(object):
    def __init__(self, throttler):
        self.throttler = throttler
        self.request_queue = []
        self.completed_requests = []

    def run(self):
        while True:
            if self.request_queue:
                self.process_queue()
            else:
                return

    def process_queue(self):
        for i in range(len(self.request_queue)):
            self.send_request(self.request_queue[0])

    def send_request(self, request):
        print request
        if self.throttler.is_request_allowed:
            self.throttler.request_sent()
            print "request {0} sent".format(request)
            self.completed_requests.append(request)
            if request in self.request_queue:
                self.request_queue.remove(request)
        else:
            print 'Please wait {0} seconds'.format(self.throttler.remaining_time_until_reset())

r = request.get(r'http://www.reddit.com/user/spilcm/comments/.json')
data = r.json()
print data.keys()