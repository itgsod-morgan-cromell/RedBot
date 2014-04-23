from request import Request
import json


class GetPostComments(Request):
    """
    This request take a post and defaults get the latest 25 comments.
    """
    def __init__(self, post_url, limit=25):
        Request.__init__(self, 'GET', '{0}.json'.format(post_url), limit=limit)
        self.json = None
        self.comments = []

    def process_request(self, client):
        r = self.run(client)
        if r and r.status_code == 200:
            try:
                j = json.loads(r.content)
                self.json = j
                # The data for each comment are stored in j['data']['children']
                for comment in j[1]['data']['children']:
                    self.comments.append(comment)
            except ValueError:
                print " "

