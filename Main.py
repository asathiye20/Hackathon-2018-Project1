import tweepy

TWITTER_CLIENT = "kwykBA0bYzMqcHoFl29zK1OQa"
TWITTER_SECRET = "xyR4hegGMoQxCiDPrqmr4CLGm41DqG1rQDDDMrQRLJwRXBYd3O"
TWITTER_ACCESS = "967433840183709696-DRyKObUSKI7WbOmoePl0O3GBff8DYxV"
TWITTER_ACCESS_SECRET = "Veyq0L0SKkByptUD1CYlR2XkgjYDhJObzwbigbFrTe76A"

auth = tweepy.OAuthHandler(TWITTER_CLIENT, TWITTER_SECRET)
auth.set_access_token(TWITTER_ACCESS, TWITTER_ACCESS_SECRET)

api = tweepy.API(auth)

try:
    api.update_status("Hello, world!")
except TweepyError:
    print "Could not tweet"
