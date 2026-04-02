import tkinter as tk

class Clock:
    def __init__(self, root):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0

        self.label = tk.Label(root, font= ("Ariel", 48), bg = "black", fg = "cyan")
        self.label.pack(padx=20, pady=20)

        self.update_clock()

    def update_clock(self):
        self.seconds += 1

        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1

        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1

        if self.hours == 24:
            self.hours = 0

        time_string = f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
        self.label.config(text=time_string)
        self.label.after(1000, self.update_clock)

root = tk.Tk()
root.title("My Python Clock")
root.configure(bg="black")
my_clock = Clock(root)
root.mainloop()