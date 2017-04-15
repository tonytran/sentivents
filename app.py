from flask import Flask, render_template, jsonify, request
from os import environ



app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():



    options = ["analyze-by-handle", "analyze-by-trend"]
    return render_template("index.html" ,options = options)

@app.route('/postto', methods=["POST"])
def post():
    if request.method == "POST":
        form = request.form

        for key in form.keys():
            print(form[key])

        try:
            selection = form["selected"]
            text = form["requested"]
            print(selection)
            print(text)
            return render_template("index.html")
        except KeyError:
            print("found error")
            return '''<HTML>
            <h1> error found </h1>
            </html>

            '''
    else:
        return render_template("index.html", options = ["shit", "shit"])




app.run(debug=True, port=environ.get("PORT", 5000))#, host = '0.0.0.0')
