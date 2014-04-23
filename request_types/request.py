class Request(object):
    def __init__(self, type, url, **kwargs):
        self.type = type
        self.parameters = kwargs
        self.url = url
        self.request_type = '{0} {1}'.format(type, url)

    def run(self, client):
        if hasattr(client, 'modhash'):
            self.parameters['uh'] = client.modhash
        if self.type == 'GET':
            r = client.get(r'{0}'.format(self.url), params=self.parameters)
        elif self.type == 'POST':
            r = client.post(r'{0}'.format(self.url), params=self.parameters)
        if r:
            return r

