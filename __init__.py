from mycroft import MycroftSkill, intent_file_handler


class GamepadInit(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('init.gamepad.intent')
    def handle_init_gamepad(self, message):
        self.speak_dialog('init.gamepad')


def create_skill():
    return GamepadInit()

