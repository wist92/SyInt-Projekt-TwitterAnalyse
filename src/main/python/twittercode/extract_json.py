import json

import matplotlib.pyplot as plt
import pandas as pd

from twittercode.s3_util import push_to_s3


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


def create_plot(tweets_series,title, path):
    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlabel('Countries', fontsize=15)
    ax.set_ylabel('Number of tweets', fontsize=15)
    if len(tweets_series) < 5:
        plot_title = 'Top %d %s' % (len(tweets_series), title)
        ax.set_title(plot_title, fontsize=15, fontweight='bold')
        tweets_series[:len(tweets_series)].plot(ax=ax, kind='bar', color='blue')
    else:
        plot_title = 'Top 5 %s' % title
        ax.set_title(plot_title, fontsize=15, fontweight='bold')
        tweets_series[:5].plot(ax=ax, kind='bar', color='blue')
    plt.tight_layout()
    file_name = path + '_top_%s.png' % title
    plt.savefig(file_name)


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

    create_plot(tweets_series=tweets_by_country,title='countries',path=path_to_json_file)
    create_plot(tweets_series=tweets_by_hashtag,title='hashtags',path=path_to_json_file)
    create_plot(tweets_series=tweets_by_lang, title='languages', path=path_to_json_file)

    # Push most used Hashtag and Country to DB
    print("Writing into database...")
    from twittercode.dbHandler import DbHandler
    try:
        db = DbHandler()
        db.set_data(session=str(path_to_json_file), hashtag=str(tweets_by_hashtag.index[0]), location=str(tweets_by_country.index[0]))
        db.get_all()
    except UnicodeEncodeError as e:
        print(e)

    print("Pushing files to S3...")
    return push_to_s3(path_to_json_file + '_top_languages.png', path_to_json_file + '_top_countries.png',
                      path_to_json_file + '_top_hashtags.png')


if __name__ == '__main__':
    extract_data('twitter_data.txt')