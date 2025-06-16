def configure_weights(set_position, lst):
    if lst:
        for el in lst:
            set_position(el)


def reset_grid(frame):
    cols_number, rows_number = frame.grid_size()
    for row in range(rows_number):
        frame.rowconfigure(row, weight=0)
    for col in range(cols_number):
        frame.columnconfigure(col, weight=0)


def set_grid(frame, rows=None, cols=None, help_rows=None,
                   rows_weight=None, help_cols=None, cols_weight=None):
    reset_grid(frame)
    configure_weights(lambda el: frame.rowconfigure(el[0], weight=el[1]), rows)
    configure_weights(lambda el: frame.columnconfigure(el[0], weight=el[1]), cols)
    configure_weights(lambda el: frame.rowconfigure(el, weight=rows_weight), help_rows)
    configure_weights(lambda el: frame.columnconfigure(el, weight=cols_weight), help_cols)
