__author__ = 'willb'
import datetime


class logs():  # Action is what to do to the logfile, item on which to do it.
    def gettime(self):
        # I don't need milliseconds in the logfile
        return str(datetime.datetime.now()).split(".")[0]

    def log(self, item):
        # Log the item, catching and recording any errors.
        try:
            logfile.write("{0}: {1}\n".format(self.gettime(), item))
        except Exception as e:
            self.log(self, e)

    def openlogs(self):
        # If the logfile already exists, open it for writing. If it doesn't, create it and restart the logging function.
        global logfile
        try:
            logfile = open("program-files/logs.txt")
            logfile.write("{0}: Opened logs\n".format(self.gettime()))
        except IOError:
            logfile = open("program-files/logs.txt", 'w')
            logfile.write("{0}: Opened and created logs\n".format(self.gettime()))
            logs()

    def closelogs(self):
        logfile.write("{0}: Closed logs\n".format(self.gettime()))
        logfile.close()
