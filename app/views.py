from app import app
from flask import Flask, render_template, request
#from chart import one_month_average

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
@app.route('/charts/<handle>/<api>' , methods = ["POST"])
def charts(handle, api):
    clicked = None
    if request.method == "POST":
        print(handle, api)

        # api =  form["api"]
        # print(handle, api)
        print('hello')
    return "hello"
