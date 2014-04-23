from request import Request
import json


class LoginRequest(Request):
    """
    This request logs the client into reddit. It takes a username and a password.
    It also sets the clients modhash.
    """
    def __init__(self, username, password):
        Request.__init__(self, 'POST', 'http://www.reddit.com/api/login', api_type='json', user=username, passwd=password)

    def process_request(self, client):
        r = self.run(client)
        if r.status_code == 200:
            j = json.loads(r.content)
            if 'data' in j['json']:
                client.modhash = j['json']['data']['modhash']
                print "Logged in"
                print 'modhash is {0}'.format(client.modhash)
        else:
            print 'Failed to log in'

