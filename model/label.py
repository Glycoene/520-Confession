import tkinter as tk

class Label:
    def __init__(self, target_window, text, font, point, relx, rely):
        self.__label = tk.Label(target_window)
        self.text = text
        self.font = font
        self.point = point
        self.relx = relx
        self.rely = rely

    def init_label(self):
        self.__label.config(text=self.text, font=(self.font, self.point))
        self.__label.place(relx=self.relx, rely=self.rely)