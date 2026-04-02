import tkinter

class Clock:
    def __init__(self):
        if self.seconds == 60:
            self.seconds = 0
            self.minutes = 1

        if self.hours == 24:
            self.hours = 0
            self.minutes = 1