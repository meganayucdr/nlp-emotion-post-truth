import tweepy
from dotenv import load_dotenv
import os

# Load environment
load_dotenv()

# Access API key from env variables
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

client = tweepy.Client(bearer_token=BEARER_TOKEN)
