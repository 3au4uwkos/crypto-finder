from tkinter import ttk
from config.settings import WINDOW_WIDTH
from ui.utils.configure_grid import set_grid
from ui.widgets.create_title import create_title
from ui.widgets.create_button import create_button
from ui.widgets.display_dataframe.display_dataframe import display_dataframe
from ui.utils.change_page import change_page


def change_to_start_page(root):
    from ui.pages.start_page import start_page
    change_page(root, lambda: start_page(root))


def dataset_page(root, dataframe, max_rows=100):
    set_grid(
        root,
        rows=((1, 0), (2, 3), (3, 0)),
        cols=((1, 1), (2, 1)),
    )

    create_title(root, row=1, column=1, pady=10)
    create_button(root, lambda: change_to_start_page(root), 'Вернуться на главную', row=1, column=2, pady=10)

    display_dataframe(root, dataframe, WINDOW_WIDTH, max_rows=max_rows, pady=(10, 0), sticky='nsew', row=2, column=1,
                      columnspan=2)

    if len(dataframe) > max_rows:
        label = ttk.Label(root,
                          text=f"Показано {max_rows} из {len(dataframe)} строк",
                          foreground="gray50")
        label.grid(row=3, column=1, columnspan=2, sticky='ew')
