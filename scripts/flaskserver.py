__author__ = 'willb'
from flask import Flask
from flask import request
import scripts.screenmain as screenmain
import threading
import scripts.settings as settings
import sys
import webview
app = Flask(__name__)
@app.route("/")
def main():
    action=request.args.get("action",'')
    print("Action is {0}".format(action))
    if action is None:
        print("Action was none")
        return "Action cannot be None"
    if action=="start":
        print("Action was start")
        screenmain.main()
    elif action == "settings":
        print("Action was settings")
        settings.main()
    elif action=="exit":
        print("Action was ssettings")
        sys.exit()
def start():
    print("In flask server thread")
    app.run()