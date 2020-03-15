import requests

from config import Config


class TweetApi:
    def __init__(self, user_id):
        self.API_KEY = Config.API_KEY
        self.user_id = user_id
        self.since_id = 0

    def setSinceID(self, resp):
        self.since_id = resp[0]['id']
        print(f"set since_id {self.since_id}")

    @staticmethod
    def formatTweet(resp):
        result = []
        for t in resp:
            message = f"{t['user']['name']}的推特更新了\n" \
                      f"正文:{t['text']}\n" \
                      f"链接：https://twitter.com/{t['user']['id_str']}/status/{t['id_str']}"
            result.append(message)
            print(f"get tweets: {message}")
        return result

    def updateTweet(self):
        payload = {
            "user_id": self.user_id,
            "exclude_replies": 1
        }
        if self.since_id != 0:
            payload['since_id'] = self.since_id
        try:
            if Config.EnableProxy:
                proxies = {
                    "http": f"http://{Config.Proxy}",
                    "https": f"http://{Config.Proxy}",
                }
                r = requests.get("https://api.twitter.com/1.1/statuses/user_timeline.json", params=payload,
                                 proxies=proxies, headers={"Authorization": "Bearer " + self.API_KEY})
            else:
                r = requests.get("https://api.twitter.com/1.1/statuses/user_timeline.json", params=payload)
            if r.status_code == 200:
                tweet_list = self.formatTweet(r.json())
                if not tweet_list:
                    return []
            else:
                raise requests.exceptions.ConnectionError
        except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout) as e:
            print(e)
            return []
        if self.since_id != 0:
            self.setSinceID(r.json())
            return tweet_list
        self.setSinceID(r.json())
        return []
