from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():

    str1 = '''TODO List:   
Finish TODO App   
...   
Profit'''
    return (str1)