import tweepy
import csv
consumer_key = 'your_key'
consumer_secret = '_your secret'
access_token = 'your access'
access_token_secret = 'your token'

auth  = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

fetch_tweets_1 = tweepy.Cursor(api.search,q ="binance").items(200)

with open("binance.csv",'w',newline='',encoding='UTF-8-sig') as my_file1:
    my_writer = csv.writer(my_file1,delimiter=',')
    my_writer.writerow(['tweet_ID','user_ID','text','created_time','location','followers','follows','verified','repost','repost_count'])
    for i in fetch_tweets_1:  
        tweet_id = str(i.id)
        tweet_id = tweet_id.replace(',',';')
        tweet_id = tweet_id.replace('，',';')
        tweet_id = tweet_id.replace('\n',';')

        user_id = str(i.user.id)
        user_id = user_id.replace(',',';')
        user_id = user_id.replace('，',';')
        user_id = user_id.replace('\n',';')

        text = str(i.text)
        text = text.replace(',',';')
        text = text.replace('，',';')
        text = text.replace('\n',';')

        created_time = str(i.created_at)
        created_time = created_time.replace(',',';')
        created_time = created_time.replace('，',';')
        created_time = created_time.replace('\n',';')

        location  = str(i.user.location)
        location = location.replace(',',';')
        location = location.replace('，',';')
        location = location.replace('\n',';')

        followers = str(i.user.followers_count)
        followers = followers.replace(',',';')
        followers = followers.replace('，',';')
        followers = followers.replace('\n',';')

        follows = str(i.user.friends_count)
        follows = follows.replace(',',';')
        follows = follows.replace('，',';')
        follows = follows.replace('\n',';')

        verified = str(i.user.verified)
        verified =verified.replace(',',';')
        verified =verified.replace('，',';')
        verified =verified.replace('\n',';')

        repost=str(i.retweeted)
        repost =repost.replace(',',';')
        repost =repost.replace('，',';')
        repost =repost.replace('\n',';')

        repost_count  = str(i.retweet_count)
        repost_count =repost_count.replace(',',';')
        repost_count =repost_count.replace('，',';')
        repost_count =repost_count.replace('\n',';')

        my_writer.writerow([tweet_id,user_id,text,created_time,location,followers,follows,verified,repost,repost_count])
 


