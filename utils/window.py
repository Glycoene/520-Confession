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
    random_x = random.random()
    random_y = random.random()

    global DENY_FONT
    DENY_FONT -= 3
    DENY_BUTTON.config(font=('黑体', DENY_FONT))
    DENY_BUTTON.place(relx=random_x, rely=random_y)

    global ACCEPT_FONT
    ACCEPT_FONT += 3
    ACCEPT_BUTTON.config(font=('黑体', ACCEPT_FONT))

def accept():
    messagebox.showinfo(message=f'{CONFIG.get('Text', 'answer')}')
    WINDOW.destroy()

def close():
    messagebox.showerror(message=f'{CONFIG.get('Text', 'closeError')}')

def check_minimize():
    if WINDOW.state() == 'iconic':
        WINDOW.deiconify()
        WINDOW.lift()
        WINDOW.focus_force()
        messagebox.showwarning(message=f'{CONFIG.get('Text', 'minimizeWaring')}')
    WINDOW.after(500, check_minimize)

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

    WINDOW.protocol('WM_DELETE_WINDOW', close)
    check_minimize()