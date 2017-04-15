import tweepy #https://github.com/tweepy/tweepy

#Twitter API credentials
consumer_key = 'XuJqupkF9ZUq8oIz921Nl141O'
consumer_secret = '9z0JyLdMNRT7brH14wh32fUqxbpL0yDXu70Ez8mJFpLifmv3nl'
access_key = '853038411426521090-yviLNx5KWrXE7lXrubdjKlwOQ0WoC8R'
access_secret = 'wCxcNrBfJi2PhTVw9Xgi1DF4EFb1Z38cS7z0PAgC3Jd6D'


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method

	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#initialize a list to hold all the tweepy Tweets
	alltweets = []

	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)

	#save most recent tweets
	alltweets.extend(new_tweets)

	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1

	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		#print "getting tweets before %s" % (oldest)

		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

		#save most recent tweets
		alltweets.extend(new_tweets)

		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1

		#print "...%s tweets downloaded so far" % (len(alltweets))

	#transform the tweepy tweets into a 2D array that will populate the csv
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

	#return outtweets
	#write the csv
	with open('%s.txt' % screen_name, 'w') as f:
		for i in outtweets:
			f.write(str(i[1])+'\t')
			f.write(str(i[2])+'\n')

	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("HackSentivents")
