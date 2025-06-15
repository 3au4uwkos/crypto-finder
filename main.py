
import os
from ui.main_window import main_window
from config.settings import WINDOW_WIDTH, WINDOW_HEIGHT
from data_collection import get_upcoming, get_source
from core import train_model, fill_column


def main():

    main_window()
    print(fill_column(get_upcoming(), train_model(get_source())).head())


if __name__ == "__main__":
    main()
