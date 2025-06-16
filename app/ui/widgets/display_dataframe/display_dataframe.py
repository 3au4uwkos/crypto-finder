from tkinter import ttk
from tkinter.font import Font


def display_dataframe(parent, dataframe, container_width, max_rows=100, row_height=17, **position):
    container = ttk.Frame(parent)
    container.grid(**position)

    tree = ttk.Treeview(container, height=row_height)

    style = ttk.Style()
    style.configure("Centered.Treeview", rowheight=25, anchor='center')
    style.configure("Centered.Treeview.Heading", anchor='center')
    tree.configure(style="Centered.Treeview")

    scrollbar = ttk.Scrollbar(container, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    container.columnconfigure(0, weight=0)
    container.columnconfigure(1, weight=0)
    tree.grid()
    scrollbar.grid(row=0, column=1, sticky='nsew')

    tree["columns"] = list(dataframe.columns)
    tree["show"] = "headings"

    font = Font()
    col_widths = {col: font.measure(col) + 20 for col in dataframe.columns}

    for col in dataframe.columns:
        for val in dataframe[col].head(20):
            val_width = font.measure(str(val)) + 10
            col_widths[col] = max(col_widths[col], val_width)

    tmp_width = sum(val for val in col_widths.values())
    ratio = (container_width - 20) / tmp_width if tmp_width < container_width - 20 else 1
    col_widths = {col: int(width * ratio) for (col, width) in col_widths.items()}
    tmp_width = sum(val for val in col_widths.values())
    col_widths['name'] += container_width - 20 - tmp_width

    for col, width in col_widths.items():
        tree.heading(col, text=col)
        tree.column(col, width=width, anchor='center')

    for _, row in dataframe.head(max_rows).iterrows():
        tree.insert("", "end", values=list(row))
    return tree
