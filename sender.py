from queue import Queue
from threading import Thread

import requests


class CqAPI:
    def __init__(self, host, groupID, token):
        self.host = host
        self.groupID = groupID
        self.token = token
        self.sess = requests.session()

    def initSess(self):
        self.sess.headers = {'Content-Type': 'application/json',
                             'Authorization': f'Bearer {self.token}'}

    def send_handler(self, msg):
        try:
            r = requests.post(f'http://{self.host}/send_group_msg', data=msg)
            if r.status_code == 200:
                print(f"send {msg['message']} to {msg['group_id']} successful")
            else:
                raise requests.exceptions.ConnectionError
        except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout) as e:
            print(f"sending {msg['message']} to {msg['group_id']} failed")
            print(e)

    @staticmethod
    def newMsg(message, groupID):
        return {
            'group_id': int(groupID),
            'message': message,
            'auto_escape': False
        }

    def sender(self, message):
        for g in self.groupID:
            msg = self.newMsg(message, g)
            self.send_handler(msg)


class Sender:
    def __init__(self, CqHost, GroupID, Token):
        self._mailbox = Queue()
        self.handler = CqAPI(CqHost, GroupID, Token)

    def send(self, tweet: str):
        self._mailbox.put(tweet)

    def recv(self):
        tweet = self._mailbox.get()
        return tweet

    def run(self):
        print("Sender")
        while True:
            tweet = self.recv()
            self.handler.sender(tweet)

    def start(self):
        t = Thread(target=self.run)
        t.daemon = True
        t.start()
