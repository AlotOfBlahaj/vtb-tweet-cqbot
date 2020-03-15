import json


class CONFIG:
    def __init__(self):
        with open("config.json") as f:
            tmp_json = json.loads(f.read())
        self.API_KEY = tmp_json['Twitter_API_KEY']
        self.CheckSec = tmp_json['CheckSec']
        self.EnableProxy = tmp_json['EnableProxy']
        self.Proxy = tmp_json['Proxy']
        self.Target = tmp_json['Target']


Config = CONFIG()
