from request import Request
import json


class GetSubredditPostsRequest(Request):
    """
    This request takes a subreddit and default gets the last 25 posts sent to that subreddit.
    """
    def __init__(self, subreddit, sorting='', limit=25, **kwargs):
        Request.__init__(self, 'GET', 'http://www.reddit.com/r/{0}/{1}.json'.format(subreddit, sorting), limit=limit)
        self.json = None
        self.posts = []

    def process_request(self, client):
        r = self.run(client)
        if r.status_code == 200:
            j = json.loads(r.content)
            self.json = j
            # The data for each post are stored in j['data']['children']
            for post in j['data']['children']:
                self.posts.append(post)
