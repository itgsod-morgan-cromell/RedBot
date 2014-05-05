from request_types import *
from RedBot import RedBot
from throttler import Throttler
import time


class PostBot(object):
    """
    This class checks posts from a given subreddit. If the given subreddit id does not exist in the ".posts" file
    it will post the given message as a comment to the post.
    """
    def __init__(self, subreddit, msg):
        """
        Creates a RedBot object and gives it a throttler with the given standard values for Reddit.
        """
        self.redbot = RedBot(Throttler(30, 60))
        self.redbot.send_request(LoginRequest('redbotitg', 'itgitg'))
        self.subreddit = subreddit
        self.message = msg
        f = open('subreddits/{0}.posts'.format(self.subreddit), 'a')
        f.close()

    def get_posts(self, subreddit):
        """
        Requests and returns the last 25 posts in given subreddit.
        """
        r = self.redbot.send_request(GetSubredditPostsRequest(subreddit, "", 25))
        if r:
            return r.posts

    def get_comments_from_post(self, post):
        """
        Requests and returns all the comments in given post
        """
        r = self.redbot.send_request(GetPostComments(post['data']['url']))
        if r:
            return r.comments

    def comment_on_post(self, message, post):
        """
        Posts a comment request with the given message on the given post.
        """
        self.redbot.send_request(PostCommentRequest(post['data']['name'], message))
        print "The bot has commented to the thread: ", post['data']['title']

    def add_post_as_posted(self, post):
        """
        Adds the unique post_id to the ".posts" file to mark it as completed.
        """
        post_id = post['data']['name']
        with open('subreddits\{0}.posts'.format(self.subreddit), 'a') as subredditfile:
            subredditfile.write('{0}\n'.format(post_id))

    def get_unresponded_posts(self, subreddit):
        """
        Returns the posts in the subreddit that has not yet been commented as an array.
        Checks the post_id with the ".post" file.
        If it does not exist in the ".posts" file it will add it to the unresponed_posts list.
        """
        self.posts = self.get_posts(subreddit)
        unresponded_posts = []
        responed_posts = [line.strip() for line in open('subreddits/{0}.posts'.format(subreddit))]
        for post in self.posts:
            # The post_id is in is located inside post['data']['name']
            if post['data']['name'] not in responed_posts:
                unresponded_posts.append(post)

        return unresponded_posts


