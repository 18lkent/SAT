### Software created by Lachlan Kent ###
   ### Begin date: fri 15/jun/2018 ###
### Completion date: tue 21/aug/2018 ###

import tkinter as tk #imports tkinter module as tk
from tkinter import filedialog

########################################################################################################################
# Base Settings and Universal Assets                                                                                   #
########################################################################################################################

def main():
    root = tk.Tk()
    root.title("Encoder/Decoder") # gives title to gui
    w = 800  # width for the Tk root
    h = 600
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (800, 600, x, y))
    root.resizable(False, False) # disallows window resizing
    bgc = "#515151" # default background colour (dark grey)
    root.configure(bg=bgc) # sets windows background colour as dark grey
    hdc = "#272727" # default header colour (darker grey)
    trimc = "#ff40e7" # default trim colour (Pink)
    lightbgc = "#CDCDCD" # light grey background colour (for light theme)
    lighthdc = "#AAAAAA" # light grey hearder colour (for light theme)
    Default = "#ff40e7" # default pink colour
    Red = "#ff0000" # red
    Orange = "#ff7f00" # orange
    Yellow = "#ffff00" # yellow
    Green = "#00ff00" # green
    Blue = "#0000ff" # blue
    Indigo = "#4b0082" # indigo
    Violet = "#9400d3" # violet
    Defaultf = "Futura" # default font
    Helvetica = "Helvetica" # fonts
    Trajan = "Trajan"
    Garamond = "Garamond"
    Bodoni = "Bodoni"
    Comic_Sans = "Comic Sans MS"
    Verdana = "Verdana"
    tkvar = tk.StringVar(root) # string variable for the dropdown menu for the colour changer
    Colours = ["Default", "Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Custom"] # colours in the dropdown menu
    tkvar2 = tk.StringVar(root) # string variable for the dropdown menu of the themes
    Themes = ["Dark", "Light"] # list of themes
    tkvar3 = tk.StringVar(root) # string var for the dropdown menu of the fonts
    Fonts = ["Futura", "Helvetica", "Trajan", "Garamond", "Bodoni", "Comic Sans", "Verdana"]
    tkvar3.set("Futura") # setting the default Font
    tkvar2.set("Dark") # setting the default theme
    tkvar.set("Default") # setting the default colour

########################################################################################################################
# Default Set                                                                                                        #
########################################################################################################################

    def default_all_set():
        f = open("user.cfg", "w") # opens "user.cfg" file
        f.write("Default\nDark\nFutura\nDefaultkey") # rewrites everything in the config file to the default

    def default_colour_set():
        with open('user.cfg', 'r') as f: # opens the "user.cfg" file as f
            cfg = [line.strip() for line in f] # strip "" for each line in f
        theme = cfg[1] # theme = second line in user.cfg file
        font = cfg[2] # font = third line in user.cfg file
        key = cfg[3]
        f.close() # close file
        x = open("user.cfg", "w") # open user.cfg
        x.write("Default\n"+theme+"\n"+font+"\n"+key) # write new default colour in user.cfg
        x.close() # close user.cfg

    def default_theme_set():
        with open('user.cfg', 'r') as f: # opens the "user.cfg" file as f
            cfg = [line.strip() for line in f] # strip "" for each line in f
        colour = cfg[0] # colour = first line in user.cfg file
        font = cfg[2] # font = third line in user.cfg file
        key = cfg[3]
        f.close() # close user.cfg
        x = open("user.cfg", "w") # open user.cfg
        x.write(colour+"\nDark\n"+font+"\n"+key) # writes default theme
        x.close() # closes user.cfg

    def default_font_set():
        with open('user.cfg', 'r') as f: # opes the user.cfg file as f
            cfg = [line.strip() for line in f] # strip "" for each line in f
        theme = cfg[1] # theme = second line in user.cfg
        colour = cfg[0] # colour = first colour in user.cfg
        key = cfg[3]
        f.close() # close user.cfg
        x = open("user.cfg", "w") # opens user.cfg
        x.write(colour+"\n"+theme+"\nFutura"+"\n"+key) # writes default font
        x.close() # closes user.cfg

    def default_key_set():
        with open('user.cfg', 'r') as f: # opes the user.cfg file as f
            cfg = [line.strip() for line in f] # strip "" for each line in f
        theme = cfg[1] # theme = second line in user.cfg
        colour = cfg[0] # colour = first colour in user.cfg
        font = cfg[2]
        f.close() # close user.cfg
        x = open("user.cfg", "w") # opens user.cfg
        x.write(colour+"\n"+theme+"\n"+font+"Default") # writes default font
        x.close() # closes user.cfg

########################################################################################################################
# Config Saver                                                                                                         #
########################################################################################################################

    def theme_saver(colour):
        with open('user.cfg', 'r') as f: #opens user.cfg as "f"
            cfg = [line.strip() for line in f] # strip "" for each line in f
        theme = cfg[1] # designates the second line of the file as 'theme'
        font = cfg[2] # designates the third line of the file as 'font'
        key = cfg[3] # designates the forth line of the file as 'key'
        f.close()
        x = open("user.cfg", "w")
        x.write(colour+"\n"+theme+"\n"+font+"\n"+key) # writes the strings into the file
        x.close()


    def colour_saver(font):
        with open('user.cfg', 'r') as f:
            cfg = [line.strip() for line in f]
        colour = cfg[0]
        theme = cfg[1]
        key = cfg[3]
        f.close()
        x = open("user.cfg", "w")
        x.write(colour+"\n"+theme+"\n"+font+"\n"+key)
        x.close()

    def font_saver(theme):
        with open('user.cfg', 'r') as f:
            cfg = [line.strip() for line in f]
        colour = cfg[0]
        font = cfg[2]
        key = cfg[3]
        f.close()
        x = open("user.cfg", "w")
        x.write(colour+"\n"+theme+"\n"+font+"\n"+key)
        x.close()

    def key_saver(key):
        if " " not in key: # checks if there are spaces in the key
            if "_" not in key: # checks if there are underscores in the key
                encodetext.delete("1.0", 'end-1c') # deletes what is in the encode text box
                decodetext.delete("1.0", 'end-1c') # deletes what is in the encode text box
                with open('user.cfg', 'r') as f:
                    cfg = [line.strip() for line in f]
                colour = cfg[0]
                theme = cfg[1]
                font = cfg[2]
                f.close()
                x = open("user.cfg", "w")
                x.write(colour+"\n"+theme+"\n"+font+"\n"+key)
                x.close()


########################################################################################################################
# Colour Picker                                                                                                        #
########################################################################################################################

    def key_confirm():
        key = keytext.get("1.0", 'end-1c') # gets key from key text box
        if " " not in key: # if space isnt in the key
            if "_" not in key: # if underscore isnt in key (Both for crash fix)
                encodetext.delete("1.0", 'end-1c') # delete everything in the text boxes
                decodetext.delete("1.0", 'end-1c')
                with open('user.cfg', 'r') as f:
                    cfg = [line.strip() for line in f]
                colour = cfg[0]
                theme = cfg[1]
                font = cfg[2]
                f.close()
                x = open("user.cfg", "w")
                x.write(colour+"\n"+theme+"\n"+font+"\n"+key) # writes new key in cfg file
                x.close()

########################################################################################################################
# Key confirm                                                                                                          #
########################################################################################################################

    def colour_confirm(new_value): # defines function "colourConfirm" with parameters "new_value"
        if new_value == "Default": # if the value included equals default,
            trim.configure(bg=trimc) # change the trim colour
            selectedWindow.configure(bg=trimc) # and the current window indicator colour to the default,
            theme_saver("Default")
            customcolourtext.lower()
        elif new_value == "Red": # if the value included equals red,
            trim.configure(bg=Red) # change the trim colour
            selectedWindow.configure(bg=Red) # and the current window indicator colour to red,
            theme_saver("Red") # write the selected value to the user.cfg file
            customcolourtext.lower()
        elif new_value == "Orange":
            trim.configure(bg=Orange)
            selectedWindow.configure(bg=Orange)
            theme_saver("Orange")
            customcolourtext.lower()
        elif new_value == "Yellow":
            trim.configure(bg=Yellow)
            selectedWindow.configure(bg=Yellow)
            theme_saver("Yellow")
            customcolourtext.lower()
        elif new_value == "Green":
            trim.configure(bg=Green)
            selectedWindow.configure(bg=Green)
            theme_saver("Green")
            customcolourtext.lower()
        elif new_value == "Blue":
            trim.configure(bg=Blue)
            selectedWindow.configure(bg=Blue)
            theme_saver("Blue")
            customcolourtext.lower()
        elif new_value == "Indigo":
            trim.configure(bg=Indigo)
            selectedWindow.configure(bg=Indigo)
            theme_saver("Indigo")
            customcolourtext.lower()
        elif new_value == "Violet":
            trim.configure(bg=Violet)
            selectedWindow.configure(bg=Violet)
            theme_saver("Violet")
            customcolourtext.lower()
        elif new_value == "Custom":
            custom_colour()

########################################################################################################################
# Custom Hex Colour Selector                                                                                           #
########################################################################################################################

    def custom_colour():
        customcolourtext.tkraise() # raises the custom colour text box

    def get_custom( event ):
        try:
            customcolourerror.lower()
            customcolour = customcolourtext.get("1.0", 'end-1c') # gets custom colour from text box
            customcolour = str(customcolour) # converts to a string
            if len(customcolour) < 5 and len(customcolour) > 3 or len(customcolour) < 8 and len(customcolour) > 6: #makes sure the colour does update when the input isnt hexidecimal
                trim.configure(bg=customcolour) # sets colour of trim
                selectedWindow.configure(bg=customcolour) # sets window indicator colour
                theme_saver(customcolour) # writes to the cfg file
        except tk.TclError:
            customcolourerror.tkraise()

########################################################################################################################
# Font Picker                                                                                                         #
########################################################################################################################

    def font_confirm(font_value):
        if font_value == "Default": # if font is "Default"
            colourdropdownMenutitle.configure(font=("Futura", 15, "italic")) # set all text in the gui as italic Futura, size 15
            fontdropdownMenutitle.configure(font=("Futura", 15, "italic"))
            themedropdownMenutitle.configure(font=("Futura", 15, "italic"))
            generalb.configure(font=("Futura", 15, "italic"))
            settingsb.configure(font=("Futura", 15, "italic"))
            copyeb.configure(font=("Futura", 15, "italic"))
            copydb.configure(font=("Futura", 15, "italic"))
            closeb.configure(font=("Futura", 15, "italic"))
            encodetextheaderlabel.configure(font=("Futura", 15, "italic"))
            decodetextheaderlabel.configure(font=("Futura", 15, "italic"))
            encodebrowse.configure(font=("Futura", 15, "italic"))
            decodebrowse.configure(font=("Futura", 15, "italic"))
            keylabel.configure(font=("Futura", 15, "italic"))
            decodebrowse.configure(font=("Futura", 15, "italic"))
            encodebrowse.configure(font=("Futura", 15, "italic"))
            colour_saver("Defaultf") # write to the file
        elif font_value == "Futura": # if font_value is anything else,
            colourdropdownMenutitle.configure(font=("Futura", 15, "italic")) # set all text that font
            fontdropdownMenutitle.configure(font=("Futura", 15, "italic"))
            themedropdownMenutitle.configure(font=("Futura", 15, "italic"))
            generalb.configure(font=("Futura", 15, "italic"))
            settingsb.configure(font=("Futura", 15, "italic"))
            copyeb.configure(font=("Futura", 15, "italic"))
            copydb.configure(font=("Futura", 15, "italic"))
            closeb.configure(font=("Futura", 15, "italic"))
            encodebrowse.configure(font=("Futura", 15, "italic"))
            decodebrowse.configure(font=("Futura", 15, "italic"))
            encodetextheaderlabel.configure(font=("Futura", 15, "italic"))
            decodetextheaderlabel.configure(font=("Futura", 15, "italic"))
            keylabel.configure(font=("Futura", 15, "italic"))
            decodebrowse.configure(font=("Futura", 15, "italic"))
            encodebrowse.configure(font=("Futura", 15, "italic"))
            colour_saver("Futura")
        elif font_value == "Helvetica":
            colourdropdownMenutitle.configure(font=("Helvetica", 15, "italic"))
            fontdropdownMenutitle.configure(font=("Helvetica", 15, "italic"))
            themedropdownMenutitle.configure(font=("Helvetica", 15, "italic"))
            generalb.configure(font=("Helvetica", 15, "italic"))
            settingsb.configure(font=("Helvetica", 15, "italic"))
            copyeb.configure(font=("Helvetica", 15, "italic"))
            copydb.configure(font=("Helvetica", 15, "italic"))
            closeb.configure(font=("Helvetica", 15, "italic"))
            encodebrowse.configure(font=("Helvetica", 15, "italic"))
            decodebrowse.configure(font=("Helvetica", 15, "italic"))
            encodetextheaderlabel.configure(font=("Helvetica", 15, "italic"))
            decodetextheaderlabel.configure(font=("Helvetica", 15, "italic"))
            keylabel.configure(font=("Helvetica", 15, "italic"))
            decodebrowse.configure(font=("Helvetica", 15, "italic"))
            encodebrowse.configure(font=("Helvetica", 15, "italic"))
            colour_saver("Helvetica")
        elif font_value == "Trajan":
            colourdropdownMenutitle.configure(font=("Trajan", 15, "italic"))
            fontdropdownMenutitle.configure(font=("Trajan", 15, "italic"))
            themedropdownMenutitle.configure(font=("Trajan", 15, "italic"))
            generalb.configure(font=("Trajan", 13, "italic"))
            settingsb.configure(font=("Trajan", 13, "italic"))
            copyeb.configure(font=("Trajan", 15, "italic"))
            copydb.configure(font=("Trajan", 15, "italic"))
            closeb.configure(font=("Trajan", 15, "italic"))
            encodebrowse.configure(font=("Trajan", 15, "italic"))
            decodebrowse.configure(font=("Trajan", 15, "italic"))
            encodetextheaderlabel.configure(font=("Trajan", 15, "italic"))
            decodetextheaderlabel.configure(font=("Trajan", 15, "italic"))
            keylabel.configure(font=("Trajan", 15, "italic"))
            decodebrowse.configure(font=("Trajan", 13, "italic"))
            encodebrowse.configure(font=("Trajan", 13, "italic"))
            colour_saver("Trajan")
        elif font_value == "Garamond":
            colourdropdownMenutitle.configure(font=("Garamond", 16, "italic"))
            fontdropdownMenutitle.configure(font=("Garamond", 16, "italic"))
            themedropdownMenutitle.configure(font=("Garamond", 16, "italic"))
            generalb.configure(font=("Garamond", 16, "italic"))
            settingsb.configure(font=("Garamond", 16, "italic"))
            copyeb.configure(font=("Garamond", 16, "italic"))
            copydb.configure(font=("Garamond", 16, "italic"))
            closeb.configure(font=("Garamond", 16, "italic"))
            encodebrowse.configure(font=("Garamond", 15, "italic"))
            decodebrowse.configure(font=("Garamond", 15, "italic"))
            encodetextheaderlabel.configure(font=("Garamond", 15, "italic"))
            decodetextheaderlabel.configure(font=("Garamond", 15, "italic"))
            keylabel.configure(font=("Garamond", 15, "italic"))
            decodebrowse.configure(font=("Garamond", 16, "italic"))
            encodebrowse.configure(font=("Garamond", 16, "italic"))
            colour_saver("Garamond")
        elif font_value == "Bodoni":
            colourdropdownMenutitle.configure(font=("Bodoni", 15, "italic"))
            fontdropdownMenutitle.configure(font=("Bodoni", 15, "italic"))
            themedropdownMenutitle.configure(font=("Bodoni", 15, "italic"))
            generalb.configure(font=("Bodoni", 13, "italic"))
            settingsb.configure(font=("Bodoni", 13, "italic"))
            copyeb.configure(font=("Bodoni", 15, "italic"))
            copydb.configure(font=("Bodoni", 15, "italic"))
            closeb.configure(font=("Bodoni", 15, "italic"))
            encodebrowse.configure(font=("Bodoni", 15, "italic"))
            decodebrowse.configure(font=("Bodoni", 15, "italic"))
            encodetextheaderlabel.configure(font=("Bodoni", 15, "italic"))
            decodetextheaderlabel.configure(font=("Bodoni", 15, "italic"))
            keylabel.configure(font=("Bodoni", 15, "italic"))
            decodebrowse.configure(font=("Bodoni", 13, "italic"))
            encodebrowse.configure(font=("Bodoni", 13, "italic"))
            colour_saver("Bodoni")
        elif font_value == "Comic Sans":
            colourdropdownMenutitle.configure(font=("Comic Sans MS", 15, "italic"))
            fontdropdownMenutitle.configure(font=("Comic Sans MS", 15, "italic"))
            themedropdownMenutitle.configure(font=("Comic Sans MS", 15, "italic"))
            generalb.configure(font=("Comic Sans MS", 13, "italic"))
            settingsb.configure(font=("Comic Sans MS", 13, "italic"))
            copyeb.configure(font=("Comic Sans MS", 15, "italic"))
            copydb.configure(font=("Comic Sans MS", 15, "italic"))
            closeb.configure(font=("Comic Sans MS", 15, "italic"))
            encodebrowse.configure(font=("Comic Sans MS", 15, "italic"))
            decodebrowse.configure(font=("Comic Sans MS", 15, "italic"))
            encodetextheaderlabel.configure(font=("Comic Sans MS", 15, "italic"))
            decodetextheaderlabel.configure(font=("Comic Sans MS", 15, "italic"))
            keylabel.configure(font=("Comic Sans MS", 15, "italic"))
            decodebrowse.configure(font=("Comic Sans MS", 13, "italic"))
            encodebrowse.configure(font=("Comic Sans MS", 13, "italic"))
            colour_saver("Comic Sans")
        elif font_value == "Verdana":
            colourdropdownMenutitle.configure(font=("Verdana", 15, "italic"))
            fontdropdownMenutitle.configure(font=("Verdana", 15, "italic"))
            themedropdownMenutitle.configure(font=("Verdana", 15, "italic"))
            generalb.configure(font=("Verdana", 13, "italic"))
            settingsb.configure(font=("Verdana", 13, "italic"))
            copyeb.configure(font=("Verdana", 15, "italic"))
            copydb.configure(font=("Verdana", 15, "italic"))
            closeb.configure(font=("Verdana", 15, "italic"))
            encodebrowse.configure(font=("Verdana", 15, "italic"))
            decodebrowse.configure(font=("Verdana", 15, "italic"))
            encodetextheaderlabel.configure(font=("Verdana", 15, "italic"))
            decodetextheaderlabel.configure(font=("Verdana", 15, "italic"))
            keylabel.configure(font=("Verdana", 15, "italic"))
            decodebrowse.configure(font=("Verdana", 15, "italic"))
            encodebrowse.configure(font=("Verdana", 15, "italic"))
            colour_saver("Verdana")
########################################################################################################################
# Theme Picker                                                                                                         #
########################################################################################################################

    def theme_confirm(theme_value):
        if theme_value == "Dark": # if theme_value is dark
            header.configure(bg=hdc)  # setting the colours of the background
            generalb.configure(highlightbackground=hdc)
            settingsb.configure(highlightbackground=hdc)
            decodebrowse.configure(highlightbackground=hdc)
            encodebrowse.configure(highlightbackground=hdc)
            copydb.configure(highlightbackground=bgc)
            copyeb.configure(highlightbackground=bgc)
            root.configure(bg=bgc)
            hider.configure(bg=bgc)
            closeb.configure(highlightbackground=bgc)
            encodetext.configure(bg=hdc, highlightbackground=hdc)
            decodetext.configure(bg=hdc, highlightbackground=hdc)
            encodetextheader.configure(bg=hdc)
            encodetextheaderlabel.configure(bg=hdc, fg="white") # setting font colours
            decodetextheader.configure(bg=hdc)
            decodetextheaderlabel.configure(bg=hdc, fg="white")
            colourdropdownMenuheader.configure(bg=hdc)
            colourdropdownMenu.configure(bg=bgc)
            colourdropdownMenutitle.configure(bg=hdc, fg="white")
            themedropdownMenuheader.configure(bg=hdc)
            themedropdownMenu.configure(bg=bgc)
            themedropdownMenutitle.configure(bg=hdc, fg="white")
            fontdropdownMenutitle.configure(bg=hdc, fg="white")
            fontdropdownMenu.configure(bg=bgc)
            fontdropdownMenuheader.configure(bg=hdc)
            keylabelheader.configure(bg=hdc)
            customcolourerror.configure(bg=bgc)
            keylabel.configure(bg=hdc, fg="white")
            keyconfirmbutton.configure(highlightbackground=bgc)
            keytext.configure(bg=hdc, fg="white", highlightbackground=hdc)
            keytextbacking.configure(bg=hdc)
            encodetext.configure(fg="white")
            decodetext.configure(fg="white")
            font_saver("Dark")

        elif theme_value == "Light": # if theme_value is light
            header.configure(bg=lighthdc) # set all colours to the lighter setting
            generalb.configure(highlightbackground=lighthdc)
            settingsb.configure(highlightbackground=lighthdc)
            decodebrowse.configure(highlightbackground=lighthdc)
            encodebrowse.configure(highlightbackground=lighthdc)
            copydb.configure(highlightbackground=lightbgc)
            copyeb.configure(highlightbackground=lightbgc)
            root.configure(bg=lightbgc)
            hider.configure(bg=lightbgc)
            closeb.configure(highlightbackground=lightbgc)
            encodetext.configure(bg=lighthdc, highlightbackground=lighthdc)
            decodetext.configure(bg=lighthdc, highlightbackground=lighthdc)
            encodetextheader.configure(bg=lighthdc)
            customcolourerror.configure(bg=lightbgc)
            encodetextheaderlabel.configure(bg=lighthdc, fg="black")
            decodetextheader.configure(bg=lighthdc)
            decodetextheaderlabel.configure(bg=lighthdc, fg="black")
            colourdropdownMenuheader.configure(bg=lighthdc)
            colourdropdownMenu.configure(bg=lightbgc)
            colourdropdownMenutitle.configure(bg=lighthdc, fg="black")
            themedropdownMenuheader.configure(bg=lighthdc)
            themedropdownMenu.configure(bg=lightbgc)
            themedropdownMenutitle.configure(bg=lighthdc, fg="black")
            fontdropdownMenutitle.configure(bg=lighthdc, fg="black")
            fontdropdownMenu.configure(bg=lightbgc)
            fontdropdownMenuheader.configure(bg=lighthdc)
            keylabelheader.configure(bg=lighthdc)
            keylabel.configure(bg=lighthdc, fg="black")
            keyconfirmbutton.configure(highlightbackground=lightbgc)
            keytext.configure(bg=lighthdc, fg="black", highlightbackground=lighthdc)
            keytextbacking.configure(bg=lighthdc)
            encodetext.configure(fg="black")
            decodetext.configure(fg="black")
            font_saver("Light")


########################################################################################################################
# Settings button commands                                                                                             #
########################################################################################################################

    def settings_button(): # this is the command that is triggered when the setting tab button is pressed
        encodetextheadershadow.lower() # Lowers the header above the encode text box's shadow so that it is not visable
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
        encodebrowse.lower() # lowers encode browse button
        decodebrowse.lower() # lowers decode browse button
        colourdropdownMenu.tkraise() # Raises the dropdown menu
        colourdropdownMenuheadershadow.tkraise() # Raises the dropdown menu header shadow
        colourdropdownMenuheader.tkraise() # Raises the dropdown menu header
        colourdropdownMenutitle.tkraise() # Raises the dropdown menu title
        themedropdownMenu.tkraise() # raises the theme drop down menu
        themedropdownMenuheadershadow.tkraise() # raises the theme drop down menu header shadow before the header so the shadow is behind it
        themedropdownMenuheader.tkraise() # raises the theme drop down menu header
        themedropdownMenutitle.tkraise() # raises the theme drop down title
        fontdropdownMenu.tkraise() # raises the font drop down menu
        fontdropdownMenuheadershadow.tkraise() # raises the font drop down menu header shadow
        fontdropdownMenuheader.tkraise() # raises the font drop down menu header
        keylabelheadershadow.tkraise() # raiese the ky label
        fontdropdownMenutitle.tkraise()
        keytextbackingshadow.tkraise()
        keylabelheader.tkraise()
        keylabel.tkraise()
        keyconfirmbutton.tkraise()
        keytextbacking.tkraise()
        keytext.tkraise()
        selectedWindow.place(relx=0.094, rely=0.04) # positions the current window indicator below the settings window

########################################################################################################################
# General button commands                                                                                              #
########################################################################################################################

    def general_button(): # this is the command that is triggered when the general button is triggered
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
        encodebrowse.tkraise()
        decodebrowse.tkraise()
        colourdropdownMenu.lower() #  lowers the dropdown menu
        colourdropdownMenuheader.lower() # lowers the dropdown menu header
        colourdropdownMenutitle.lower() # lowers the dropdown menu title
        colourdropdownMenuheadershadow.lower() # lowers the dropdown menu header shadow
        themedropdownMenu.lower()
        themedropdownMenuheadershadow.lower()
        themedropdownMenuheader.lower()
        themedropdownMenutitle.lower()
        fontdropdownMenu.lower()
        fontdropdownMenuheadershadow.lower()
        fontdropdownMenuheader.lower()
        fontdropdownMenutitle.lower()
        keytext.lower()
        keylabel.lower()
        keyconfirmbutton.lower()
        keylabelheader.lower()
        keylabelheadershadow.lower()
        keytextbacking.lower()
        keytextbackingshadow.lower()
        selectedWindow.place(relx=0.004, rely=0.04) # positions the current window indicator below the general window


########################################################################################################################
# Settings Page                                                                                                        #
########################################################################################################################

    colourdropdownMenu = tk.OptionMenu(root, tkvar, *Colours, command=colour_confirm) # makes the dropdown menu
    colourdropdownMenu.place(relx=0.202, rely=0.105) # places the dropdown menu relative to the window
    colourdropdownMenu.configure(bg=bgc) # makes the background colour of the dropdown menu the same as the pages background

    colourdropdownMenuheader = tk.Frame(root, bg=hdc,width=130, height=31,) # makes box for the header above the drop down menu
    colourdropdownMenuheader.place(relx=0.04, rely=0.1) # places the header relative to the window

    colourdropdownMenuheadershadow = tk.Frame(root, bg="black",width=130, height=31,) # makes shadow under the header above the drop down menu
    colourdropdownMenuheadershadow.place(relx=0.042, rely=0.105) # places the shadow relative to the window

    colourdropdownMenutitle = tk.Label(root, text="Choose a colour") # creates the label for the colour picker
    colourdropdownMenutitle.place(relx=0.04, rely=0.105) # places the label for the colour picker on the header
    colourdropdownMenutitle.configure(font=("Futura",15, "italic"),fg="white", bg=hdc) # changes the font, font colour and background colour of the label

    themedropdownMenu = tk.OptionMenu(root, tkvar2, *Themes, command=theme_confirm) # makes the dropdown menu
    themedropdownMenu.place(relx=0.202, rely=0.205) # places the dropdown menu relative to the window
    themedropdownMenu.configure(bg=bgc) # makes the background colour of the dropdown menu the same as the pages background

    themedropdownMenuheader = tk.Frame(root, bg=hdc,width=130, height=31,) # makes box for the header above the drop down menu
    themedropdownMenuheader.place(relx=0.04, rely=0.2) # places the header relative to the window

    themedropdownMenuheadershadow = tk.Frame(root, bg="black",width=130, height=31,) # makes shadow under the header above the drop down menu
    themedropdownMenuheadershadow.place(relx=0.042, rely=0.205) # places the shadow relative to the window

    themedropdownMenutitle = tk.Label(root, text="Choose a theme") # creates the label for the colour picker
    themedropdownMenutitle.place(relx=0.04, rely=0.205) # places the label for the colour picker on the header
    themedropdownMenutitle.configure(font=("Futura",15, "italic"),fg="white", bg=hdc) # changes the font, font colour and background colour of the label

    fontdropdownMenutitle = tk.Label(root, text="Choose a font") # creates the label for the colour picker
    fontdropdownMenutitle.place(relx=0.04, rely=0.305) # places the label for the colour picker on the header
    fontdropdownMenutitle.configure(font=("Futura",15, "italic"),fg="white", bg=hdc) # changes the font, font colour and background colour of the label

    fontdropdownMenu = tk.OptionMenu(root, tkvar3, *Fonts, command=font_confirm) # makes the dropdown menu
    fontdropdownMenu.place(relx=0.202, rely=0.305) # places the dropdown menu relative to the window
    fontdropdownMenu.configure(bg=bgc) # makes the background colour of the dropdown menu the same as the pages background

    fontdropdownMenuheader = tk.Frame(root, bg=hdc,width=130, height=31,) # makes box for the header above the drop down menu
    fontdropdownMenuheader.place(relx=0.04, rely=0.3) # places the header relative to the window

    fontdropdownMenuheadershadow = tk.Frame(root, bg="black",width=130, height=31,) # makes shadow under the header above the drop down menu
    fontdropdownMenuheadershadow.place(relx=0.042, rely=0.305) # places the shadow relative to the window

    customcolourtext = tk.Text(root,height=1, width=7,bg="white", fg="black", borderwidth=2) # creates the label for the colour picker
    customcolourtext.place(relx=0.34, rely=0.105) # places the label for the colour picker on the header

    customcolourerror = tk.Label(root, text="error, colour does not exist", bg=bgc, fg="red")
    customcolourerror.place(relx=0.21, rely=0.155)

    customcolourtext.bind("<KeyRelease>", get_custom) # binds the get_custom command to a key

    keylabelheadershadow = tk.Frame(root, bg="black",width=40, height=31,) # shadow for the key label header
    keylabelheadershadow.place(relx=0.502, rely=0.11) # places shadow

    keylabelheader = tk.Frame(root, bg=hdc,width=40, height=31,)
    keylabelheader.place(relx=0.50, rely=0.105)

    keylabel = tk.Label(root, text="Key:")
    keylabel.place(relx=0.50, rely=0.105)
    keylabel.configure(font=("Futura",15, "italic"),fg="white", bg=hdc)

    keytext = tk.Text(root, height=1, width=24, bg=hdc, fg="white", borderwidth=0)
    keytext.place(relx=0.56, rely=0.105)
    keytext.config(highlightbackground=hdc)

    keytextbacking = tk.Frame(root, bg=hdc,width=176, height=31)
    keytextbacking.place(relx=0.56, rely=0.105)

    keytextbackingshadow = tk.Frame(root, bg="black",width=176, height=31)
    keytextbackingshadow.place(relx=0.562, rely=0.11)

    keylabelheader = tk.Frame(root, bg=hdc,width=40, height=31,)
    keylabelheader.place(relx=0.50, rely=0.105)

    keyconfirmbutton = tk.Button(root, text="Confirm", command=key_confirm)
    keyconfirmbutton.place(relx=0.79, rely=0.105)
    keyconfirmbutton.configure(highlightbackground=bgc)

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

    generalb = tk.Button(root, text="General",highlightbackground=hdc, command=general_button) # creates general button
    generalb.place(relx=0.0, rely=0.0, height=24, width=75) # positions the button on the toolbar relative to the window
    generalb.config(font=("Futura",15, "italic")) # sets font and text size for general button

    settingsb = tk.Button(root, text="Settings",highlightbackground=hdc, command=settings_button) # creates settings button
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

    encodetext = tk.Text(root,height=25, width=47,bg = hdc, fg="white", borderwidth=2) # creates the text box
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
# file dialog                                                                                                          #
########################################################################################################################

    def encodefromfile():
        try:
            root.filename = tk.filedialog.askopenfilename(filetypes = (("text files", "*.txt"),("all files", "*.*")))
            with open('user.cfg', 'r') as f:
                cfg = [line.strip() for line in f]
            key = cfg[3] # key is the 4th line in the cfg file
            f.close()
            f = open(root.filename, "r")
            input = f.read()
            encrypted = [] # creates list called "encrypted"
            for i, c in enumerate(input): # *
                key_c = ord(key[i % len(key)])
                input_c = ord(c)
                encrypted.append(chr((input_c + key_c) % 127))
            encrypted = ''.join(encrypted)
            f.close()
            f = tk.filedialog.asksaveasfile(mode='w', defaultextension=".txt")
            if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
                return
            encoded_string = str(encrypted)
            f.write(encoded_string)
            f.close()
        except FileNotFoundError:
            ""

    def decodefromfile():
        try:
            root.filename = tk.filedialog.askopenfilename(filetypes = (("text files", "*.txt"),("all files", "*.*")))
            with open('user.cfg', 'r') as f:
                cfg = [line.strip() for line in f]
            key = cfg[3] # key is the 4th line in the cfg file
            f.close()
            f = open(root.filename, "r")
            input = f.read()
            encrypted = [] # creates list called "encrypted"
            for i, c in enumerate(input): # loops over input
                key_c = ord(key[i % len(key)])
                input_c = ord(c)
                encrypted.append(chr((input_c - key_c) % 127))
            encrypted = ''.join(encrypted)
            f.close()
            f = tk.filedialog.asksaveasfile(mode='w', defaultextension=".txt")
            if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
                return
            text2save = str(encrypted)
            f.write(text2save)
            f.close()
        except FileNotFoundError:
            ""

    encodebrowse = tk.Button(root, text="Browse", highlightbackground=hdc, command=encodefromfile)
    encodebrowse.place(relx=0.05,rely=0.1)

    decodebrowse = tk.Button(root, text="Browse", highlightbackground=hdc, command=decodefromfile)
    decodebrowse.place(relx=0.86,rely=0.1)


########################################################################################################################
# Encryption/Decryption Function                                                                                       #
########################################################################################################################

    def encrypt( event ):
        with open('user.cfg', 'r') as f:
            cfg = [line.strip() for line in f]
        key = cfg[3] # key is the 4th line in the cfg file
        f.close()
        encrypted = [] # creates list called "encrypted"
        input = encodetext.get("1.0", 'end-1c') # gets input from input box
        input = input.strip("_") # strips underscores (prevents gui from freezing)
        decodetext.delete("1.0", 'end-1c') # deletes what is in the decode box
        for i, c in enumerate(input): # loops over input
            key_c = ord(key[i % len(key)])
            input_c = ord(c)
            encrypted.append(chr((input_c + key_c) % 127))
        encrypted = ''.join(encrypted)
        decodetext.insert('end', encrypted)

    def decrypt( event ):
        with open('user.cfg', 'r') as f:
            cfg = [line.strip() for line in f]
        key = cfg[3]
        f.close()
        decrypted = []
        inputd = decodetext.get("1.0", 'end-1c')
        encodetext.delete("1.0", 'end-1c')
        for i, c in enumerate(inputd):
            key_c = ord(key[i % len(key)])
            inputd_c = ord(c)
            decrypted.append(chr((inputd_c - key_c) % 127))
        if "_" not in decrypted:
            decrypted = ''.join(decrypted)
            encodetext.insert('end', decrypted)

    decodetext.bind("<KeyRelease>", decrypt)# binds the users key releases to the decodethetext command which performs the algorythm
    encodetext.bind("<KeyRelease>", encrypt) # binds the users key releases to the encodethetext command. this makes the decode and encoding process realtime (converted as you type it)
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
    try:
        with open('user.cfg', 'r') as f:
            cfg = [line.strip() for line in f]
        colour = cfg[0]
        first = colour[0]
        theme = cfg[1]
        font = cfg[2]
        key = cfg[3]
        if colour == "Default":
            colour_confirm(Default)
        elif first == "#":
            trim.configure(bg=colour)
            selectedWindow.configure(bg=colour)
            tkvar.set(colour)
        elif colour in Colours: # if x isnt nothing and it also isnt "default"
            trim.configure(bg=colour)
            selectedWindow.configure(bg=colour)
            tkvar.set(colour)
            if theme != "":  # if x isnt nothing and it also isnt "default"
                theme_confirm(theme)
                tkvar2.set(theme)
                if font != "":  # if x isnt nothing and it also isnt "default"
                    font_confirm(font)
                    tkvar3.set(font)
                    if key != "":
                        key_saver(key)
                    else:
                        print("Invalid Key detected in 'user.cfg', Setting to default...")
                        default_key_set()
                else:
                    print("Invalid Font detected in 'user.cfg', Setting to default...")
                    default_font_set()
            else:
                print("Invalid Theme detected in 'user.cfg', Setting to default...")
                default_theme_set()
        elif colour not in Colours:
            print("Invalid Colour detected in 'user.cfg', Setting to default...")
            default_colour_set()
    except IndexError:
        print("Invalid Style detected in 'User.cfg', Setting to default...")
        default_all_set()


########################################################################################################################
# Main loop                                                                                                            #
########################################################################################################################

    root.mainloop() # starts mainloop

########################################################################################################################
# Login Screen                                                                                                         #
########################################################################################################################


def Login():

    username1 = "User123"
    password1 = "CoolPassword123"

    root = tk.Tk()
    root.title("Login") # gives title to gui
    w = 400  # width for the Tk root
    h = 300  # height for the Tk root
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (400, 300, x, y))
    root.resizable(False, False) # disallows window resizing
    bgc = "#515151" # default background colour (dark grey)
    dbgc = "#3d3d3d"
    root.configure(bg=bgc) # sets windows background colour as dark grey

    def loginb():
        u = username.get()
        p = password.get()
        if u != username1 and p != password1:
            errorusername.lower()
            errorpassword.lower()
            errorboth.tkraise()
        elif u == username1:
            if p == password1:
                root.destroy()
                main()
            else:
                errorboth.lower()
                errorusername.lower()
                errorpassword.tkraise()
        else:
            errorboth.lower()
            errorpassword.lower()
            errorusername.tkraise()

    errorusername = tk.Label(root,bg=bgc, fg="red", text="Invalid Username!")
    errorusername.place(relx=.4,rely=.65)

    errorpassword = tk.Label(root, bg=bgc, fg="red", text="Invalid Password!")
    errorpassword.place(relx=.4, rely=.65)

    errorboth = tk.Label(root, bg=bgc, fg="red", text="Invalid Username and Password!")
    errorboth.place(relx=.4, rely=.65)

    background = tk.Frame(root, bg=bgc,width=400, height=300)
    background.place(relx=0,rely=0)

    usernamelabel = tk.Label(root,text = "Username:", bg=bgc, fg="white")
    usernamelabel.place(relx=.2,rely=.35)

    username = tk.Entry(root,bg=dbgc, fg="white", borderwidth=2, highlightbackground = dbgc) # creates the label for the colour picker
    username.place(relx=.4,rely=.35)

    passwordlabel = tk.Label(root,text = "Password:", bg=bgc, fg="white")
    passwordlabel.place(relx=.2,rely=.45)

    password = tk.Entry(root,bg=dbgc, fg="white", borderwidth=2, highlightbackground = dbgc, show="*") # creates the label for the colour picker
    password.place(relx=.4,rely=.45)

    loginb = tk.Button(root,text = "Login", highlightbackground=bgc, command=loginb)
    loginb.place(relx=.4,rely=.55)

    root.mainloop()

Login()