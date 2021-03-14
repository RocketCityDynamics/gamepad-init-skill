from mycroft import MycroftSkill, intent_file_handler
import subprocess


class GamepadInit(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('init.gamepad.intent')
    def handle_init_gamepad(self, message):
        self.speak_dialog('init.gamepad')
        #subprocess.call(["ROS command line command here. Picked up by listener"],shell=True)

#what didn't work
#subprocess.call(["sudo python3 Bluetooth.py"],shell=True) Not this easy. sudo commands are locked out by a certain default. 
#The gamepad .py script can be initialized in the image on startup more easily. 
        
def create_skill():
    return GamepadInit()

