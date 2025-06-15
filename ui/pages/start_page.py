from ui.utils.configure_grid import set_grid
from ui.widgets.create_title import create_title
from ui.widgets.create_button import create_button
from ui.utils.change_page import change_page


def change_to_dataset_page(root):
    from ui.pages.dataset_page import dataset_page
    change_page(root, lambda: dataset_page(root))


def start_page(root):
    set_grid(
        root,
        rows=((1, 1), (2, 1)),
        cols=((1, 1),),
        help_rows=(0, 3),
        rows_weight=10,
    )

    create_title(root, row=1, column=1)
    create_button(root, lambda: change_to_dataset_page(root), 'Сгенерировать', row=2, column=1)
