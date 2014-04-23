from request import Request
import json

class GetSubredditPostsRequest(Request):
    def __init__(self, subreddit, sorting='', limit=25, **kwargs):
        Request.__init__(self, 'GET', 'http://www.reddit.com/r/{0}/{1}.json'.format(subreddit, sorting), limit=limit)
        self.json = None
        self.posts = []

    def process_request(self, client):
        r = self.run(client)
        if r.status_code == 200:
            j = json.loads(r.content)
            self.json = j
            for post in j['data']['children']:
                self.posts.append(post)
