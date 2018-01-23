from twittercode.extract_json import extract_hashtags
import unittest
import json


class TestUtil(unittest.TestCase):
    def test_extract_hashtags_from_given_json_string(self):
        json_string = json.loads({"created_at":"Sat Jan 20 18:23:47 +0000 2018","id":954781518538428417,"id_str":"954781518538428417","text":"RT @ebr_lice: #AfrinOperasyonu\nDe\u011ferli AK DAVA neferimiz olan \ud83d\udc49 @OrhanBirinci61 karde\u015fimiz madur durumdad\u0131r.. Kanser hastas\u0131 annesi i\u00e7in bo\u2026","source":"\u003ca href=\"http:\/\/twitter.com\/download\/android\" rel=\"nofollow\"\u003eTwitter for Android\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":579162247,"id_str":"579162247","name":"Ercan51","screen_name":"eko5171","location":null,"url":null,"description":null,"translator_type":"regular","protected":false,"verified":false,"followers_count":7012,"friends_count":7093,"listed_count":3,"favourites_count":73861,"statuses_count":95591,"created_at":"Sun May 13 18:05:48 +0000 2012","utc_offset":-36000,"time_zone":"Hawaii","geo_enabled":false,"lang":"tr","contributors_enabled":false,"is_translator":false,"profile_background_color":"000000","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_tile":false,"profile_link_color":"19CF86","profile_sidebar_border_color":"000000","profile_sidebar_fill_color":"000000","profile_text_color":"000000","profile_use_background_image":false,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/886147482371198978\/b8W9J-Yi_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/886147482371198978\/b8W9J-Yi_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/579162247\/1502287458","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"retweeted_status":{"created_at":"Sat Jan 20 15:23:50 +0000 2018","id":954736231946047489,"id_str":"954736231946047489","text":"#AfrinOperasyonu\nDe\u011ferli AK DAVA neferimiz olan \ud83d\udc49 @OrhanBirinci61 karde\u015fimiz madur durumdad\u0131r.. Kanser hastas\u0131 anne\u2026 https:\/\/t.co\/QcYZFnAQ4U","source":"\u003ca href=\"http:\/\/twitter.com\/download\/iphone\" rel=\"nofollow\"\u003eTwitter for iPhone\u003c\/a\u003e","truncated":true,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":897005867454914560,"id_str":"897005867454914560","name":"\u2130\u212c\u211b\u10ae\u2112\u2148\u2102\u2130\u00a0\u211b\u1768 \ud83c\uddef\ud83c\uddf4\ud83c\uddf9\ud83c\uddf7","screen_name":"ebr_lice","location":"Kayseri, T\u00fcrkiye","url":null,"description":"B\u0130ZLER BU VATANIN BEK\u00c7\u0130LER\u0130Y\u0130Z \u015eEHZADE GRUPLARI #\u015eEHZADEGRUPLARI","translator_type":"none","protected":false,"verified":false,"followers_count":5953,"friends_count":5061,"listed_count":5,"favourites_count":31560,"statuses_count":30520,"created_at":"Mon Aug 14 08:03:59 +0000 2017","utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":"tr","contributors_enabled":false,"is_translator":false,"profile_background_color":"F5F8FA","profile_background_image_url":"","profile_background_image_url_https":"","profile_background_tile":false,"profile_link_color":"1DA1F2","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/939471488318689280\/zUgIPCK4_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/939471488318689280\/zUgIPCK4_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/897005867454914560\/1509195967","default_profile":true,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"extended_tweet":{"full_text":"#AfrinOperasyonu\nDe\u011ferli AK DAVA neferimiz olan \ud83d\udc49 @OrhanBirinci61 karde\u015fimiz madur durumdad\u0131r.. Kanser hastas\u0131 annesi i\u00e7in bor\u00e7 alt\u0131na girmi\u015f ve \u00e7al\u0131\u015fmad\u0131\u011f\u0131 i\u00e7in \u00f6deyememektedir..\nBu arkada\u015f\u0131m\u0131z\u0131n maduriyetinin giderilmesini istiyoruz \n\nSES\u0130M\u0130Z\u0130 DUYUN!!\n\ud83d\udc47\ud83d\udc47\ud83d\udc47\ud83d\udc47\ud83d\udc47\ud83d\udc47\n@ahmetmgenc","display_text_range":[0,272],"entities":{"hashtags":[{"text":"AfrinOperasyonu","indices":[0,16]}],"urls":[],"user_mentions":[{"screen_name":"OrhanBirinci61","name":"Orhan Birinci","id":2850292745,"id_str":"2850292745","indices":[50,65]},{"screen_name":"ahmetmgenc","name":"Av. Ahmet Metin GEN\u00c7","id":2547626028,"id_str":"2547626028","indices":[261,272]}],"symbols":[]}},"quote_count":0,"reply_count":9,"retweet_count":102,"favorite_count":126,"entities":{"hashtags":[{"text":"AfrinOperasyonu","indices":[0,16]}],"urls":[{"url":"https:\/\/t.co\/QcYZFnAQ4U","expanded_url":"https:\/\/twitter.com\/i\/web\/status\/954736231946047489","display_url":"twitter.com\/i\/web\/status\/9\u2026","indices":[117,140]}],"user_mentions":[{"screen_name":"OrhanBirinci61","name":"Orhan Birinci","id":2850292745,"id_str":"2850292745","indices":[50,65]}],"symbols":[]},"favorited":false,"retweeted":false,"filter_level":"low","lang":"tr"},"is_quote_status":false,"quote_count":0,"reply_count":0,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[{"text":"AfrinOperasyonu","indices":[14,30]}],"urls":[],"user_mentions":[{"screen_name":"ebr_lice","name":"\u2130\u212c\u211b\u10ae\u2112\u2148\u2102\u2130\u00a0\u211b\u1768 \ud83c\uddef\ud83c\uddf4\ud83c\uddf9\ud83c\uddf7","id":897005867454914560,"id_str":"897005867454914560","indices":[3,12]},{"screen_name":"OrhanBirinci61","name":"Orhan Birinci","id":2850292745,"id_str":"2850292745","indices":[64,79]}],"symbols":[]},"favorited":false,"retweeted":false,"filter_level":"low","lang":"tr","timestamp_ms":"1516472627659"})
        tags = extract_hashtags(json_string)
        self.assertTrue(tags is not None)


if __name__ == '__main__':
    unittest.main()