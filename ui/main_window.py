# TODO Прописать создание окна приложения плюс выгрузка виджетов в данное окно
import tkinter as tk
from config.settings import WINDOW_WIDTH, WINDOW_HEIGHT
from ui.pages.start_page import start_page


def main_window():
    root = tk.Tk()
    root.title('Crypto analyzer')
    root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
    root.resizable(False, False)
    root.configure(background='#dcdad5')

    start_page(root)

    root.mainloop()
