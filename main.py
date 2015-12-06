__author__ = 'willb'
import scripts.screenmain as screenmain
import scripts.flaskserver as flaskserver
import webview
import requests
import os
class main():
    def __init__(self):
        print "Starting ui"
        os.system("python {0}/scripts/screenmain.py".format(os.getcwd()))
        print "Starting flask"
        flaskserver.start()
if __name__ == "__main__":
    main()
