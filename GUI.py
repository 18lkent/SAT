import tkinter as tk #imports tkinter module as tk

########################################################################################################################

root = tk.Tk()
root.title("Encoder/Decoder") # gives title to gui
root.geometry('800x600') # sets the window's size to 800px by 600px
root.resizable(False, False) # disallows window resizing
root.configure(background="#515151") # sets windows background colour as dark grey
bgc = "#515151" # dark grey colour
hdc = "#272727" # darker grey colour
trimc = "#ff40e7" # pink colour
tkvar = tk.StringVar(root)
Colours = ["Default", "Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
tkvar.set('Default')

########################################################################################################################
def settingsb():
    encodetextheadershadow.lower()
    encodetextheader.lower()
    encodetext.lower()
    encodetextheaderlabel.lower()
    encodetextshadow.lower()
    decodetextheadershadow.lower()
    decodetextheader.lower()
    decodetext.lower()
    decodetextheaderlabel.lower()
    decodetextshadow.lower()
    convertb.lower()
    copydb.lower()
    copyeb.lower()
    convertb.lower()
    popupMenu.tkraise()
    popupMenuheader.tkraise()
    popupMenutitle.tkraise()

########################################################################################################################
def generalb():
    encodetextshadow.tkraise()
    decodetextshadow.tkraise()
    encodetextheadershadow.tkraise()
    encodetextheader.tkraise()
    encodetext.tkraise()
    encodetextheaderlabel.tkraise()
    decodetextheadershadow.tkraise()
    decodetextheader.tkraise()
    decodetext.tkraise()
    decodetextheaderlabel.tkraise()
    convertb.tkraise()
    copydb.tkraise()
    copyeb.tkraise()
    convertb.tkraise()
    popupMenu.lower()
    popupMenuheader.lower()
    popupMenutitle.lower()
########################################################################################################################

popupMenu = tk.OptionMenu(root, tkvar, *Colours)
popupMenu.place(relx=0.202, rely=0.105)
popupMenu.configure(bg=bgc)

popupMenuheader = tk.Frame(root, bg=hdc,width=130, height=31,) # makes box for the header above the encoder text box
popupMenuheader.place(relx=0.04, rely=0.1) # places the header relative to the window

popupMenutitle = tk.Label(root, text="Choose a colour")
popupMenutitle.place(relx=0.04, rely=0.105)
popupMenutitle.configure(font=("Futura",15, "italic"),fg="white", bg=hdc)

hider = tk.Frame(root, bg=bgc, width=800, height=600)
hider.place(relx=0,rely=0)

########################################################################################################################

trim = tk.Frame(root, bg=trimc,width=800, height=3,) # defines the size and colour of the pink trim
trim.place(relx=0.0, rely=0.049) # places the trim relative to the window (this is why i disabled window resizing)

header = tk.Frame(root, bg=hdc,width=800,height=29) # sets toolbar size and colour
header.grid(row=0,column=0,rowspan=29) # places toolbar at the top

########################################################################################################################

generalb = tk.Button(root, text="General",highlightbackground='#272727', command=generalb) # creates general button
generalb.place(relx=0.0, rely=0.0, height=24, width=75) # positions the button on the toolbar relative to the window
generalb.config(font=("Futura",15, "italic")) # sets font and text size for general button

settingsb = tk.Button(root, text="Settings",highlightbackground='#272727', command=settingsb) # creates settings button
settingsb.place(relx=0.09, rely=0.0, height=24, width=75) # positions the button on the toolbar relative to the window
settingsb.config(font=("Futura",15, "italic")) # sets font and text size for general button

########################################################################################################################

encodetextheadershadow = tk.Frame(root, bg="black",width=341, height=31,) # makes the the shadow below the encoder header
encodetextheadershadow.place(relx=0.052, rely=0.105) # places the shadow below the header

encodetextheader = tk.Frame(root, bg=hdc,width=341, height=31,) # makes box for the header above the encoder text box
encodetextheader.place(relx=0.05, rely=0.1) # places the header relative to the window

encodetextheaderlabel = tk.Label(root, text="Encode", font=("Futura",15, "italic")) # creates the label above the encoder
encodetextheaderlabel.place(relx=0.212, rely=0.102, height=24, width=75) # positions the label in the header
encodetextheaderlabel.config(bg=hdc,fg="white") # makes the text white and the background of the label the same colour as the header

encodetextshadow = tk.Frame(root, height=387, width=341,bg = "black") # creates the text box
encodetextshadow.place(relx=0.052, rely=0.170) # places the text box on the screen relative to the window colour as the text box

encodetext = tk.Text(root, height=25, width=47,bg = hdc, fg="white", borderwidth=2) # creates the text box
encodetext.place(relx=0.05, rely=0.165) # places the text box on the screen relative to the window
encodetext.config(highlightbackground=hdc) # makes the highlight border the same colour as the text box

########################################################################################################################

decodetextheadershadow = tk.Frame(root, bg="black",width=341, height=31,) # makes the the shadow below the decoder header
decodetextheadershadow.place(relx=0.532, rely=0.105) # places the shadow below the header

decodetextheader = tk.Frame(root, bg=hdc,width=341, height=31,) # makes the box fo the header above the decoder text box
decodetextheader.place(relx=0.53, rely=0.1) # places the header relative to the window

decodetextheaderlabel = tk.Label(root, text="Decode", font=("Futura",15, "italic")) # creates the label above the decoder
decodetextheaderlabel.place(relx=0.687, rely=0.102, height=24, width=75) # positions the label in the header
decodetextheaderlabel.config(bg=hdc,fg="white") # makes the text white and the background of the label the same colour as the header

decodetextshadow = tk.Frame(root, height=387, width=341,bg = "black") # creates the text box
decodetextshadow.place(relx=0.532, rely=0.170) # places the text box on the screen relative to the window colour as the text box

decodetext = tk.Text(root, height=25, width=47,bg = hdc, fg="white", borderwidth=2) # creates the text box
decodetext.place(relx=0.53, rely=0.165) # positions the text box on the screen relative to the window
decodetext.config(highlightbackground=hdc) # makes the highlight border the same colour as the text box

########################################################################################################################

def convert(): # defines function called "convert"
    inputd = decodetext.get("1.0",'end-1c') # gets the input from the decode text box
    inpute = encodetext.get("1.0", 'end-1c') # gets the input from the encode text box
    if inputd != "":
        encodetext.delete("1.0", 'end-1c') #deletes everything in the encodetext box
        inputdc = inputd.replace("F4", "a").replace("A4", "b").replace("A1", "c").replace("E3", "d").replace("B6","e").replace("D1", "f").replace("C4", "g").replace("B5", "h").replace("C2", "i").replace("D3", "j").replace("F3", "k").replace("E6", "l").replace("A2", "m").replace("D5", 'n').replace("B3", "o").replace("A6", "p").replace("D6","q").replace("B1", "r").replace("D2", "s").replace("B4", "t").replace("A5", "u").replace("B2", "v").replace("A3","w").replace("F5", "x").replace("C6", "y").replace("C1", "z").replace("4!"," ").replace("f4", "A").replace("a4", "B").replace("a1", "C").replace("e3", "D").replace("b6","E").replace("d1", "F").replace("c4", "G").replace("b5", "H").replace("c2", "I").replace("d3", "J").replace("f3", "K").replace("e6", "L").replace("a2", "M").replace("d5", 'N').replace("b3", "O").replace("a6", "P").replace("d6","Q").replace("b1", "R").replace("d2", "S").replace("b4", "T").replace("a5", "U").replace("b2", "V").replace("a3","W").replace("f5", "X").replace("c6", "Y").replace("c1", "Z")
        encodetext.insert('end', inputdc) #inserts encoded text in the decode box # replace algorithm ^
    elif inpute != "":
        decodetext.delete("1.0", 'end-1c') #deletes everything in the decodetext box
        inputec = inpute.replace("A", "f4").replace("B", "a4").replace("C", "a1").replace("D", "e3").replace("E", "b6").replace("F","d1").replace("G", "c4").replace("H", "b5").replace("I", "c2").replace("J", "d3").replace("K", "f3").replace("L","e6").replace("M", "a2").replace("N", 'd5').replace("O", "b3").replace("P", "a6").replace("Q", "d6").replace("R","b1").replace("S", "d2").replace("T", "b4").replace("U", "a5").replace("V", "b2").replace("W", "a3").replace("X","f5").replace("Y", "c6").replace("Z", "c1").replace(" ", "4!").replace("a", "F4").replace("b", "A4").replace("c","A1").replace("d", "E3").replace("e", "B6").replace("f", "D1").replace("g", "C4").replace("h", "B5").replace("i","C2").replace("j", "D3").replace("k", "F3").replace("l", "E6").replace("m", "A2").replace("n", 'D5').replace("o","B3").replace("p", "A6").replace("q", "D6").replace("r", "B1").replace("s", "D2").replace("t", "B4").replace("u","A5").replace("v", "B2").replace("w", "A3").replace("x", "F5").replace("y", "C6").replace("z", "C1")
        decodetext.insert('end', inputec) #inserts decoded text in the encode box # replace algorithm ^

########################################################################################################################

convertb = tk.Button(root, text="Convert",highlightbackground=bgc, command = convert) # creates button and assigns convert command
convertb.place(relx=0.4575, rely=0.83, height=24, width=75) # places convert button relative to window
convertb.config(font=("Futura",15, "italic")) # configures button font

########################################################################################################################

def copyd(): # defines copy button for the decoder
    copyd2 = decodetext.get("1.0", 'end-1c') # gets text from the decoder box
    root.clipboard_clear() # clears users clipboard
    root.clipboard_append(str(copyd2)) # adds string from text box to users clipboard
    root.update() # this makes it so that the clipboard remains when the window is closed

copydb = tk.Button(root, text="Copy",highlightbackground=bgc, command=copyd) # creates the copy button and assigns the copyd command
copydb.place(relx=0.867, rely=0.83, height=24, width=75) # establishes proportions and location of the button relative to the window
copydb.config(font=("Futura",15, "italic")) # configures text on the button

########################################################################################################################

def copye(): # defines copy button for the encoder
    copye2 = encodetext.get("1.0", 'end-1c') # gets text from the encoder box
    root.clipboard_clear() # clears use clipboard
    root.clipboard_append(str(copye2)) # adds string from text box to users clipboard
    root.update() # this makes it so that the clipboard remains when the window is closed

copyeb = tk.Button(root, text="Copy",highlightbackground=bgc, command=copye) # creates the copy button and assigns the copye command
copyeb.place(relx=0.0465, rely=0.83, height=24, width=75) # establishes proportions and location of the button relative to the window
copyeb.config(font=("Futura",15, "italic")) # configures text on the button

########################################################################################################################

def close(): # defines close function
    exit(0) # exits code with code 0

########################################################################################################################

closeb = tk.Button(root, text="Close",highlightbackground=bgc, command=close) # creates close button and assigns close command
closeb.place(relx=0.9, rely=0.95, height=24, width=75) # places button and defines size
closeb.config(font=("Futura",15, "italic")) # configures text on the button

########################################################################################################################

root.mainloop() # starts mainloop