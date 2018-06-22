import tkinter as tk

root = tk.Tk()
root.title("Encoder/Decoder")
root.geometry('800x600')
root.resizable(False, False)
root.configure(background="#515151")
bgc = "#515151"
hdc = "#272727"
trimc = "#ff40e7"

Besni = tk.Frame(root, bg=bgc)

### y = up and down, x = left and right

trim = tk.Frame(root, bg=trimc,width=800, height=3,)
trim.place(relx=0.0, rely=0.049)

header = tk.Frame(root, bg=hdc,width=800,height=29)
header.grid(row=0,column=0,rowspan=29)

generalb = tk.Button(root, text="General",highlightbackground='#272727')
generalb.place(relx=0.0, rely=0.0, height=24, width=75)
generalb.config(font=("Futura",15, "italic"))

settingsb = tk.Button(root, text="Settings",highlightbackground='#272727')
settingsb.place(relx=0.09, rely=0.0, height=24, width=75)
settingsb.config(font=("Futura",15, "italic"))

encodetextheader = tk.Frame(root, bg=hdc,width=341, height=31,)
encodetextheader.place(relx=0.05, rely=0.1)

encodetextheaderlabel = tk.Label(root, text="Encode", font=("Futura",15, "italic"))
encodetextheaderlabel.place(relx=0.212, rely=0.102, height=24, width=75)
encodetextheaderlabel.config(bg=hdc,fg="white")

encodetext = tk.Text(root, height=25, width=47,bg = hdc, fg="white", borderwidth=2)
encodetext.place(relx=0.05, rely=0.165)
encodetext.config(highlightbackground=hdc)

decodetextheader = tk.Frame(root, bg=hdc,width=341, height=31,)
decodetextheader.place(relx=0.53, rely=0.1)

decodetextheaderlabel = tk.Label(root, text="Decode", font=("Futura",15, "italic"))
decodetextheaderlabel.place(relx=0.687, rely=0.102, height=24, width=75)
decodetextheaderlabel.config(bg=hdc,fg="white")

decodetext = tk.Text(root, height=25, width=47,bg = hdc, fg="white", borderwidth=2)
decodetext.place(relx=0.53, rely=0.165)
decodetext.config(highlightbackground=hdc)

convertb = tk.Button(root, text="Convert",highlightbackground=bgc)
convertb.place(relx=0.4575, rely=0.83, height=24, width=75)
convertb.config(font=("Futura",15, "italic"))

closeb = tk.Button(root, text="Close",highlightbackground=bgc)
closeb.place(relx=0.9, rely=0.95, height=24, width=75)
closeb.config(font=("Futura",15, "italic"))

root.mainloop()