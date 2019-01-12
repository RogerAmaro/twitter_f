import tweepy
from time import sleep

consumer_key = 'mQ5lJCIWJrybdnIcgChfWcXhp'
consumer_secret = 'EKQSXC0p4IlFxw8DAiQDa5jexSmABz78qTx39RVCtoKDsdPcKs'
access_token = '4136896132-4Nw1Prlbb7s3y41GKRqGpWbfpUxyOEcvnBgL5hk'
access_token_secret = 'fag32MPJ7iubwTcf5O2IviVtiqlSTBARQyPIEgFXrgxWX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


def get_followes_list(screen_name):
	with open("followers.txt", "+a") as file:
		for user in tweepy.Cursor(api.followers,screen_name=screen_name).items():
			file.write(str(user.screen_name)+"\n")
			print(user.screen_name)
			sleep(2)

def get_friends_list(scren_name):
	with open("friends.txt", "+a") as file:
		for user in tweepy.Cursor(api.friends,screen_name=scren_name).items():
			file.write(str(user.screen_name)+"\n")
			print(user.screen_name)
			sleep(2)

def get_followers_by_id(id_number):
	user=api.get_user(id_number)
	return user.followers_count

def followin_me(screen_name):
	with open("followers.txt") as file:
		if screen_name in  file.read().split("\n"):
			return True
		else:
			return False

def follow_peoples(id_tt):
	with open("friends.txt") as file:
		friends = file.read().split("\n")

	for user in tweepy.Cursor(api.followers,screen_name=id_tt).items():
		if not user.screen_name in friends:
			try:
				sleep(15)
				user.follow()
				with open("new_friends.txt",'+a') as file:
					file.write(user.screen_name+"\n")
					print("seguindo:"+user.screen_name)
	
			except Exception as e:
				return e


def who_dont_follow_me():
	black_list = []
	with open("friends.txt") as file:
		array_friends = file.read().split("\n")
	with open("followers.txt") as file1:
		array_followers = file1.read().split("\n")

	for i in array_friends:
		if not i in array_followers:
			black_list.append(i)
	return [black_list, len(black_list)]




print(follow_peoples("MariahCarey"))



