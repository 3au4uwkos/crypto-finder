import os
from config.settings import CSV_PATH


def delete_dataset():
    os.remove(CSV_PATH)
