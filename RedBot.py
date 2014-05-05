import requests
import time


class RedBot(object):
    """
    This class takes care of the request objects. If the throttler allows this class to send the request object
    the class will process the request object.
    This class also takes care of the client and keeps everything running.
    The client is the session that makes us able to continue with the same login account.
    """

    def __init__(self, throttler):
        self.client = requests.session()
        self.client.headers = {'user-agent': 'u/RedBotITG\'s testbot v1. Made for commenting on posts.'}
        self.throttler = throttler
        self.request_queue = []
        self.completed_requests = []
        self.process_queue()


    #clear_completed_queue and process_queue are not currently used

    def clear_completed_queue(self):
        self.completed_requests = []

    def process_queue(self):
        for i in range(len(self.request_queue)):
            self.send_request(self.request_queue[0])

    def send_request(self, request):
        while True:
            if self.throttler.is_request_allowed:
                self.throttler.request_sent()
                print "request {0} sent \n".format(request.request_type)
                self.completed_requests.insert(0, request)
                if request in self.request_queue:
                    self.request_queue.remove(request)
                request.process_request(self.client)
                return request
            else:
                print 'Please wait {0} seconds'.format(self.throttler.remaining_time_until_reset())
                time.sleep(1)
