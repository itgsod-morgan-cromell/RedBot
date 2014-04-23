class Request(object):
    """
    A standard request class that is supposed to work with all requests. Needs a type that is either a 'GET' or 'POST'.
    And an url to use as request target.
    **kwargs is extra properties that is mostly used for POST requests.
    """
    def __init__(self, type, url, **kwargs):
        self.type = type
        self.parameters = kwargs
        self.url = url
        self.request_type = '{0} {1}'.format(type, url)

    def run(self, client):
        """
        Sends the request to the client and processes it either as a GET or a POST request depending on the type.
        Also makes sure the client has a modhash before processing the request.
        """
        if hasattr(client, 'modhash'):
            self.parameters['uh'] = client.modhash
        if self.type == 'GET':
            r = client.get(r'{0}'.format(self.url), params=self.parameters)
        elif self.type == 'POST':
            r = client.post(r'{0}'.format(self.url), params=self.parameters)
        if r:
            return r

