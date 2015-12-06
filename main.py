__author__ = 'willb'
import scripts.screenmain as screenmain
import scripts.flaskserver as flaskserver
import webview
import requests
import threading
import scripts.logs
import __builtin__

__builtin__.logs = scripts.logs.logs()


class main():
    def flaskthread(self):
        flaskserver.start()
        logs.log("Flask shut down")
        flaskdone = True

    def __init__(self):
        global flaskdone
        flaskdone = False
        logs.log("Starting flask server")
        t = threading.Thread(target=self.flaskthread())
        t.start()
        logs.log("Starting ui")
        screenmain.main()
if __name__ == "__main__":
    logs.openlogs()
    main()
