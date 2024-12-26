import pandas as pd

class TwitterQuery:
    def __init__(self, client):
        self.client = client

    def fetch_tweets(self, query, max_results=100):
        try:
          tweets = self.client.search(
              query = query,
              tweet_fields = ['full_text', 'created_at', 'author_id', 'retweet_count', 'like_count'],
              max_results = max_results
          )
          tweet_data = []
          if tweets.data:
              for tweet in tweets.data:
                  tweet_data.append({
                      "created_at": tweet.created_at,
                      "author_id": tweet.author_id,
                      "full_text": tweet.full_text,
                      "retweet_count": tweet.public_metrics["retweet_count"],
                      "like_count": tweet.public_metrics["like_count"],
                  })
          return tweet_data
        except Exception as e:
            print(e)
            return []

    def save_to_csv(self, data, filename):
        try:
            df = pd.DataFrame(data)
            df.to_csv(filename, index=False)
        except Exception as e:
            print(e)