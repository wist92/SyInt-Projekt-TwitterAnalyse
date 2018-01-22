import json
import pandas as pd
import matplotlib.pyplot as plt
from src.main.python.s3_util import push_to_s3
from src.main.python.dbHandler import *


def import_twitter_data(path):
    print('Import file %s' % path)
    tweets_data = []
    tweets_file = open(path, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue
    tweets_file.close()
    return tweets_data


def extract_data(path_to_json_file):
    tweets_data = import_twitter_data('twitter_data_' + path_to_json_file + '.txt')

    tweets = pd.DataFrame()
    tweets['text'] = [tweet.get('text', '') for tweet in tweets_data]
    tweets['lang'] = [tweet.get('lang', '') for tweet in tweets_data]
    tweets['country'] = [tweet.get('place', '')['country'] if tweet.get('place') is not None else None
                         for tweet in tweets_data]

    hashtags = pd.DataFrame()
    tags = list()
    for tweet in tweets_data:
        g = tweet.get('entities')['hashtags']
        for hashtag in g:
            tags.append(hashtag['text'])

    hashtags['tags'] = [tag for tag in tags]

    tweets_by_lang = tweets['lang'].value_counts()
    tweets_by_hashtag = hashtags['tags'].value_counts()
    tweets_by_country = tweets['country'].value_counts()

    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlabel('Languages', fontsize=15)
    ax.set_ylabel('Number of tweets' , fontsize=15)
    ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
    tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
    plt.tight_layout()
    plt.savefig(path_to_json_file + '_top_languages.png')

    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlabel('Countries', fontsize=15)
    ax.set_ylabel('Number of tweets' , fontsize=15)
    if len(tweets_by_country) < 5:
        title = 'Top %d countries' % len(tweets_by_country)
        ax.set_title(title, fontsize=15, fontweight='bold')
        tweets_by_country[:len(tweets_by_country)].plot(ax=ax, kind='bar', color='blue')
    else:
        ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
        tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
    plt.tight_layout()
    plt.savefig(path_to_json_file + '_top_countries.png')

    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlabel('Hashtags', fontsize=15)
    ax.set_ylabel('Number of tweets' , fontsize=15)
    if len(tweets_by_hashtag) < 5:
        title = 'Top %d hashtags' % len(tweets_by_hashtag)
        ax.set_title(title, fontsize=15, fontweight='bold')
        tweets_by_hashtag[:len(tweets_by_hashtag)].plot(ax=ax, kind='bar', color='blue')
    else:
        ax.set_title('Top 5 hashtags', fontsize=15, fontweight='bold')
        tweets_by_hashtag[:5].plot(ax=ax, kind='bar', color='blue')
    plt.tight_layout()
    plt.savefig(path_to_json_file + '_top_hashtags.png')

    # Push most used Hashtag and Country to DB
    print("Writing into database...")
    db = dbHandler()
    db.setData(session=path_to_json_file, hashtag=tweets_by_hashtag[0], location=tweets_by_country[0])
    db.getAll()
    db.closeConn()

    print("Pushing files to S3...")
    return push_to_s3(path_to_json_file + '_top_languages.png', path_to_json_file + '_top_countries.png',
                      path_to_json_file + '_top_hashtags.png')


if __name__ == '__main__':
    extract_data('twitter_data.txt')