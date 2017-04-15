# from flask import Flask, render_template, jsonify, request
from os import environ



app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():

    options = ["sentiment-analysis", "political-analysis", "myers-briggs", "twitter-engagement", "personality" , "emotional-analysis"]
    return render_template("index.html" ,options = options)

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
def barGraph():
    data1 = [] #list of labels
    data2 = [] #list of
    pass
@app.route('/changeOver')
def lineGraph():
    pass
def peakCircles():
    pass
def gaugeChart():
    pass
@app.route('/post' , methods = ["POST"])
def queryOnUser():
    if request.method == 'POST':
        form = request.form
        twitterHandle = form['user-handle']
        selection = form['type']
        #pass data in and do processing

        if selection == "sentiment-analysis":
            pass
        elif selection == "political-analysis":
            pass
        elif selection == "myers-briggs":
            pass
        elif selection == "twitter-engagement":
            pass
        elif selection == "personality":
            pass
        elif selection == "emotion":
            pass






app.run(debug=True, port=environ.get("PORT", 5000))#, host = '0.0.0.0')
