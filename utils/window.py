import tkinter as tk
from pathlib import Path
from utils.config import CONFIG

WINDOW = tk.Tk()

def init_window():
    global WINDOW
    WINDOW.iconbitmap(Path(__file__).parent.parent / 'icon.ico')
    WINDOW.title(CONFIG.get('Window', 'title'))
    screen_width, screen_height = WINDOW.maxsize()
    if CONFIG.getboolean('Window', 'isCustomize'):
        WINDOW.geometry(f'{int(CONFIG.get('Window', 'width'))}x{int(CONFIG.get('Window', 'height'))}+{int(screen_width/2 - CONFIG.getint('Window', 'width')/2)}+{int(screen_height - CONFIG.getint('Window', 'height')/2)}')
    else:
        WINDOW.geometry(f'{int(screen_width/2)}x{int(screen_height/2)}+{int(screen_width/2 - screen_width/4)}+{int(screen_height/2 - screen_height/4)}')
    WINDOW.resizable(False, False)
    WINDOW.attributes('-topmost', True)