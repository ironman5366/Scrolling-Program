__author__ = 'willb'
import scripts.settings as settings
from multiprocessing import Pool
import webview
import time
import thread
status=True
class main():
    def pausebox():
        pb=easygui.buttonbox(title="Wall Program", msg="", choices="Play/Pause")
        if status==False:
            status=True
        elif status==True:
            status=False
    def counter(self, duration):
        num=0
        print duration
        duration=float(duration)
        while True:
            time.sleep(0.1)
            num+=(0.1)
            print num
            if duration == num or num > duration:
                return "finished"
            else:
                if status==False:
                    while True:
                        time.sleep(0.1)
                        if f==False:
                            pass
                        else:
                            break

    def viewer(self,url):
        print "In viewer"
        try:
            print "Creating window"
            webview.create_window("Wall Program",url)
        except Exception as e:
            print e
            print "Loading url"
            webview.load_url(url)
    def dayview(self, duration):
        thread.start_new_thread ( self.viewer, ("https://calendar.google.com/?mode=day",))
        self.counter(duration)
    def weekview(self, duration): 
        thread.start_new_thread ( self.viewer, ("https://calendar.google.com/?mode=week",))
        self.counter(duration)
    def weather(self, duration):
        thread.start_new_thread ( self.viewer, ("html/weather.html",))
        self.counter(duration)
    def timescreen(self, duration):
        thread.start_new_thread ( self.viewer, ("html/timescreen.html",))
        self.counter(duration)
    def alarm(self, duration):
        thread.start_new_thread ( self.viewer, ("html/alarm.html",))
        self.counter(duration)
    def start(self):
        def get_duration(screen_name):
            screen_duration = int(settings.main().get_setting(screen_name))
            return screen_duration
        thread.start_new_thread ( self.pausebox, () )
        self.dayview(get_duration("dayview"))
        self.weekview(get_duration("weekview"))
        self.weather(get_duration("weather"))
        self.timescreen(get_duration("timescreen"))
        self.alarm(get_duration("alarm"))
        self.start()

