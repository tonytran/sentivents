import indicoio
import parse
indicoio.config.api_key = 'a2225f696d231a267eeab8e884d85449'

# single example
def analyze_tweets(tweet_dict):
    indico_dict = {}

    for key in tweet_dict:
        indico_dict[key] = []
        for tweet in tweet_dict[key]:
            indico_dict[key].append(indicoio.analyze_text(tweet, apis=['sentiment', 'political','twitter_engagement','personality','personas','emotion']))

if __name__ == '__main__':
	#pass in the username of the account you want to download
    analyze_tweets(parse.organize_tweets(parse.parse_tweets("HackSentivents")))



def average_data(indico_dict):

    print('done analyzing tweets, calculating now')

    monthly_data = {}

    for month in indico_dict:
        sentiment = 0
        twitter_engagement = 0
        personality = {'openness': 0, 'extraversion': 0, 'agreeableness': 0, 'conscientiousness': 0}
        political = {'Libertarian': 0, 'Liberal': 0, 'Green': 0, 'Conservative': 0}
        personas = {'advocate': 0, 'debater': 0, 'mediator': 0, 'consul': 0, 'executive': 0, 'adventurer': 0, 'logistician': 0, 'commander': 0,
                    'entrepreneur': 0, 'logician': 0, 'protagonist': 0, 'architect': 0, 'campaigner': 0, 'entertainer': 0, 'defender': 0, 'virtuoso': 0}
        emotion = {'anger': 0, 'joy': 0, 'fear': 0, 'sadness': 0, 'surprise': 0}

        #each tweet is the dictinary that holds the data per tweet
        for tweet in indico_dict[month]:

            sentiment += tweet['sentiment']
            twitter_engagement += tweet['twitter_engagement']
            personality['openness'] += tweet['personality']['openness']
            personality['extraversion'] += tweet['personality']['extraversion']
            personality['agreeableness'] += tweet['personality']['agreeableness']
            personality['conscientiousness'] += tweet['personality']['conscientiousness']
            political['Libertarian'] += tweet['political']['Libertarian']
            political['Liberal'] += tweet['political']['Liberal']
            political['Green'] += tweet['political']['Green']
            political['Conservative'] += tweet['political']['Conservative']
            personas['advocate'] += tweet['personas']['advocate']
            personas['debater'] += tweet['personas']['debater']
            personas['mediator'] += tweet['personas']['mediator']
            personas['consul'] += tweet['personas']['consul']
            personas['executive'] += tweet['personas']['executive']
            personas['adventurer'] += tweet['personas']['adventurer']
            personas['logistician'] += tweet['personas']['logistician']
            personas['commander'] += tweet['personas']['commander']
            personas['entrepreneur'] += tweet['personas']['entrepreneur']
            personas['logician'] += tweet['personas']['advocate']
            personas['protagonist'] += tweet['personas']['advocate']
            personas['architect'] += tweet['personas']['advocate']
            personas['campaigner'] += tweet['personas']['advocate']
            personas['entertainer'] += tweet['personas']['advocate']
            personas['defender'] += tweet['personas']['advocate']
            personas['virtuoso'] += tweet['personas']['advocate']
            emotion['anger'] += tweet['emotion']['anger']
            emotion['joy'] += tweet['emotion']['joy']
            emotion['fear'] += tweet['emotion']['fear']
            emotion['sadness'] += tweet['emotion']['sadness']
            emotion['surprise'] += tweet['emotion']['surprise']

        sentiment = sentiment / len(indico_dict[month])
        twitter_engagementent = twitter_engagement / len(indico_dict[month])
        personality['openness'] = personality['openness'] / len(indico_dict[month])
        personality['extraversion'] = personality['extraversion'] / len(indico_dict[month])
        personality['agreeableness'] = personality['agreeableness'] / len(indico_dict[month])
        personality['conscientiousness'] = personality['conscientiousness'] / len(indico_dict[month])
        political['Libertarian'] = political['Libertarian'] / len(indico_dict[month])
        political['Liberal'] = political['Liberal'] / len(indico_dict[month])
        political['Green'] = political['Green'] / len(indico_dict[month])
        political['Conservative'] = political['Conservative'] / len(indico_dict[month])
        personas['advocate'] = personas['advocate'] / len(indico_dict[month])
        personas['debater'] = personas['debater'] / len(indico_dict[month])
        personas['mediator'] = personas['mediator'] / len(indico_dict[month])
        personas['consul'] = personas['consul'] / len(indico_dict[month])
        personas['executive'] = personas['executive'] / len(indico_dict[month])
        personas['adventurer'] = personas['adventurer'] / len(indico_dict[month])
        personas['logistician'] = personas['logistician'] / len(indico_dict[month])
        personas['commander'] = personas['commander'] / len(indico_dict[month])
        personas['entrepreneur'] = personas['entrepreneur'] / len(indico_dict[month])
        personas['logician'] = personas['logician'] / len(indico_dict[month])
        personas['protagonist'] = personas['protagonist'] / len(indico_dict[month])
        personas['architect'] = personas['architect'] / len(indico_dict[month])
        personas['campaigner'] = personas['campaigner'] / len(indico_dict[month])
        personas['entertainer'] = personas['entertainer'] / len(indico_dict[month])
        personas['defender'] = personas['defender'] / len(indico_dict[month])
        personas['virtuoso'] = personas['virtuoso'] / len(indico_dict[month])
        emotion['anger'] = emotion['anger'] / len(indico_dict[month])
        emotion['joy'] = emotion['joy'] / len(indico_dict[month])
        emotion['fear'] = emotion['fear'] / len(indico_dict[month])
        emotion['sadness'] = emotion['sadness'] / len(indico_dict[month])
        emotion['surprise'] = emotion['surprise'] / len(indico_dict[month])

        monthly_data[month] = [{'sentiment' : copy.deepcopy(sentiment)}]
        monthly_data[month].append({'twitter_engagementent' : copy.deepcopy(twitter_engagementent)})
        monthly_data[month].append({'personality' : copy.deepcopy(personality)})
        monthly_data[month].append({'political' : copy.deepcopy(political)})
        monthly_data[month].append({'personas' : copy.deepcopy(personas)})
        monthly_data[month].append({'emotion' : copy.deepcopy(emotion)})

    return (monthly_data)

    def analyze_tweets(tweet_dict):

        print('done organizing tweets, analyzing now')

        indico_dict = {}
        tweet_batches = {}

        for key in tweet_dict:
            tweet_batches[key] = []
            for tweet in tweet_dict[key]:
                tweet_batches[key].append(tweet)

        for month in tweet_batches:
            indico_dict[month] = []
            returndict = (indicoio.analyze_text(tweet_batches[month], apis=['sentiment','twitter_engagement','political','personality','personas','emotion']))
            indico_dict[month].append({'sentiment' : sum(returndict['sentiment'])/len(returndict['sentiment'])})
            indico_dict[month].append({'twitter_engagement' : sum(returndict['twitter_engagement'])/len(returndict['twitter_engagement'])})

            indico_dict[month].append({'political': {'Libertarian': 0, 'Liberal': 0, 'Green': 0, 'Conservative': 0}})
            for mydict in returndict['political']:
                indico_dict[month][2]['political']['Libertarian'] += mydict['Libertarian']
                indico_dict[month][2]['political']['Liberal'] += mydict['Liberal']
                indico_dict[month][2]['political']['Green'] += mydict['Green']
                indico_dict[month][2]['political']['Conservative'] += mydict['Conservative']
            indico_dict[month][2]['political']['Libertarian'] = indico_dict[month][2]['political']['Libertarian']/len(returndict['political'])
            indico_dict[month][2]['political']['Liberal'] = indico_dict[month][2]['political']['Liberal']/len(returndict['political'])
            indico_dict[month][2]['political']['Green'] = indico_dict[month][2]['political']['Green']/len(returndict['political'])
            indico_dict[month][2]['political']['Conservative'] = indico_dict[month][2]['political']['Conservative']/len(returndict['political'])

            indico_dict[month].append({'personality': {'openness': 0, 'extraversion': 0, 'agreeableness': 0, 'conscientiousness': 0}})
            for mydict in returndict['personality']:
                indico_dict[month][3]['personality']['openness'] += mydict['openness']
                indico_dict[month][3]['personality']['extraversion'] += mydict['extraversion']
                indico_dict[month][3]['personality']['agreeableness'] += mydict['agreeableness']
                indico_dict[month][3]['personality']['conscientiousness'] += mydict['conscientiousness']
            indico_dict[month][3]['personality']['openness'] = indico_dict[month][3]['personality']['openness']/len(returndict['personality'])
            indico_dict[month][3]['personality']['extraversion'] = indico_dict[month][3]['personality']['extraversion']/len(returndict['personality'])
            indico_dict[month][3]['personality']['agreeableness'] = indico_dict[month][3]['personality']['agreeableness']/len(returndict['personality'])
            indico_dict[month][3]['personality']['conscientiousness'] = indico_dict[month][3]['personality']['conscientiousness']/len(returndict['personality'])

            indico_dict[month].append({'emotion': {'anger': 0, 'joy': 0, 'fear': 0, 'sadness': 0, 'surprise' : 0}})
            for mydict in returndict['emotion']:
                indico_dict[month][4]['emotion']['anger'] += mydict['anger']
                indico_dict[month][4]['emotion']['joy'] += mydict['joy']
                indico_dict[month][4]['emotion']['fear'] += mydict['fear']
                indico_dict[month][4]['emotion']['sadness'] += mydict['sadness']
                indico_dict[month][4]['emotion']['surprise'] += mydict['surprise']
            indico_dict[month][4]['emotion']['anger'] = indico_dict[month][4]['emotion']['anger']/len(returndict['emotion'])
            indico_dict[month][4]['emotion']['joy'] = indico_dict[month][4]['emotion']['joy']/len(returndict['emotion'])
            indico_dict[month][4]['emotion']['fear'] = indico_dict[month][4]['emotion']['fear']/len(returndict['emotion'])
            indico_dict[month][4]['emotion']['sadness'] = indico_dict[month][4]['emotion']['sadness']/len(returndict['emotion'])
            indico_dict[month][4]['emotion']['surprise'] = indico_dict[month][4]['emotion']['surprise']/len(returndict['emotion'])

            indico_dict[month].append({'personas': {'advocate': 0, 'debater': 0, 'mediator': 0, 'consul': 0, 'executive' : 0, 'adventurer' : 0, 'logistician' : 0,
            'commander' : 0, 'entrepreneur' : 0, 'logician' : 0, 'protagonist' : 0, 'architect' : 0, 'campaigner' : 0, 'entertainer' : 0, 'defender' : 0, 'virtuoso' : 0}})
            for mydict in returndict['personas']:
                indico_dict[month][5]['personas']['advocate'] += mydict['advocate']
                indico_dict[month][5]['personas']['debater'] += mydict['debater']
                indico_dict[month][5]['personas']['mediator'] += mydict['mediator']
                indico_dict[month][5]['personas']['consul'] += mydict['consul']
                indico_dict[month][5]['personas']['executive'] += mydict['executive']
                indico_dict[month][5]['personas']['adventurer'] += mydict['adventurer']
                indico_dict[month][5]['personas']['logistician'] += mydict['logistician']
                indico_dict[month][5]['personas']['commander'] += mydict['commander']
                indico_dict[month][5]['personas']['entrepreneur'] += mydict['entrepreneur']
                indico_dict[month][5]['personas']['logician'] += mydict['logician']
                indico_dict[month][5]['personas']['protagonist'] += mydict['protagonist']
                indico_dict[month][5]['personas']['architect'] += mydict['architect']
                indico_dict[month][5]['personas']['campaigner'] += mydict['campaigner']
                indico_dict[month][5]['personas']['entertainer'] += mydict['entertainer']
                indico_dict[month][5]['personas']['defender'] += mydict['defender']
                indico_dict[month][5]['personas']['virtuoso'] += mydict['virtuoso']
            indico_dict[month][5]['personas']['advocate'] = indico_dict[month][5]['personas']['advocate']/len(returndict['personas'])
            indico_dict[month][5]['personas']['debater'] = indico_dict[month][5]['personas']['debater']/len(returndict['personas'])
            indico_dict[month][5]['personas']['mediator'] = indico_dict[month][5]['personas']['mediator']/len(returndict['personas'])
            indico_dict[month][5]['personas']['consul'] = indico_dict[month][5]['personas']['consul']/len(returndict['personas'])
            indico_dict[month][5]['personas']['executive'] = indico_dict[month][5]['personas']['executive']/len(returndict['personas'])
            indico_dict[month][5]['personas']['adventurer'] = indico_dict[month][5]['personas']['adventurer']/len(returndict['personas'])
            indico_dict[month][5]['personas']['logistician'] = indico_dict[month][5]['personas']['logistician']/len(returndict['personas'])
            indico_dict[month][5]['personas']['commander'] = indico_dict[month][5]['personas']['commander']/len(returndict['personas'])
            indico_dict[month][5]['personas']['entrepreneur'] = indico_dict[month][5]['personas']['entrepreneur']/len(returndict['personas'])
            indico_dict[month][5]['personas']['logician'] = indico_dict[month][5]['personas']['logician']/len(returndict['personas'])
            indico_dict[month][5]['personas']['protagonist'] = indico_dict[month][5]['personas']['protagonist']/len(returndict['personas'])
            indico_dict[month][5]['personas']['architect'] = indico_dict[month][5]['personas']['architect']/len(returndict['personas'])
            indico_dict[month][5]['personas']['campaigner'] = indico_dict[month][5]['personas']['campaigner']/len(returndict['personas'])
            indico_dict[month][5]['personas']['entertainer'] = indico_dict[month][5]['personas']['entertainer']/len(returndict['personas'])
            indico_dict[month][5]['personas']['defender'] = indico_dict[month][5]['personas']['defender']/len(returndict['personas'])
            indico_dict[month][5]['personas']['virtuoso'] = indico_dict[month][5]['personas']['virtuoso']/len(returndict['personas'])

        return indico_dict

        import scrape

        def parse_tweets(screen_name):

            scrape.get_all_tweets(screen_name)
            tweetlist = []
            f = open('%s.txt' % screen_name, 'r')
            for line in f:
                lines = line.split('\t')
                lines[0] = lines[0][:-9]
                lines[1] = lines[1][2:-2]
                tweetlist.append(lines)
            f.close()

            return tweetlist

        def organize_tweets(tweets):
            for tweet in tweets:
                if tweet[0][5:7] == '01':
                    tweet[0] = 'January' + str(tweet[0][0:4])
                elif tweet[0][5:7] == '02':
                    tweet[0] = 'February' + str(tweet[0][0:4])
                elif tweet[0][5:7] == '03':
                    tweet[0] = 'March' + str(tweet[0][0:4])
                elif tweet[0][5:7] == '04':
                    tweet[0] = 'April' + str(tweet[0][0:4])
                elif tweet[0][5:7] == '05':
                    tweet[0] = 'May' + str(tweet[0][0:4])
                elif tweet[0][5:7] == '06':
                    tweet[0] = 'June' + str(tweet[0][0:4])
                elif tweet[0][5:7] == '07':
                    tweet[0] = 'July' + str(tweet[0][0:4])
                elif tweet[0][5:7] == '08':
                    tweet[0] = 'August' + str(tweet[0][0:4])
                elif tweet[0][5:7] == '09':
                    tweet[0] = 'September' + str(tweet[0][0:4])
                elif tweet[0][5:7] == '10':
                    tweet[0] = 'October' + str(tweet[0][0:4])
                elif tweet[0][5:7] == '11':
                    tweet[0] = 'November' + str(tweet[0][0:4])
                elif tweet[0][5:7] == '12':
                    tweet[0] = 'December' + str(tweet[0][0:4])

            tweet_dict={}

            for tweet in tweets:
                if tweet[0] not in tweet_dict:
                    tweet_dict[tweet[0]] = [tweet[1]]
                else:
                    tweet_dict[tweet[0]].append(tweet[1])

            return tweet_dict

        if __name__ == '__main__':
        	#pass in the username of the account you want to download
        	organize_tweets(parse_tweets("HackSentivents"))

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
