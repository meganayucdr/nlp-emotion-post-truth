import tweepy

class TwitterAuth:
    def __init__(self, api_key, api_secret, bearer_token):
        self.api_key = api_key
        self.api_secret = api_secret
        self.bearer_token = bearer_token
        self.client = None

    def authenticate(self):
        try:
            self.client = tweepy.Client(bearer_token=self.bearer_token)
            return self.client
        except tweepy.TweepError as e:
            print(e.reason)
            return None