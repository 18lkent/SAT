import tkinter as tk #imports tkinter module as tk

########################################################################################################################
# Base Settings and Universal Assets                                                                                   #
########################################################################################################################

root = tk.Tk()
root.title("Encoder/Decoder") # gives title to gui
root.geometry('800x600') # sets the window's size to 800px by 600px
root.resizable(False, False) # disallows window resizing
bgc = "#515151" # default background colour (dark grey)
root.configure(bg=bgc) # sets windows background colour as dark grey
hdc = "#272727" # default header colour (darker grey)
trimc = "#ff40e7" # default trim colour (Pink)
lightbgc = "#CDCDCD"
lighthdc = "#AAAAAA"
Red = "#ff0000" # red
Orange = "#ff7f00" # orange
Yellow = "#ffff00" # yellow
Green = "#00ff00" # green
Blue = "#0000ff" # blue
Indigo = "#4b0082" # indigo
Violet = "#9400d3" # violet
tkvar = tk.StringVar(root) # string variable for the dropdown menu for the colour changer
Colours = ["Default", "Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"] # colours in the dropdown menu
tkvar2 = tk.StringVar(root)
Themes = ["Default", "Light"]
tkvar2.set("Default")
tkvar.set("Default")

########################################################################################################################
# Colour Picker                                                                                                        #
########################################################################################################################

def colourConfirm(new_value): # defines function "colourConfirm" with parameters "new_value"
    if new_value == "Default": # if the value included equals default,
        trim.configure(bg=trimc) # change the trim colour
        selectedWindow.configure(bg=trimc) # and the current window indicator colour to the default,
        f = open("user.cfg", "w")
        f.write("#ff40e7")
        f.close()
    elif new_value == "Red": # if the value included equals red,
        trim.configure(bg=Red) # change the trim colour
        selectedWindow.configure(bg=Red) # and the current window indicator colour to red,
        f = open("user.cfg", "w") # open and
        f.write("#ff0000") # write the selected value to the user.cfg file
        f.close() # then close || the following modules all work the same as the previous
    elif new_value == "Orange":
        trim.configure(bg=Orange)
        selectedWindow.configure(bg=Orange)
        f = open("user.cfg", "w")
        f.write("#ff7f00")
        f.close()
    elif new_value == "Yellow":
        trim.configure(bg=Yellow)
        selectedWindow.configure(bg=Yellow)
        f = open("user.cfg", "w")
        f.write("#ffff00")
        f.close()
    elif new_value == "Green":
        trim.configure(bg=Green)
        selectedWindow.configure(bg=Green)
        f = open("user.cfg", "w")
        f.write("#00ff00")
        f.close()
    elif new_value == "Blue":
        trim.configure(bg=Blue)
        selectedWindow.configure(bg=Blue)
        f = open("user.cfg", "w")
        f.write("#0000ff")
        f.close()
    elif new_value == "Indigo":
        trim.configure(bg=Indigo)
        selectedWindow.configure(bg=Indigo)
        f = open("user.cfg", "w")
        f.write("#9400d3")
        f.close()
    elif new_value == "Violet":
        trim.configure(bg=Violet)
        selectedWindow.configure(bg=Violet)
        f = open("user.cfg", "w")
        f.write("#9400d3")
        f.close()

########################################################################################################################
# Theme Picker                                                                                                         #
########################################################################################################################

def themeconfirm(theme_value):
    if theme_value == "Default":
        header.configure(bg=hdc)
        generalb.configure(highlightbackground=hdc)
        settingsb.configure(highlightbackground=hdc)
        copydb.configure(highlightbackground=bgc)
        copyeb.configure(highlightbackground=bgc)
        root.configure(bg=bgc)
        hider.configure(bg=bgc)
        closeb.configure(highlightbackground=bgc)
        encodetext.configure(bg=hdc, highlightbackground=hdc)
        decodetext.configure(bg=hdc, highlightbackground=hdc)
        encodetextheader.configure(bg=hdc)
        encodetextheaderlabel.configure(bg=hdc, fg="white")
        decodetextheader.configure(bg=hdc)
        decodetextheaderlabel.configure(bg=hdc, fg="white")
        colourdropdownMenuheader.configure(bg=hdc)
        colourdropdownMenu.configure(bg=bgc)
        colourdropdownMenutitle.configure(bg=hdc, fg="white")
        themedropdownMenuheader.configure(bg=hdc)
        themedropdownMenu.configure(bg=bgc)
        themedropdownMenutitle.configure(bg=hdc, fg="white")
        x = open("user.cfg", "r")
        colour = x.read()
        x.close()
        f = open("user.cfg", "w")
        f.write(colour+"\nDark")
        f.close()

    elif theme_value == "Light":
        header.configure(bg=lighthdc)
        generalb.configure(highlightbackground=lighthdc)
        settingsb.configure(highlightbackground=lighthdc)
        copydb.configure(highlightbackground=lightbgc)
        copyeb.configure(highlightbackground=lightbgc)
        root.configure(bg=lightbgc)
        hider.configure(bg=lightbgc)
        closeb.configure(highlightbackground=lightbgc)
        encodetext.configure(bg=lighthdc, highlightbackground=lighthdc)
        decodetext.configure(bg=lighthdc, highlightbackground=lighthdc)
        encodetextheader.configure(bg=lighthdc)
        encodetextheaderlabel.configure(bg=lighthdc, fg="black")
        decodetextheader.configure(bg=lighthdc)
        decodetextheaderlabel.configure(bg=lighthdc, fg="black")
        colourdropdownMenuheader.configure(bg=lighthdc)
        colourdropdownMenu.configure(bg=lightbgc)
        colourdropdownMenutitle.configure(bg=lighthdc, fg="black")
        themedropdownMenuheader.configure(bg=lighthdc)
        themedropdownMenu.configure(bg=lightbgc)
        themedropdownMenutitle.configure(bg=lighthdc, fg="black")
        x = open("user.cfg", "r")
        colour = x.read()
        x.close()
        f = open("user.cfg", "w")
        f.write(colour+"\nLight")
        f.close()

########################################################################################################################
# Settings button commands                                                                                             #
########################################################################################################################

def settingsb(): # this is the command that is triggered when the setting tab button is pressed
    encodetextheadershadow.lower() # Lowers the header above the encode text box's shadow
    encodetextheader.lower() # Lowers the hedaer above the encode text box
    encodetext.lower() # Lowers the encoding text box
    encodetextheaderlabel.lower() # Lowers the text in the header above the encoder text box
    encodetextshadow.lower() # Lowers the shadow behind the encoder text box
    decodetextheadershadow.lower() # Lowers the header above the decode text box's shadow
    decodetextheader.lower() # Lowers the header above the decode text box
    decodetext.lower() # Lowers the decoding text box
    decodetextheaderlabel.lower() # Lowers the text in the header above the decoder text box
    decodetextshadow.lower() # Lowers the shadow behind the decoder text box
    copydb.lower() # Lowers the copy button next to the decode text box
    copyeb.lower() # Lowers the copy button next to the encode text box
    colourdropdownMenu.tkraise() # Raises the dropdown menu
    colourdropdownMenuheadershadow.tkraise() # Raises the dropdown menu header shadow
    colourdropdownMenuheader.tkraise() # Raises the dropdown menu header
    colourdropdownMenutitle.tkraise() # Raises the dropdown menu title
    themedropdownMenu.tkraise()
    themedropdownMenuheadershadow.tkraise()
    themedropdownMenuheader.tkraise()
    themedropdownMenutitle.tkraise()
    selectedWindow.place(relx=0.094, rely=0.04) # positions the current window indicator below the settings window

########################################################################################################################
# General button commands                                                                                              #
########################################################################################################################

def generalb(): # this is the command that is triggered when the general button is triggered
    encodetextshadow.tkraise() # Raises the encode text box shadow
    decodetextshadow.tkraise() # Raises the decode text box shadow
    encodetextheadershadow.tkraise() # Raises the encode text box header shadow
    encodetextheader.tkraise() # Raises the encode text box header
    encodetext.tkraise() # Raises the encode text box
    encodetextheaderlabel.tkraise() # Raises the encode text box header label
    decodetextheadershadow.tkraise() # Raises the decode text box header shadow
    decodetextheader.tkraise() # Raises the decode text box header
    decodetext.tkraise() # Raises the decode text box
    decodetextheaderlabel.tkraise() # Raises the decode text box label
    copydb.tkraise() # Raises the decode text box copy button
    copyeb.tkraise() # Raises the encode text box copy button
    colourdropdownMenu.lower() #  lowers the dropdown menu
    colourdropdownMenuheader.lower() # lowers the dropdown menu header
    colourdropdownMenutitle.lower() # lowers the dropdown menu title
    colourdropdownMenuheadershadow.lower() # lowers the dropdown menu header shadow
    themedropdownMenu.lower()
    themedropdownMenuheadershadow.lower()
    themedropdownMenuheader.lower()
    themedropdownMenutitle.lower()
    selectedWindow.place(relx=0.004, rely=0.04) # positions the current window indicator below the general window

########################################################################################################################
# Settings Page                                                                                                        #
########################################################################################################################

colourdropdownMenu = tk.OptionMenu(root, tkvar, *Colours, command=colourConfirm) # makes the dropdown menu
colourdropdownMenu.place(relx=0.202, rely=0.105) # places the dropdown menu relative to the window
colourdropdownMenu.configure(bg=bgc) # makes the background colour of the dropdown menu the same as the pages background

colourdropdownMenuheader = tk.Frame(root, bg=hdc,width=130, height=31,) # makes box for the header above the drop down menu
colourdropdownMenuheader.place(relx=0.04, rely=0.1) # places the header relative to the window

colourdropdownMenuheadershadow = tk.Frame(root, bg="black",width=130, height=31,) # makes shadow under the header above the drop down menu
colourdropdownMenuheadershadow.place(relx=0.042, rely=0.105) # places the shadow relative to the window

colourdropdownMenutitle = tk.Label(root, text="Choose a colour") # creates the label for the colour picker
colourdropdownMenutitle.place(relx=0.04, rely=0.105) # places the label for the colour picker on the header
colourdropdownMenutitle.configure(font=("Futura",15, "italic"),fg="white", bg=hdc) # changes the font, font colour and background colour of the label

themedropdownMenu = tk.OptionMenu(root, tkvar2, *Themes, command=themeconfirm) # makes the dropdown menu
themedropdownMenu.place(relx=0.202, rely=0.205) # places the dropdown menu relative to the window
themedropdownMenu.configure(bg=bgc) # makes the background colour of the dropdown menu the same as the pages background

themedropdownMenuheader = tk.Frame(root, bg=hdc,width=130, height=31,) # makes box for the header above the drop down menu
themedropdownMenuheader.place(relx=0.04, rely=0.2) # places the header relative to the window

themedropdownMenuheadershadow = tk.Frame(root, bg="black",width=130, height=31,) # makes shadow under the header above the drop down menu
themedropdownMenuheadershadow.place(relx=0.042, rely=0.205) # places the shadow relative to the window

themedropdownMenutitle = tk.Label(root, text="Choose a theme") # creates the label for the colour picker
themedropdownMenutitle.place(relx=0.04, rely=0.205) # places the label for the colour picker on the header
themedropdownMenutitle.configure(font=("Futura",15, "italic"),fg="white", bg=hdc) # changes the font, font colour and background colour of the label

hider = tk.Frame(root, bg=bgc, width=800, height=600) # a frame for hiding the contents of the page which the user is not on
hider.place(relx=0,rely=0) # places the hider

########################################################################################################################
# Header                                                                                                               #
########################################################################################################################

trim = tk.Frame(root, bg=trimc,width=800, height=3,) # defines the size and colour of the pink trim
trim.place(relx=0.0, rely=0.049) # places the trim relative to the window (this is why i disabled window resizing)

header = tk.Frame(root, bg=hdc,width=800,height=29) # sets toolbar size and colour
header.grid(row=0,column=0,rowspan=29) # places toolbar at the top

selectedWindow = tk.Frame(root, bg=trimc, width=69, height=2) # creates the selected window indicator
selectedWindow.place(relx=0.004, rely=0.04) # places the selected window indicator

########################################################################################################################
# Header Buttons                                                                                                       #
########################################################################################################################

generalb = tk.Button(root, text="General",highlightbackground=hdc, command=generalb) # creates general button
generalb.place(relx=0.0, rely=0.0, height=24, width=75) # positions the button on the toolbar relative to the window
generalb.config(font=("Futura",15, "italic")) # sets font and text size for general button

settingsb = tk.Button(root, text="Settings",highlightbackground=hdc, command=settingsb) # creates settings button
settingsb.place(relx=0.09, rely=0.0, height=24, width=75) # positions the button on the toolbar relative to the window
settingsb.config(font=("Futura",15, "italic")) # sets font and text size for general button

########################################################################################################################
# Encode text box                                                                                                      #
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
# Decode text box                                                                                                      #
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
# Conversion Function                                                                                                  #
########################################################################################################################
def encodethetext( event ):
    inpute = encodetext.get("1.0", 'end-1c') # gets the input from the encode text box
    decodetext.delete("1.0", 'end-1c') #deletes everything in the decodetext box
    inputec = inpute.replace("A", "f4").replace("B", "a4").replace("C", "a1").replace("D", "e3").replace("E", "b6").replace("F","d1").replace("G", "c4").replace("H", "b5").replace("I", "c2").replace("J", "d3").replace("K", "f3").replace("L","e6").replace("M", "a2").replace("N", 'd5').replace("O", "b3").replace("P", "a6").replace("Q", "d6").replace("R","b1").replace("S", "d2").replace("T", "b4").replace("U", "a5").replace("V", "b2").replace("W", "a3").replace("X","f5").replace("Y", "c6").replace("Z", "c1").replace(" ", "4!").replace("a", "F4").replace("b", "A4").replace("c","A1").replace("d", "E3").replace("e", "B6").replace("f", "D1").replace("g", "C4").replace("h", "B5").replace("i","C2").replace("j", "D3").replace("k", "F3").replace("l", "E6").replace("m", "A2").replace("n", 'D5').replace("o","B3").replace("p", "A6").replace("q", "D6").replace("r", "B1").replace("s", "D2").replace("t", "B4").replace("u","A5").replace("v", "B2").replace("w", "A3").replace("x", "F5").replace("y", "C6").replace("z", "C1")
    decodetext.insert('end', inputec) #inserts decoded text in the encode box # replace algorithm ^

def decodethetext( event ):
    inputd = decodetext.get("1.0",'end-1c') # gets the input from the decode text box
    encodetext.delete("1.0", 'end-1c') #deletes everything in the encodetext box
    inputdc = inputd.replace("F4", "a").replace("A4", "b").replace("A1", "c").replace("E3", "d").replace("B6","e").replace("D1", "f").replace("C4", "g").replace("B5", "h").replace("C2", "i").replace("D3", "j").replace("F3", "k").replace("E6", "l").replace("A2", "m").replace("D5", 'n').replace("B3", "o").replace("A6", "p").replace("D6","q").replace("B1", "r").replace("D2", "s").replace("B4", "t").replace("A5", "u").replace("B2", "v").replace("A3","w").replace("F5", "x").replace("C6", "y").replace("C1", "z").replace("4!"," ").replace("f4", "A").replace("a4", "B").replace("a1", "C").replace("e3", "D").replace("b6","E").replace("d1", "F").replace("c4", "G").replace("b5", "H").replace("c2", "I").replace("d3", "J").replace("f3", "K").replace("e6", "L").replace("a2", "M").replace("d5", 'N').replace("b3", "O").replace("a6", "P").replace("d6","Q").replace("b1", "R").replace("d2", "S").replace("b4", "T").replace("a5", "U").replace("b2", "V").replace("a3","W").replace("f5", "X").replace("c6", "Y").replace("c1", "Z")
    encodetext.insert('end', inputdc) #inserts encoded text in the decode box # replace algorithm ^

decodetext.bind("<KeyRelease>", decodethetext) # binds the users key releases to the decodethetext command which performs the algorythm
encodetext.bind("<KeyRelease>", encodethetext) # binds the users key releases to the encodethetext command. this makes the decode and encoding process realtime (converted as you type it)
########################################################################################################################
# Copy decode function and button                                                                                        #
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
# Copy encode function and button                                                                                      #
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
# Close button function                                                                                                #
########################################################################################################################

def close(): # defines close function
    exit(0) # exits code with code 0

########################################################################################################################
# Close Button                                                                                                         #
########################################################################################################################

closeb = tk.Button(root, text="Close",highlightbackground=bgc, command=close) # creates close button and assigns close command
closeb.place(relx=0.9, rely=0.95, height=24, width=75) # places button and defines size
closeb.config(font=("Futura",15, "italic")) # configures text on the button

########################################################################################################################
# User Config file                                                                                                     #
########################################################################################################################

with open('user.cfg', 'r') as f:
    cfg = [line.strip() for line in f]
colour = cfg[0]
theme = cfg[1]
if colour != "" and colour != "Default": # if x isnt nothing and it also isnt "default",
    trim.configure(bg=colour) # change the colour of the trim and
    selectedWindow.configure(bg=colour) # the colour of the selected window indicator to what is in the config file
    themeconfirm(theme)
else: # if x is nothing (config file empty) or "default"
    trim.configure(bg=trimc) # set the colour of the trim,
    selectedWindow.configure(bg=trimc) # and the selected window colour to the default (trimc)
    themeconfirm(theme)

########################################################################################################################
# Main loop                                                                                                            #
########################################################################################################################


root.mainloop() # starts mainloop