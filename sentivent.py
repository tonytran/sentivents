import tweepy
import indicoio
import copy
import csv

indicoio.config.api_key = '244bc7ddfa94c013564e4c90eda05720'
key1 = '4ab0b94b8a621102278cb10dd944164a'
key2 = '3b13476b78ad741dd8847f0f7d99fbdb'

consumer_key = 'XuJqupkF9ZUq8oIz921Nl141O'
consumer_secret = '9z0JyLdMNRT7brH14wh32fUqxbpL0yDXu70Ez8mJFpLifmv3nl'
access_key = '853038411426521090-yviLNx5KWrXE7lXrubdjKlwOQ0WoC8R'
access_secret = 'wCxcNrBfJi2PhTVw9Xgi1DF4EFb1Z38cS7z0PAgC3Jd6D'
#screen_name = "HackSentivents"


def get_all_tweets(screen_name):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	alltweets = []
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	alltweets.extend(new_tweets)
	oldest = alltweets[-1].id - 1
	while len(new_tweets) > 0:
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		alltweets.extend(new_tweets)
		oldest = alltweets[-1].id - 1
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	with open('data\\'+screen_name+'.txt', 'w') as f:
		for i in outtweets:
			f.write(str(i[1])+'\t')
			f.write(str(i[2])+'\n')
	pass

def parse_tweets(screen_name):

    print('done getting tweets, parsing now')
    tweetlist = []
    f = open('data\\'+screen_name+'.txt', 'r')
    for line in f:
        lines = line.split('\t')
        lines[0] = lines[0][:-9]
        lines[1] = lines[1][2:-2]
        tweetlist.append(lines)
    f.close()

    return tweetlist

def organize_tweets(tweets):

    print('done parsing tweets, organizing now')

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

def analyze_tweets(tweet_dict):

    print('done organizing tweets, analyzing now')

    indico_dict = {}
    tweet_batches = {}

    for key in tweet_dict:
        tweet_batches[key] = []
        for tweet in tweet_dict[key]:
            tweet_batches[key].append(tweet)

    indicoio.config.api_key = key1
    print('key 1')
    for month in tweet_batches:
        indico_dict[month] = []
        returndict = (indicoio.analyze_text(tweet_batches[month], apis=['sentiment','twitter_engagement','political']))

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


    indicoio.config.api_key = key2
    print('key 2')
    for month in tweet_batches:
        returndict = (indicoio.analyze_text(tweet_batches[month], apis=['personality','personas','emotion']))

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

def csv_write(month_data, screen_name):

    print('done calculating, writing now')

    with open('data\\'+screen_name+'_indico.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["month_year","handle","sentiment","twitter_engagement","personality_openness","personality_extraversion","personality_agreeableness",
        "personality_conscientiousness","political_Libertarian","political_Liberal","political_Green","political_Conservative","personas_advocate",
        "personas_debater","personas_mediator","personas_consul","personas_executive","personas_adventurer","personas_logistician","personas_commander",
        "personas_entrepreneur","personas_logician","personas_protagonist","personas_architect","personas_campaigner","personas_entertainer","personas_defender","personas_virtuoso","emotion_anger","emotion_joy","emotion_fear","emotion_sadness","emotion_surprise"])
        #each month is a list of dicts
        for month in month_data:
            writer.writerow(["'"+month+"'","'"+screen_name+"'",month_data[month][0]['sentiment'],month_data[month][1]['twitter_engagement'],
            month_data[month][3]['personality']['openness'],month_data[month][3]['personality']['extraversion'],
            month_data[month][3]['personality']['agreeableness'],month_data[month][3]['personality']['conscientiousness'],
            month_data[month][2]['political']['Libertarian'],month_data[month][2]['political']['Liberal'],month_data[month][2]['political']['Green'],
            month_data[month][2]['political']['Conservative'],month_data[month][5]['personas']['advocate'],month_data[month][5]['personas']['debater'],
            month_data[month][5]['personas']['mediator'],month_data[month][5]['personas']['consul'],month_data[month][5]['personas']['executive'],
            month_data[month][5]['personas']['adventurer'],month_data[month][5]['personas']['logistician'],month_data[month][5]['personas']['commander'],
            month_data[month][5]['personas']['entrepreneur'],month_data[month][5]['personas']['logician'],month_data[month][5]['personas']['protagonist'],
            month_data[month][5]['personas']['architect'],month_data[month][5]['personas']['campaigner'],month_data[month][5]['personas']['entertainer'],
            month_data[month][5]['personas']['defender'],month_data[month][5]['personas']['virtuoso'],month_data[month][4]['emotion']['anger'],
            month_data[month][4]['emotion']['joy'],month_data[month][4]['emotion']['fear'],month_data[month][4]['emotion']['sadness'],
            month_data[month][4]['emotion']['surprise']])

def create_user_data(screen_name):
    get_all_tweets(screen_name)
    tweets = parse_tweets(screen_name)
    tweets = organize_tweets(tweets)
    tweets = analyze_tweets(tweets)
    csv_write(tweets, screen_name)

if __name__ == '__main__':
    #get_all_tweets(screen_name)
    #tweets = parse_tweets(screen_name)
    #tweets = organize_tweets(tweets)
    #tweets = analyze_tweets(tweets)
    #csv_write(tweets)
    #create_user_data('hampshirecolg')
