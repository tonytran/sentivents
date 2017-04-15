import copy

def one_month_average(screen_name, data_type):
    infile = open('data\\'+screen_name+'_indico.csv', 'r')
    keys = infile.readline().split(',')
    monthdata = {}
    returndata = {}
    data = infile.readline().split(',')

    i = 0
    for key in keys:
        monthdata[key.strip('\n')] = data[i].strip('\n').strip("'")
        i += 1
    infile.close()
    if data_type == 'sentiment':
        returndata[data_type+'_average'] = monthdata[data_type]
    elif data_type == 'twitter_engagement':
        returndata[data_type+'_average'] = monthdata[data_type]
    elif data_type == 'personality':
        returndata['personality_openness'+'_average'] = monthdata['personality_openness']
        returndata['personality_extraversion'+'_average'] = monthdata['personality_extraversion']
        returndata['personality_agreeableness'+'_average'] = monthdata['personality_agreeableness']
        returndata['personality_conscientiousness'+'_average'] = monthdata['personality_conscientiousness']
    elif data_type == 'political':
        returndata['political_Libertarian'+'_average'] = monthdata['political_Libertarian']
        returndata['political_Liberal'+'_average'] = monthdata['political_Liberal']
        returndata['political_Green'+'_average'] = monthdata['political_Green']
        returndata['political_Conservative'+'_average'] = monthdata['political_Conservative']
    elif data_type == 'emotion':
        returndata['emotion_anger'+'_average'] = monthdata['emotion_anger']
        returndata['emotion_joy'+'_average'] = monthdata['emotion_joy']
        returndata['emotion_fear'+'_average'] = monthdata['emotion_fear']
        returndata['emotion_sadness'+'_average'] = monthdata['emotion_sadness']
        returndata['emotion_surprise'+'_average'] = monthdata['emotion_surprise']
    elif data_type == 'personas':
        returndata['personas_advocate'+'_average'] = monthdata['personas_advocate']
        returndata['personas_debater'+'_average'] = monthdata['personas_debater']
        returndata['personas_mediator'+'_average'] = monthdata['personas_mediator']
        returndata['personas_consul'+'_average'] = monthdata['personas_consul']
        returndata['personas_executive'+'_average'] = monthdata['personas_executive']
        returndata['personas_adventurer'+'_average'] = monthdata['personas_adventurer']
        returndata['personas_logistician'+'_average'] = monthdata['personas_logistician']
        returndata['personas_commander'+'_average'] = monthdata['personas_commander']
        returndata['personas_entrepreneur'+'_average'] = monthdata['personas_entrepreneur']
        returndata['personas_logician'+'_average'] = monthdata['personas_logician']
        returndata['personas_protagonist'+'_average'] = monthdata['personas_protagonist']
        returndata['personas_architect'+'_average'] = monthdata['personas_architect']
        returndata['personas_campaigner'+'_average'] = monthdata['personas_campaigner']
        returndata['personas_entertainer'+'_average'] = monthdata['personas_entertainer']
        returndata['personas_defender'+'_average'] = monthdata['personas_defender']
        returndata['personas_virtuoso'+'_average'] = monthdata['personas_virtuoso']
    return returndata

def six_month_average(screen_name, data_type):
    infile = open('data\\'+screen_name+'_indico.csv', 'r')
    keys = infile.readline().split(',')
    monthdata = {}
    returndata = {}
    data = []
    for i in range(6):
        data.append(infile.readline().split(','))

    for dat in data:
        monthdata[dat[0].strip('\n').strip("'")] = []
        for i in range(2,33):
            monthdata[dat[0].strip('\n').strip("'")].append(dat[i].strip('\n').strip("'"))

    i = 0
    for key in keys:
        if key != 'month_year' and key != 'handle':
            tempdict = {}
            for month in monthdata:
                tempdict[key.strip('\n')] = monthdata[month][i]
                monthdata[month][i] = copy.deepcopy(tempdict)
            i +=1

    if data_type == 'sentiment':
        total = 0
        for month in monthdata:
            total += float(monthdata[month][0][data_type])
        returndata[data_type+'_average'] = total/6

    elif data_type == 'twitter_engagement':
        total = 0
        for month in monthdata:
            total += float(monthdata[month][1][data_type])
        returndata[data_type+'_average'] = total/6

    elif data_type == 'personality':
        total = 0
        for month in monthdata:
            total += float(monthdata[month][2]['personality_openness'])
        returndata['personality_openness'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][3]['personality_extraversion'])
        returndata['personality_extraversion'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][4]['personality_agreeableness'])
        returndata['personality_agreeableness'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][5]['personality_conscientiousness'])
        returndata['personality_conscientiousness'+'_average'] = total/6

    elif data_type == 'political':
        total = 0
        for month in monthdata:
            total += float(monthdata[month][6]['political_Libertarian'])
        returndata['political_Libertarian'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][7]['political_Liberal'])
        returndata['political_Liberal'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][8]['political_Green'])
        returndata['political_Green'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][9]['political_Conservative'])
        returndata['political_Conservative'+'_average'] = total/6

    elif data_type == 'personas':
        total = 0
        for month in monthdata:
            total += float(monthdata[month][10]['personas_advocate'])
        returndata['personas_advocate'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][11]['personas_debater'])
        returndata['personas_debater'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][12]['personas_mediator'])
        returndata['personas_mediator'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][13]['personas_consul'])
        returndata['personas_consul'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][14]['personas_executive'])
        returndata['personas_executive'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][15]['personas_adventurer'])
        returndata['personas_adventurer'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][16]['personas_logistician'])
        returndata['personas_logistician'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][17]['personas_commander'])
        returndata['personas_commander'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][18]['personas_entrepreneur'])
        returndata['personas_entrepreneur'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][19]['personas_logician'])
        returndata['personas_logician'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][20]['personas_protagonist'])
        returndata['personas_protagonist'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][21]['personas_architect'])
        returndata['personas_architect'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][22]['personas_campaigner'])
        returndata['personas_campaigner'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][23]['personas_entertainer'])
        returndata['personas_entertainer'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][24]['personas_defender'])
        returndata['personas_defender'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][25]['personas_virtuoso'])
        returndata['personas_virtuoso'+'_average'] = total/6

    elif data_type == 'emotion':
        total = 0
        for month in monthdata:
            total += float(monthdata[month][26]['emotion_anger'])
        returndata['emotion_anger'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][27]['emotion_joy'])
        returndata['emotion_joy'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][28]['emotion_fear'])
        returndata['emotion_fear'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][29]['emotion_sadness'])
        returndata['emotion_sadness'+'_average'] = total/6

        total = 0
        for month in monthdata:
            total += float(monthdata[month][30]['emotion_surprise'])
        returndata['emotion_surprise'+'_average'] = total/6
    infile.close()
    return returndata

def one_year_average(screen_name, data_type):
    infile = open('data\\'+screen_name+'_indico.csv', 'r')
    keys = infile.readline().split(',')
    monthdata = {}
    returndata = {}
    data = []
    for i in range(12):
        data.append(infile.readline().split(','))

    for dat in data:
        monthdata[dat[0].strip('\n').strip("'")] = []
        for i in range(2,33):
            monthdata[dat[0].strip('\n').strip("'")].append(dat[i].strip('\n').strip("'"))

    i = 0
    for key in keys:
        if key != 'month_year' and key != 'handle':
            tempdict = {}
            for month in monthdata:
                tempdict[key.strip('\n')] = monthdata[month][i]
                monthdata[month][i] = copy.deepcopy(tempdict)
            i +=1

    if data_type == 'sentiment':
        total = 0
        for month in monthdata:
            total += float(monthdata[month][0][data_type])
        returndata[data_type+'_average'] = total/12

    elif data_type == 'twitter_engagement':
        total = 0
        for month in monthdata:
            total += float(monthdata[month][1][data_type])
        returndata[data_type+'_average'] = total/12

    elif data_type == 'personality':
        total = 0
        for month in monthdata:
            total += float(monthdata[month][2]['personality_openness'])
        returndata['personality_openness'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][3]['personality_extraversion'])
        returndata['personality_extraversion'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][4]['personality_agreeableness'])
        returndata['personality_agreeableness'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][5]['personality_conscientiousness'])
        returndata['personality_conscientiousness'+'_average'] = total/12

    elif data_type == 'political':
        total = 0
        for month in monthdata:
            total += float(monthdata[month][6]['political_Libertarian'])
        returndata['political_Libertarian'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][7]['political_Liberal'])
        returndata['political_Liberal'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][8]['political_Green'])
        returndata['political_Green'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][9]['political_Conservative'])
        returndata['political_Conservative'+'_average'] = total/12

    elif data_type == 'personas':
        total = 0
        for month in monthdata:
            total += float(monthdata[month][10]['personas_advocate'])
        returndata['personas_advocate'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][11]['personas_debater'])
        returndata['personas_debater'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][12]['personas_mediator'])
        returndata['personas_mediator'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][13]['personas_consul'])
        returndata['personas_consul'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][14]['personas_executive'])
        returndata['personas_executive'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][15]['personas_adventurer'])
        returndata['personas_adventurer'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][16]['personas_logistician'])
        returndata['personas_logistician'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][17]['personas_commander'])
        returndata['personas_commander'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][18]['personas_entrepreneur'])
        returndata['personas_entrepreneur'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][19]['personas_logician'])
        returndata['personas_logician'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][20]['personas_protagonist'])
        returndata['personas_protagonist'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][21]['personas_architect'])
        returndata['personas_architect'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][22]['personas_campaigner'])
        returndata['personas_campaigner'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][23]['personas_entertainer'])
        returndata['personas_entertainer'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][24]['personas_defender'])
        returndata['personas_defender'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][25]['personas_virtuoso'])
        returndata['personas_virtuoso'+'_average'] = total/12

    elif data_type == 'emotion':
        total = 0
        for month in monthdata:
            total += float(monthdata[month][26]['emotion_anger'])
        returndata['emotion_anger'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][27]['emotion_joy'])
        returndata['emotion_joy'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][28]['emotion_fear'])
        returndata['emotion_fear'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][29]['emotion_sadness'])
        returndata['emotion_sadness'+'_average'] = total/12

        total = 0
        for month in monthdata:
            total += float(monthdata[month][30]['emotion_surprise'])
        returndata['emotion_surprise'+'_average'] = total/12
    infile.close()
    return returndata
