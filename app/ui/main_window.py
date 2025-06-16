import tkinter as tk
from app.config.settings import WINDOW_WIDTH, WINDOW_HEIGHT
from app.ui.pages.start_page import start_page


def main_window():
    root = tk.Tk()
    root.title('Crypto analyzer')
    root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
    root.resizable(False, False)
    root.configure(background='#dcdad5')

    start_page(root)

    root.mainloop()
