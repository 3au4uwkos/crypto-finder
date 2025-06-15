# TODO Прописать вызов функции формирования главного окна, которая каскадно будет
#  вызывать функции из других пакетов
import os
from ui.main_window import main_window
from config.settings import WINDOW_WIDTH, WINDOW_HEIGHT


def main():
    main_window()


if __name__ == '__main__':
    main()
