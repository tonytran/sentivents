import scrape

def parse_tweets(screen_name):

    #scrape.get_all_tweets(screen_name)
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
