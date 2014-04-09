from request_types import *
from RedBot import RedBot
from throttler import Throttler


class PostBot(object):

    def __init__(self):
        self.redbot = RedBot(Throttler(5, 60))
        self.redbot.request_queue.append(LoginRequest('redbotitg', 'itgitg'))
        self.redbot.process_queue()

    def get_posts(self):
        r = self.redbot.send_request(GetSubredditPostsRequest('itgSodertornsubreddit'))
        if r:
            return r.posts

    def get_comments_from_post(self, post):
        r = self.redbot.send_request(GetPostComments(post['data']['url']))
        if r:
            return r.comments



    def test(self):
        posts = self.get_unresponded_posts()
        if posts:
            for post in posts:
                print "wop"

    def get_unresponded_posts(self):
        self.posts = self.get_posts()
        unresponded_posts = []
        for post in self.posts:
            print "-------------"
            print "-------------"
            post['data']['comments'] = self.get_comments_from_post(post)
            if post['data']['comments']:
                print 'post title: ', post['data']['title']
                for comment in post['data']['comments']:
                    if 'author' in comment['data']:
                        if comment['data']['author'] is 'redbotitg':
                            break
            unresponded_posts.append(post)
        return unresponded_posts



