from app import app
from flask import Flask, render_template, request, jsonify
from chart import one_month_average, six_month_average, one_year_average





@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
@app.route('/post', methods=["POST"])
def post():
    if request.method == "POST":
        form = request.form
        try:
            selection = form["selected"]
            handle = form["requested"]
            print(selection)
            print(text)
            return render_template("charts.html")
        except KeyError:
            print("found error")
            return '''<HTML>
            <h1> error found </h1>
            </html>
            '''
    else:
        return render_template("index.html", options = ["shit", "shit"])

@app.route('/average')
def columnChart(handle, tableType):
    data = one_month_average(handle, tableType)
    data2 = six_month_average(handle, tableType)
    data3 = one_year_average(handle,tableType)
    if tableType == "political":
        seriesData = []
        fields = ['libertarian', 'green', 'liberal', 'conservative']
        seriesData.append(data['political_Libertarian_average'])
        seriesData.append(data['political_Green_average'])
        seriesData.append(data['political_Liberal_average'])
        seriesData.append(data['political_Conservative_average'])
        seriesData.append(data['political_Libertarian_average'])
        seriesData.append(data['political_Green_average'])
        seriesData.append(data['political_Liberal_average'])
        seriesData.append(data['political_Conservative_average'])
        seriesData.append(data['political_Libertarian_average'])
        seriesData.append(data['political_Green_average'])
        seriesData.append(data['political_Liberal_average'])
        seriesData.append(data['political_Conservative_average'])
        return jsonify(fields, seriesData)


    elif tableType == "emotion":
        seriesData = []
        fields = ['anger', 'joy', 'fear', 'sadness', 'surprise']
        seriesData.append(data['emotion_anger_average'])
        seriesData.append(data['emotion_joy_average'])
        seriesData.append(data['emotion_fear_average'])
        seriesData.append(data['emotion_sadness_average'])
        seriesData.append(data['emotion_surprise_average'])
        seriesData.append(data2['emotion_anger_average'])
        seriesData.append(data2['emotion_joy_average'])
        seriesData.append(data2['emotion_fear_average'])
        seriesData.append(data2['emotion_sadness_average'])
        seriesData.append(data2['emotion_surprise_average'])
        seriesData.append(data3['emotion_anger_average'])
        seriesData.append(data3['emotion_joy_average'])
        seriesData.append(data3['emotion_fear_average'])
        seriesData.append(data3['emotion_sadness_average'])
        seriesData.append(data3['emotion_surprise_average'])
        return jsonify(fields, seriesData)

    elif tableType == "personality":
        fields = ['extraversion', 'openness', 'agreeableness', 'conscientiousness']
        seriesData = []
        seriesData.append(data['personality_extraversion_average'])
        seriesData.append(data['personality_openness_average'])
        seriesData.append(data['personality_agreeableness_average'])
        seriesData.append(data['personality_conscientiousness_average'])
        seriesData.append(data2['personality_extraversion_average'])
        seriesData.append(data2['personality_openness_average'])
        seriesData.append(data2['personality_agreeableness_average'])
        seriesData.append(data2['personality_conscientiousness_average'])
        seriesData.append(data3['personality_extraversion_average'])
        seriesData.append(data3['personality_openness_average'])
        seriesData.append(data3['personality_agreeableness_average'])
        seriesData.append(data3['personality_conscientiousness_average'])
        return jsonify(fields, seriesData)


def peakCircles(handle, api):
    data = one_year_average(handle, api)
    seriesData = []
    fields = ['architect', 'logician', 'commander','debater','advocate', 'mediator', 'protagonist', 'campaigner', 'logistician', 'defender', 'executive', 'consul', 'virtuoso', 'adventurer', 'entrepreneur', 'entertainer']
    seriesData.append(data['personas_architect_average'])
    seriesData.append(data['personas_logician_average'])
    seriesData.append(data['personas_commander_average'])
    seriesData.append(data['personas_debater_average'])
    seriesData.append(data['personas_advocate_average'])
    seriesData.append(data['personas_mediator_average'])
    seriesData.append(data['personas_protagonist_average'])
    seriesData.append(data['personas_campaigner_average'])
    seriesData.append(data['personas_logistician_average'])
    seriesData.append(data['personas_defender_average'])
    seriesData.append(data['personas_executive_average'])
    seriesData.append(data['personas_consul_average'])
    seriesData.append(data['personas_virtuoso_average'])
    seriesData.append(data['personas_adventurer_average'])
    seriesData.append(data['personas_entrepreneur_average'])
    seriesData.append(data['personas_entertainer_average'])
    return jsonify(fields, seriesData)

def gaugeChart(handle, api):

    if api == "sentiment":
        lists = []
        data = one_month_average(handle, api)
        data2 = six_month_average(handle, api)
        data3 = one_year_average(handle, api)
        print(type(data))
        val1 = data['sentiment_average']
        lists.append(val1)
        val2 = data2['sentiment_average']
        lists.append(val2)
        val3 = data3['sentiment_average']
        lists.append(val3)
        print('hiiii')
        return jsonify(lists)
    else: #twitter-engagement
        lists = []
        data = one_month_average(handle, api)
        data2 = six_month_average(handle, api)
        data3 = one_year_average(handle, api)
        for key in data.keys():
            print(key)
        val1 = data['twitter_engagement_average']
        lists.append(val1)
        val2 = data2['twitter_engagement_average']
        lists.append(val2)
        val3 = data3['twitter_engagement_average']
        lists.append(val3)
        return jsonify(lists)

@app.route('/charts/<handle>/<api>' , methods = ["POST"])
def charts(handle, api):
    clicked = None
    if request.method == "POST":
        print(handle, api)

        if api == "sentiment":
            return gaugeChart(handle, api)
        elif api == "political":
            return columnChart(handle, api)
        elif api == "twitter_engagement":
            return gaugeChart(handle, api)
        elif api == "emotion":
            return columnChart(handle, api)
        elif api == "personality":
            return columnChart(handle, api)
        elif api == "personas":
            return peakCircles(handle, api)
