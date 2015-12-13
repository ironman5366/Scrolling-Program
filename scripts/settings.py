import sys
import easygui
class main():
    def get_setting(self,setting_name):
        settings_file=open('program-files/settings.txt')
        lines=settings_file.readlines()
        for line in lines:
            screen=line.split(":")[0]
            if screen==setting_name:
                return line.split(":")[1]
    def make_setting(self,setting_name,setting_value):
        print "In make_setting"
        settings_file=open('program-files/settings.txt')
        print "Settings file opened"
        settings_file_str=settings_file.read()
        print settings_file_str
        lines=settings_file_str.split('\n')
        print "Lines read"
        print lines
        for line in lines:
            print "In iteration"
            screen=line.split(":")[0]
            print screen
            print setting_name
            if screen==setting_name:
                settings_file_str=settings_file_str.replace(line,"{0}:{1}".format(screen,str(setting_value)))
                print settings_file_str
                settings_file.close()
        settings_file_new=open("program-files/settings.txt",'w')
        settings_file_new.write(settings_file_str)
        settings_file.close()
    def settings_ui(self):
        settingschoices=[
            "Day view duration",
            "Week view duration",
            "Weather Duration",
            "Time & Date duration",
            "Change Last line of time screen"
        ]
        sc=easygui.choicebox(msg="Please make a selection", title="Wall Program", choices=settingschoices)
        if sc==settingschoices[0]:
            scn="dayview"
        elif sc==settingschoices[1]:
            scn="weekview"
        elif sc==settingschoices[2]:
            scn="weather"
        elif sc==settingschoices[3]:
            scn="timescreen"
        elif sc==settingschoices[4]:
            newline=easygui.enterbox("What should it say?")
            tf=open('html/timescreen.html')
            f=tf.read()
            current=f.split('id="lastline">')[1].split("<")[0]
            newf=f.replace(current,newline)
            tf.close()
            finalfile=open('html/timescreen.html','w')
            finalfile.write(newf)
            finalfile.close()
            sys.exit()
        elif sc==None:
            sys.exit()

        else:
            print "Unrecognized choice {0}".format(sc)
            sys.exit()
        svaluecurrent=self.get_setting(scn)
        if easygui.ynbox("Current duration for {0} is {1}. Would you like to change it?".format(sc,svaluecurrent)):
            def get_new_val():
                try:
                    newsval=easygui.enterbox("What should the duration be (in seconds)?")
                    newsval=int(newsval)
                    self.make_setting(scn,newsval)
                    easygui.msgbox("Done")
                except TypeError:
                    easygui.msgbox("Must be a valid integer")
                    get_new_val()
            get_new_val()
        else:
            sys.exit()
    def __init__(self):
        pass

