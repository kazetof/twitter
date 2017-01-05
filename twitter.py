#coding: UTF-8
from twython import Twython
import numpy as np
import time

APP_KEY = ''
APP_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

twitter = Twython(app_key=APP_KEY, app_secret=APP_SECRET, oauth_token=ACCESS_TOKEN, oauth_token_secret=ACCESS_TOKEN_SECRET)
#auth = twitter.get_authentication_tokens()
#OAUTH_TOKEN = auth['oauth_token']
#OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

#to get the people who 'screen_name' is following.
screen_name = u'NAME'
friend = twitter.get_friends_list(screen_name=screen_name,count=5)
for i in np.arange(3):
    print("ID : {0:d}".format(friend[u'users'][i]['id']))
    print(friend[u'users'][i]['name'])

#to get the people who 'screen_name' is followed.  
next_cursor = -1
count = 0
auto_follow_bool = False
while next_cursor != 0:
    followers = twitter.get_followers_list(screen_name=screen_name,cursor=next_cursor,count=200)
    for i in np.arange(len(followers[u'users'])):
        print("Count : {0:d}".format(count))
        print("ID : {0:d}".format(followers[u'users'][i]['id']))
        print(followers[u'users'][i]['name'])
        count += 1
        if auto_follow_bool == True:
            twitter.create_friendship(user_id=followers[u'users'][i]['id'],follow=True)
            sleeptime = np.random.random(1)[0]*20
            time.sleep(sleeptime)
            
    next_cursor = followers[u'next_cursor']
    print("next_cursor : {0:d}".format(next_cursor))


#twitter.get_friends_ids()
#twitter.get_followers_list()
#twitter.show_friendship(source_id=id1,target_id=id2)
#twitter.update_status(status='See how easy using Twython is!')
#twitter.get_available_trends()
