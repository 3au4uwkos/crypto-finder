def change_page(root, show_page):
    for widget in root.winfo_children():
        widget.destroy()
    show_page()
