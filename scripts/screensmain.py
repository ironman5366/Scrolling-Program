__author__ = 'willb'
import scripts.settings as settings
import webview
import time
import thread
import sys
import os
status=True
categories=['dayview','weekview','weather','timescreen','alarm']
catnum=0
class main():
    catnum=0
    def webload(self,url_load):
        webview.load_url(url_load)
    def get_duration(self,screen_name):
        screen_duration = int(settings.main().get_setting(screen_name))
        return screen_duration
    def counter(self, duration, urlload, catnum):
        num=0
        print duration
        duration=float(duration)
        while True:
            time.sleep(0.1)
            num+=(0.1)
            print num
            if duration == num or num > duration:
                global cat
                try:
                    cat=categories[catnum]
                    print cat
                except IndexError:
                    print "Index Error"
                    catnum=0
                    cat=categories[catnum]
                    print cat
                print cat
                catnum+=1
                catduration=self.get_duration(cat)
                if cat==categories[0]:
                    caturl="https://calendar.google.com/?mode=day"
                elif cat==categories[1]:
                    caturl="https://calendar.google.com/?mode=week"
                elif cat==categories[2]:
                    caturl="{0}/html/weather.html".format(os.getcwd())
                elif cat==categories[3]:
                    caturl="{0}/html/timescreen.html".format(os.getcwd())
                elif cat==categories[4]:
                    caturl="{0}/html/alarm.html".format(os.getcwd())
                else:
                    print "Unrecognized category {0}".format(cat)
                    sys.exit()
                thread.start_new_thread(self.webload,(caturl,))
                self.counter(catduration,caturl,catnum)
            else:
                if status==False:
                    while True:
                        time.sleep(0.1)
                        if f==False:
                            pass
                        else:
                            break
    def start(self):
        thread.start_new_thread( self.counter, (2,"https://calendar.google.com?mode=day",0,) )
        webview.create_window("wall program","html/start.html", fullscreen=True)

