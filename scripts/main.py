__version__ = "0.1.0"

__author__ = "Jonas Kemnitzer"
__email__ = "jonas.kemnitzer.2@hof-university.de"

import qi
import os


class Activity:
    APP_ID = "mini_python3_nao_app"

    def __init__(self, qiapp):
        self.qiapp = qiapp
        self.session = qiapp.session

    def on_start(self):
        answer = ""

        self.say(answer)
        self.stop()

    def stop(self):
        self.qiapp.stop()

    def say(self, answer):
        self.session.service("ALTextToSpeech").say(str(answer))

    def get_recording(self):
        path = os.path.expanduser("~") + "/recordings/microphones/tts.wav"
        return open(path, "rb")


if __name__ == "__main__":
    qiapp = qi.Application()
    qiapp.start()
    activity = Activity(qiapp)
    qi.runAsync(activity.on_start)
    qiapp.run()
