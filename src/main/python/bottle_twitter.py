import string
import random
import datetime
import traceback
from bottle import template, route, request, run

from src.main.python.TwitterStream import twitter_sampling
from src.main.python.extract_json import extract_data
from src.main.python.util import delete_txt_and_png


@route('/twitter')
def twitter():
    sampling_time = int(request.query.time)
    now = str(datetime.datetime.now().day) + '_' + str(datetime.datetime.now().month) + '_' + str(datetime.datetime.now().year)
    result_json_name = now + '_' + (''.join(random.choice(string.ascii_lowercase +
                                                          string.ascii_uppercase +
                                                          string.digits) for i in range(5)))
    try:
        print("Reading TwitterSampleStream...")
        twitter_sampling(time=sampling_time, name=result_json_name)
        print("Extracting Data from JSON...")
        result_file_links = extract_data(path_to_json_file=result_json_name)
        print("Deleting unneeded files...")
        delete_txt_and_png()

        info = {'country_result_link': result_file_links[1],
                'hashtag_result_link': result_file_links[2],
                'language_result_link': result_file_links[0]
                }

        return template('result_vorlage.tpl', info)
    except UnicodeEncodeError as e:
        delete_txt_and_png()
        return 'Most found Hashtag couldn\'t be written into database.'
    except TypeError as e:
        delete_txt_and_png()
        return 'Analysis time was too short to find hashtags, countries or languages in TwitterSampleStream.'


run(host='127.0.0.1', port=80)