from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():

    str1 = "finish the todo list app"
    str2 = "\n"
    str3 = "take a nap"
    return ("TO DO: " + str2 + str1 + str2 + str3)