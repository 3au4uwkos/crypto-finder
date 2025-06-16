from tkinter import ttk


def create_title(parent, **position):
    title = ttk.Frame(parent)
    title.grid(**position)

    label = ttk.Label(
        title,
        text="Программное обеспечение для анализа новых криптовалют перед листингом",
        font=('Helvetica', 20, 'bold'),
        wraplength=720,
        anchor="center",
        justify="center",
    )
    label.grid()

    return title
