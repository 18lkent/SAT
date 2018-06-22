import tkinter as tk

root = tk.Tk()
root.geometry('800x600')
root.configure(background="#515151")
bgc = "#515151"
hdc = "#272727"
trimc = "#ff40e7"

Besni = tk.Frame(root, bg=bgc)

trim = tk.Frame(root, bg=trimc,width=800, height=3)
trim.place(relx=0.0, rely=0.049)

header = tk.Frame(root, bg=hdc,width=800,height=29)
header.grid(row=0,column=0,rowspan=29)

generalb = tk.Button(root, text="General",highlightbackground='#272727')
generalb.place(relx=0.0, rely=0.0, height=24, width=75)

settingsb = tk.Button(root, text="Settings",highlightbackground='#272727')
settingsb.place(relx=0.09, rely=0.0, height=24, width=75)

encodetext = tk.Text(root, height=25, width=47)
encodetext.place(relx=0.05, rely=0.1)

decodetext = tk.Text(root, height=25, width=47)
decodetext.place(relx=0.53, rely=0.1)

root.mainloop()