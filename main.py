from PostBot import *

p = PostBot('itgsodertornsubreddit', 'I am a hacker!')
while True:
    posts = p.get_unresponded_posts(p.subreddit)
    if posts:
        for post in posts:
            p.comment_on_post(p.message, post)
            p.add_post_as_posted(post)
    # sleep before we get new posts again to prevent unnecessary requests.
    print "All posts have been commented on"
    time.sleep(30)