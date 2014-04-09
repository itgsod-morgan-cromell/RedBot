from request import Request
import json


class GetPostComments(Request):
    def __init__(self, post_url, limit=25):
        Request.__init__(self, 'GET', '{0}.json'.format(post_url), limit=limit)
        self.json = None
        self.comments = []


    def process_request(self, client):
        r = self.run(client)
        if r.status_code == 200:
            j = json.loads(r.content)
            self.json = j
            for comment in j[1]['data']['children']:
                self.comments.append(comment)

