import tkinter as tk

root = tk.Tk()
root.geometry('800x600')

Besni = tk.Frame(root, bg='grey43')
header = tk.Frame(root, bg='maroon1')
content = tk.Frame(root, bg='grey43')
footer = tk.Frame(root, bg='grey43')

root.columnconfigure(0, weight=1) # 100%

root.rowconfigure(0, weight=1) # 10%
root.rowconfigure(1, weight=1) # 10%
root.rowconfigure(2, weight=7) # 70%
root.rowconfigure(3, weight=1) # 10%

header.grid(row=0, sticky='news')
content.grid(row=1, sticky='news')
footer.grid(row=2, sticky='news')

root.mainloop()