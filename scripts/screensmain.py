__author__ = 'willb'
import scripts.settings as settings
from multiprocessing import Pool
import webview
import time
def callback():
    print "Callback"
    webview.load_url("google.com")
class main():
    def counter(self, duration):
        num=0
        print duration
        duration=float(duration)
        while True:
            time.sleep(0.1)
            num+=(0.1)
            print num
            if duration == num or num > duration:
                break
                return "finished"
            else:
                f=open("program-files/status.txt").read()
                if 'pause' in f:
                    f.close()
                    while True:
                        time.sleep(0.1)
                        f=open("status.txt").read()
                        if "pause" in f:
                            pass
                        else:
                            break
                        f.close()


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
        print 'In dayview'
        print "Starting webview"
        self.viewer("https://calendar.google.com/?mode=day")
        pool = Pool(processes=1)              # Start a worker processes.
        result = pool.apply_async(self.counter,duration, callback) # Evaluate "f(10)" asynchronously calling callback when finished.
    def weekview(self, duration):
        pool = Pool(processes=1)              # Start a worker processes.
        result = pool.apply_async(self.viewer, ["https://calendar.google.com/?mode=week"], callback) # Evaluate "f(10)" asynchronously calling callback when finished.
        countvar=self.counter(duration)
    def weather(self, duration):
        pool = Pool(processes=1)              # Start a worker processes.
        result = pool.apply_async(self.viewer, ["html/weather.html"], callback) # Evaluate "f(10)" asynchronously calling callback when finished.
        countvar=self.counter(duration)
    def timescreen(self, duration):
        pool = Pool(processes=1)              # Start a worker processes.
        result = pool.apply_async(self.viewer, ["html/timescreen.html"], callback) # Evaluate "f(10)" asynchronously calling callback when finished.
        countvar=self.counter(duration)
    def alarm(self, duration):
        pool = Pool(processes=1)              # Start a worker processes.
        result = pool.apply_async(self.viewer, ["html/alarm.html"], callback) # Evaluate "f(10)" asynchronously calling callback when finished.
        countvar=self.counter(duration)
    def start(self):
        def get_duration(screen_name):
            screen_duration = int(settings.main().get_setting(screen_name))
            return screen_duration
        self.dayview(get_duration("dayview"))
        self.weekview(get_duration("weekview"))
        self.weather(get_duration("weather"))
        self.timescreen(get_duration("timescreen"))
        self.alarm(get_duration("alarm"))
        self.start()

