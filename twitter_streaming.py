import tweepy
import requests # request img from web
import shutil # save img locally
import os
from tankbuster.engine.detect import bust
from utils import list_pictures
from os.path import exists as file_exists
import time
import json
import pandas as pd
from googletrans import Translator
import csv
import numpy as np
from classify_tweets import *

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAAfsggEAAAAAeAn2S6iLPXOESLxTm%2BzfIwZsvO0%3DEyD7sWM3vL9MLZ33lwif34QRxZzcfH0DzYNZQb5XoRxeXLhFpz'
csv_file_name = 'tweet_data.csv'
filtering_rule = 'has:media Ukraine OR Kherson OR War OR tank OR танк'

#inherites tweepy.StreamClient
class TwitterStream(tweepy.StreamingClient):
    def on_data(self, raw_data):
        
        try:
            detectBody(raw_data)
            #time.sleep(5)
        except BaseException as err:
            print("Something happend: ", err)

def detectBody(raw_data):

    media_url = None    
    data = json.loads(raw_data)
    coordinates_list = None
    coordinates = ''

    if 'includes' in data:
        if 'media' in data['includes']:
            for i in range(len(data['includes']['media'])):
                if 'url' in data['includes']['media'][i]:
                    media_url = data['includes']['media'][i]['url']
                elif 'preview_image_url' in data['includes']['media'][i]:
                    media_url = data['includes']['media'][i]['preview_image_url']
        if 'places' in data['includes']:
            coordinates_list = data['includes']['places'][0]['geo']['bbox']

    if data['data']['text'] != None:
        target_text = data['data']['text']
        print('Ivan: analyzing a tweet -- ' + target_text + '\n')

        text_class = classify_mil_text(target_text)
        if text_class.get('pred') == 'military' and text_class.get('prob_mil') >= 0.60:

            print('Ivan: ' + u'\u2191\u2191\u2191' + 'found a tweet relavant to the military domain....\n')

            if media_url != None:
                #print("Examining image: "+media_url)
                file_name = './images/'+media_url[-19:]

                res = requests.get(media_url, stream = True)
                if res.status_code == 200 and not file_exists(file_name):
                    with open(file_name,'wb') as f:
                        shutil.copyfileobj(res.raw, f)
                    #print('Image sucessfully Downloaded: ', file_name)

                    # Feed images to the classifier to retrieve a dictionary of predictions
                    preds = bust(file_name, network='ResNet')

                    # Get the prediction with the highest probability
                    pred = max(preds, key=preds.get)

                    if ('t-72' in pred or 'bmp' in pred) and preds[pred] >= 0.40:
                        #Print the prediction
                        print('Ivan: ' + u'\u2191\u2191\u2191' + ' {} - Russian tank images detected ({:.2f}%) ...\n'.format(file_name,
                                                                           preds[pred] * 100))
                        #print("The image url is: "+media_url+"\n\n")

                        user_id = data['includes']['users'][len(data['includes']['users'])-1]['id']
                        user_name = data['includes']['users'][len(data['includes']['users'])-1]['name']
                        
                        if coordinates_list != None:
                            tweet_info = {
                                'id': data['data']['id'],
                                'user_id' : user_id,
                                'user_name': user_name,
                                'tweet_address': 'https://twitter.com/anyuser/status/'+data['data']['id'],
                                'text': target_text,
                                'image_url': media_url,
                                'coordinate': coordinates.join(coordinates_list)
                            }
                        else:
                            tweet_info = {
                                'id': data['data']['id'],
                                'user_id' : user_id,
                                'user_name': user_name,
                                'tweet_address': 'https://twitter.com/anyuser/status/'+data['data']['id'],
                                'text': target_text,
                                'image_url': media_url,
                            }

                        temp_df = pd.DataFrame([tweet_info])

                        #Use this line when a dataframe with whole data within a session is needed...
                        #tweet_info_df = pd.concat([tweet_info_df, temp_df], ignore_index=True)
                        
                        with open(csv_file_name , 'a+', newline='') as fd:
                            write = csv.DictWriter(fd, fieldnames = list(tweet_info.keys()))
                            if os.path.isfile('./'+csv_file_name) != True:
                                write.writeheader()
                                write.writerow(tweet_info)
                            else:
                                write.writerow(tweet_info)

                    else:
                        os.remove(file_name)


# 규칙 제거 함수
def delete_all_rules(rules):
    if rules is None or rules.data is None:
        return None
    stream_rules = rules.data
    ids = list(map(lambda rule: rule.id, stream_rules))
    streamClient.delete_rules(ids=ids)

############################################

tweet_info_df = pd.DataFrame()

# 스트림 클라이언트 인스터턴스 생성
streamClient = TwitterStream(BEARER_TOKEN)

# 모든 규칙 불러오기 - id값을 지정하지 않으면 모든 규칙을 불러옴
rules = streamClient.get_rules()

# 모든 규칙 제거
delete_all_rules(rules)

# 스트림 규칙 추가
streamClient.add_rules(tweepy.StreamRule(value=filtering_rule))

# 스트림 시작
streamClient.filter(tweet_fields=['geo','context_annotations','created_at'], user_fields='description', media_fields=['preview_image_url,url'],
                                                                        place_fields=["id","geo","name","country_code","place_type","full_name","country"],expansions=['attachments.media_keys','author_id','geo.place_id'])
