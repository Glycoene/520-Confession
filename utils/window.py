import random
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
from utils.config import CONFIG

WINDOW = tk.Tk()
DENY_FONT = 25
ACCEPT_FONT = 25
DENY_BUTTON = tk.Button(WINDOW, font=('黑体', DENY_FONT))
ACCEPT_BUTTON = tk.Button(WINDOW, font=('黑体', ACCEPT_FONT))


def deny():
    window_width = WINDOW.winfo_width()
    window_height = WINDOW.winfo_height()

    deny_button_width = DENY_BUTTON.winfo_width()
    deny_button_height = DENY_BUTTON.winfo_height()

    accept_button_width = ACCEPT_BUTTON.winfo_width()
    accept_button_height = ACCEPT_BUTTON.winfo_height()

    random_x = random.randint(0, (window_width - deny_button_width))
    random_y = random.randint(0, (window_height - deny_button_height))

    global DENY_FONT
    DENY_FONT -= 1
    DENY_BUTTON.config(font=('黑体', DENY_FONT))
    DENY_BUTTON.place(x=random_x, y=random_y, width=deny_button_width - 5, height=deny_button_height - 5)

    global ACCEPT_FONT
    ACCEPT_FONT += 1
    ACCEPT_BUTTON.config(font=('黑体', ACCEPT_FONT))
    ACCEPT_BUTTON.place(width=accept_button_width + 5, height=accept_button_height + 5)

def accept():
    messagebox.showinfo(message=f'{CONFIG.get('Text', 'answer')}')
    WINDOW.destroy()

def init_window():
    WINDOW.iconbitmap(Path(__file__).parent.parent / 'icon.ico')

    WINDOW.title(CONFIG.get('Window', 'title'))

    screen_width, screen_height = WINDOW.maxsize()
    width = CONFIG.getint('Window', 'width')
    height = CONFIG.getint('Window', 'height')
    if CONFIG.getboolean('Window', 'isCustomize'):
        WINDOW.geometry(f'{int(width)}x{int(height)}+{(screen_width - width) // 2}+{(screen_height - height) // 2}')
    else:
        WINDOW.geometry(f'{screen_width // 2}x{screen_height // 2}+{screen_width // 4}+{screen_height // 4}')

    WINDOW.resizable(False, False)

    WINDOW.attributes('-topmost', True)

    tk.Label(WINDOW, text=CONFIG.get('Text', 'mainQuestion'), font=('黑体', 30)).place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    DENY_BUTTON.config(command=deny, text=CONFIG.get('Text', 'denyButton'))
    DENY_BUTTON.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
    ACCEPT_BUTTON.config(command=accept, text=CONFIG.get('Text', 'acceptButton'))
    ACCEPT_BUTTON.place(relx=0.7, rely=0.5, anchor=tk.CENTER)