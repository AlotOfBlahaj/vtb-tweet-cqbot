from threading import Thread
from time import sleep

from config import Config
from sender import Sender
from tweet import TweetApi


class Main:
    def __init__(self, Twitter_UserID, CqHost, GroupID, CqToken):
        self.sender = Sender(CqHost, GroupID, CqToken)
        self.sender.start()
        self.t = TweetApi(Twitter_UserID)
        while True:
            for i in self.t.updateTweet():
                self.sender.send(i)
            sleep(Config.CheckSec)


def newMain(Twitter_UserID, CqHost, GroupID, CqToken):
    m = Main(Twitter_UserID, CqHost, GroupID, CqToken)


def main():
    for t in Config.Target:
        th = Thread(target=newMain, args=(t['Twitter_UserID'], t['CqHost'], t['GroupID'], t['CqToken']))
        th.start()


if __name__ == '__main__':
    main()
