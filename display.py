def find_total_averages(screen_name):
    infile = open('data\\'+screen_name+'_indico.csv', 'r')

    names = infile.readline()[:-1].split(',')

    lines = []
    for line in infile:
        if line != '\n':
            lines.append(line[:-1])
    data = {}
    for name in names:
        data[name] = []

#find_total_averages('HackSentivents')
