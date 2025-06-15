from data_collection import get_upcoming, get_source
from core import train_model, fill_column


def main():

    print(fill_column(get_upcoming(), train_model(get_source())).head())


if __name__ == "__main__":
    main()