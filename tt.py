import tweepy
from time import sleep

consumer_key = 'mQ5lJCIWJrybdnIcgChfWcXhp'
consumer_secret = 'EKQSXC0p4IlFxw8DAiQDa5jexSmABz78qTx39RVCtoKDsdPcKs'
access_token = '4136896132-4Nw1Prlbb7s3y41GKRqGpWbfpUxyOEcvnBgL5hk'
access_token_secret = 'fag32MPJ7iubwTcf5O2IviVtiqlSTBARQyPIEgFXrgxWX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


def get_followes_list():
	followers=[]
	for user in tweepy.Cursor(api.followers,screen_name="twitter").items():
		followers.append(user.screen_name)
		sleep(2)
	return followers

def get_friends_list():
	friends=[]
	with open("friends.txt", "+a") as file:
		for user in tweepy.Cursor(api.friends,screen_name="twitter").items():
			file.write(user)
			sleep(2)

def get_followers_by_id(id_number):
	user=api.get_user(id_number)
	return user.followers_count

def check_friendship(user_a,user_b):
	return api.exists_friendship(user_a,user_b)


print(check_friendship("EnricoMoses"))
	file = open("followers.txt", 'r')


