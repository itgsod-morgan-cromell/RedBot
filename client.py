import requests
import json


class Client(object):
    def __init__(self, username, password):
        self.session = requests.session()
        self.session.headers = {'user-agent': 'u/RedBotITG\'s testbot v 0.000000001'}
        self.user_dict = {'api_type': 'json',
                          'user': username,
                          'passwd': password}

    def login(self):
        self.response = self.session.post(r'http://www.reddit.com/api/login', data=self.user_dict)
        j = json.loads(self.response.content)
        print j
        self.session.modhash = j['json']['data']['modhash']


