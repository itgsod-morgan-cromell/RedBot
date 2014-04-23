from request import Request
import json
import time


class PostComment(Request):
    def __init__(self, id, message):
        Request.__init__(self, 'POST', 'http://www.reddit.com/api/comment', api_type='json',
                         text=message, thing_id=id)


    def process_request(self, client):
        r = self.run(client)
        if r and r.status_code == 200:
            j = json.loads(r.content)
            if 'ratelimit' in j['json']:
                print "can't post, sleeping {0} seconds".format(j['json']['ratelimit'])
                time.sleep(j['json']['ratelimit'])
                self.process_request(client)