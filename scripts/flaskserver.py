__author__ = 'willb'
from flask import Flask
from flask import request
import scripts.screenmain as screenmain
import threading
import scripts.settings as settings
import sys
import webview
app = Flask(__name__)
def startui():
    webview.create_window("Wall Program","html/main.html")
@app.route("/")
def main():
    action=request.args.get("action",'')
    logs.log("")
    if action is None:
        return "Action cannot be None"
    if action=="start":
        screenmain.main()
    elif action == "settings":
        settings.main()
    elif action=="exit":
        sys.exit()
def start():
    logs.log("In flask server thread")
    app.run()