from flask import Flask, render_template, jsonify, request
from os import environ



app = Flask(__name__)

@app.route('/')
def index():

    return render_template("index.html")
    
app.run(debug=True, port=environ.get("PORT", 5000))#, host = '0.0.0.0')
