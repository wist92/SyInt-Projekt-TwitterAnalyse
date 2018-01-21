# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time

# Variables that contains the user credentials to access Twitter API
access_token = "1468542362-x9hqz45XRfIo2W53gt6zscVjOtinbzeluriER4G"
access_token_secret = "AR94TILL9Imk7YXKCX4RC9GX7pt6kBbur0rll013PHBR9"
consumer_key = "iInr1a3dPbgH5Mkqi9fmZRy6u"
consumer_secret = "XHkYBQB2wCin0UzyDjl2qEKYnIGjTyPFcdvRNI3wiMDWX5P6So"


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def __init__(self, time_limit=10, file_name='twitter_data.txt'):
        self.start_time = time.time()
        self.limit = time_limit
        self.saveFile = open(file_name, 'w+')
        super(StdOutListener, self).__init__()

    def on_data(self, data):
        print (data)
        if (time.time() - self.start_time) < self.limit:
            if "{\"delete\":" not in data:
                self.saveFile.write(data)
            return True
        else:
            self.saveFile.close()
            return False

    def on_error(self, status):
        print (status)
        if status == 420:
            # returning False in on_data disconnects the stream
            return False


def twitter_sampling(time, name):
    # This handles Twitter authentication and the connection to Twitter Streaming API
    stream_listener = StdOutListener(time_limit=time, file_name='twitter_data_' + name + '.txt')
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, stream_listener)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.sample()


if __name__ == '__main__':

    # This handles Twitter authentication and the connection to Twitter Streaming API
    stream_listener = StdOutListener(time_limit=60)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, stream_listener)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.sample()