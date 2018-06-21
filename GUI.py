import tkinter as tk

root = tk.Tk()
root.geometry('800x600')
root.configure(background="#515151")
bgc = "#515151"
hdc = "#272727"
trimc = "#ff40e7"


size = tk.Frame(root)
Besni = tk.Frame(root, bg=bgc)
header = tk.Frame(root, bg=hdc,width=800,height=29)

header.grid(row=0,column=0)#,columnspan=29)

general = tk.Button(root, text="General",highlightbackground='#272727')
general.grid(row=0,column=0)

trim = tk.Frame(root, bg=trimc,width=800, height=3)
trim.grid(row=0,column=0)

#settings = tk.Button(root, text="settings",highlightbackground='#272727')
#settings.grid(row=0,column=1)


root.mainloop()