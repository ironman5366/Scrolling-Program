__author__ = 'willb'
import webview
import requests
import os
import sys
import easygui
import scripts.settings as settings
import scripts.screensmain as screensmain
class main():
    def start(self):
        screensmain.main().start()
    def main_ui(self):
        ui_choices=[
            "Start",
            "Settings",
            "Exit"
        ]
        ui_choice=easygui.buttonbox(
            msg="Welcome to the Wall Program, please make a selection",
            title="Wall Program",
            choices=ui_choices)
        return ui_choice
    def __init__(self):
        easygui.msgbox("Welcome to the Wall Program")
        choice=self.main_ui()
        if choice=="Start":
            self.start()
        elif choice=="Settings":
            settings.main().settings_ui()
        elif choice=="Exit":
            sys.exit()
        elif choice==None:
            sys.exit()
        else:
            easygui.msgbox("Unrecognized choice {0}".format(str(choice)))
            sys.exit()
if __name__ == "__main__":
    main()
