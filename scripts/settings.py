class main():
    def get_setting(self,setting_name):
        settings_file=open('program-files/settings.txt')
        lines=settings_file.readlines()
        for line in lines:
            screen=line.split(":")[0]
            if screen==setting_name:
                return line.split(":")[1]
    def make_setting(self,setting_name,setting_value):
        settings_file=open('program-files/settings.txt')
        settings_file_str=settings_file.read()
        lines=settings_file.readlines()
        for line in lines:
            screen=line.split(":")[0]
            if screen==setting_name:
                settings_file_str=settings_file_str.replace(line,"{0}:{1}\n".format(screen,str(setting_value)))
        settings_file.write(settings_file_str)
        settings_file.close()
    def __init__(self):
        pass

