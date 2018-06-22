import tkinter as tk


root = tk.Tk()
settingsw = tk.Toplevel(root)
settingsw.withdraw()
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

settingsb = tk.Button(root, text="Settings",highlightbackground='#272727',command="Settings")
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

def convert():
    inputd = decodetext.get("1.0",'end-1c')
    inpute = encodetext.get("1.0", 'end-1c')
    if inputd != "":
        encodetext.delete("1.0", 'end-1c')
        inputdc = inputd.replace("F4", "a").replace("A4", "b").replace("A1", "c").replace("E3", "d").replace("B6","e").replace("D1", "f").replace("C4", "g").replace("B5", "h").replace("C2", "i").replace("D3", "j").replace("F3", "k").replace("E6", "l").replace("A2", "m").replace("D5", 'n').replace("B3", "o").replace("A6", "p").replace("D6","q").replace("B1", "r").replace("D2", "s").replace("B4", "t").replace("A5", "u").replace("B2", "v").replace("A3","w").replace("F5", "x").replace("C6", "y").replace("C1", "z").replace("4!"," ").replace("f4", "A").replace("a4", "B").replace("a1", "C").replace("e3", "D").replace("b6","E").replace("d1", "F").replace("c4", "G").replace("b5", "H").replace("c2", "I").replace("d3", "J").replace("f3", "K").replace("e6", "L").replace("a2", "M").replace("d5", 'N').replace("b3", "O").replace("a6", "P").replace("d6","Q").replace("b1", "R").replace("d2", "S").replace("b4", "T").replace("a5", "U").replace("b2", "V").replace("a3","W").replace("f5", "X").replace("c6", "Y").replace("c1", "Z")
        encodetext.insert('end', inputdc)
    elif inpute != "":
        decodetext.delete("1.0", 'end-1c')
        inputec = inpute.replace("A", "f4").replace("B", "a4").replace("C", "a1").replace("D", "e3").replace("E", "b6").replace("F","d1").replace("G", "c4").replace("H", "b5").replace("I", "c2").replace("J", "d3").replace("K", "f3").replace("L","e6").replace("M", "a2").replace("N", 'd5').replace("O", "b3").replace("P", "a6").replace("Q", "d6").replace("R","b1").replace("S", "d2").replace("T", "b4").replace("U", "a5").replace("V", "b2").replace("W", "a3").replace("X","f5").replace("Y", "c6").replace("Z", "c1").replace(" ", "4!").replace("a", "F4").replace("b", "A4").replace("c","A1").replace("d", "E3").replace("e", "B6").replace("f", "D1").replace("g", "C4").replace("h", "B5").replace("i","C2").replace("j", "D3").replace("k", "F3").replace("l", "E6").replace("m", "A2").replace("n", 'D5').replace("o","B3").replace("p", "A6").replace("q", "D6").replace("r", "B1").replace("s", "D2").replace("t", "B4").replace("u","A5").replace("v", "B2").replace("w", "A3").replace("x", "F5").replace("y", "C6").replace("z", "C1")
        decodetext.insert('end', inputec)

convertb = tk.Button(root, text="Convert",highlightbackground=bgc, command = convert)
convertb.place(relx=0.4575, rely=0.83, height=24, width=75)
convertb.config(font=("Futura",15, "italic"))

def close():
    exit(0)

closeb = tk.Button(root, text="Close",highlightbackground=bgc, command=close)
closeb.place(relx=0.9, rely=0.95, height=24, width=75)
closeb.config(font=("Futura",15, "italic"))

root.mainloop()


