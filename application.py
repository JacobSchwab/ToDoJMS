from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():

    str1 = "TO DO:" \
           "finish the todo list app " \
           "..." \
           "profit"
    return (str1)