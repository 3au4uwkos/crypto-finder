from tkinter import ttk


def button_styles():
    style = ttk.Style()
    style.theme_use('clam')
    name = 'Modern.TButton'

    style.configure(
        name,
        font=('Helvetica', 12, 'bold'),
        foreground='black',
        bordercolor='black',
        padding=10,
    )
    style.map(
        name,
        background=[
            ('active', '#45a049'),
            ('!disabled', 'blue')
        ]
    )
    return name


def create_button(parent, callback, text, **position):
    button = ttk.Frame(parent)
    button.grid(**position)

    generate_btn = ttk.Button(
        button,
        style=button_styles(),
        text=text,
        command=callback,
    )
    generate_btn.grid()

    return button
