class Request(object):
    def __init__(self, type, url, **kwargs):
        self.type = type
        self.parameters = kwargs
        self.url = url
        self.request_type = '{0} {1}'.format(type, url)

    def run(self, client):
        if self.type == 'GET':
            r = client.get(r'http://www.reddit.com/{0}'.format(self.url), params=self.parameters)
        elif self.type == 'POST':
            r = client.post(r'http://www.reddit.com/{0}'.format(self.url), params=self.parameters)
        if r:
            return r

