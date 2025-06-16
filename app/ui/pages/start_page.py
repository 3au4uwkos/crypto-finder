from app.ui.utils.configure_grid import set_grid
from app.ui.widgets.create_title import create_title
from app.ui.widgets.create_button import create_button
from app.ui.utils.change_page import change_page


def change_to_dataset_page(root):
    from app.ui.pages.dataset_page import dataset_page
    from app.data_collection import get_upcoming, get_source
    from app.core import train_model, fill_column

    dataframe = fill_column(get_upcoming(rows=100, pages=2), train_model(get_source(pages=2)))
    dataframe.drop_duplicates(inplace=True)
    dataframe = dataframe.sort_values('roi', ascending=False)
    change_page(root, lambda: dataset_page(root, dataframe))


def start_page(root):
    set_grid(
        root,
        rows=((1, 1), (2, 1), (3, 1)),
        cols=((1, 1),),
        help_rows=(0, 4),
        rows_weight=10,
    )

    create_title(root, row=1, column=1)
    create_button(root, lambda: change_to_dataset_page(root), 'Сгенерировать', row=2, column=1)
