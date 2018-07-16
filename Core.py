### Software created by Lachlan Kent ###
   ### Begin date: Fri 8 jun 2018 ###

running = 0
print("1. Plane Text\n2. File\n3. Exit") #key for decisions

while running == 0:
    initial_mode = str(input("Enter Decision: "))
    if initial_mode == "1":
        print("1. Encode\n2. Decode\n3. Exit")  # key for decisions
        mode_input = str(input("Enter Decision: ")) #enter input for mode (encrpyt or decrypt)
        if mode_input == "1":
            line = input("Enter text to Encode: ")
            line = line.replace("A", "f4").replace("B", "a4").replace("C", "a1").replace("D", "e3").replace("E","b6").replace("F", "d1").replace("G", "c4").replace("H", "b5").replace("I", "c2").replace("J", "d3").replace("K","f3").replace("L", "e6").replace("M", "a2").replace("N", 'd5').replace("O", "b3").replace("P", "a6").replace("Q","d6").replace("R", "b1").replace("S", "d2").replace("T", "b4").replace("U", "a5").replace("V", "b2").replace("W","a3").replace("X", "f5").replace("Y", "c6").replace("Z", "c1").replace(" ", "4!").replace("a", "F4").replace("b","A4").replace("c", "A1").replace("d", "E3").replace("e", "B6").replace("f", "D1").replace("g", "C4").replace("h","B5").replace("i", "C2").replace("j", "D3").replace("k", "F3").replace("l", "E6").replace("m", "A2").replace("n",'D5').replace("o", "B3").replace("p", "A6").replace("q", "D6").replace("r", "B1").replace("s", "D2").replace("t","B4").replace("u", "A5").replace("v", "B2").replace("w", "A3").replace("x", "F5").replace("y", "C6").replace("z","C1").replace("\n", "!!")
            print(line)
            running = 1
        elif mode_input == "2":
            line = input("Enter text to Decode: ")
            line = line.replace("F4", "a").replace("A4", "b").replace("A1", "c").replace("E3", "d").replace("B6","e").replace("D1", "f").replace("C4", "g").replace("B5", "h").replace("C2", "i").replace("D3", "j").replace("F3", "k").replace("E6", "l").replace("A2", "m").replace("D5", 'n').replace("B3", "o").replace("A6", "p").replace("D6","q").replace("B1", "r").replace("D2", "s").replace("B4", "t").replace("A5", "u").replace("B2", "v").replace("A3","w").replace("F5", "x").replace("C6", "y").replace("C1", "z").replace("4!"," ").replace("f4", "A").replace("a4", "B").replace("a1", "C").replace("e3", "D").replace("b6","E").replace("d1", "F").replace("c4", "G").replace("b5", "H").replace("c2", "I").replace("d3", "J").replace("f3", "K").replace("e6", "L").replace("a2", "M").replace("d5", 'N').replace("b3", "O").replace("a6", "P").replace("d6","Q").replace("b1", "R").replace("d2", "S").replace("b4", "T").replace("a5", "U").replace("b2", "V").replace("a3","W").replace("f5", "X").replace("c6", "Y").replace("c1", "Z").replace("!!", "\n")
            print(line)
            running = 1
        elif mode_input == "3":
            exit(0)
        else:
            print("Invalid input detected, Try again!")

    if initial_mode == "2":
        print("1. Encode\n2. Decode\n3. Exit")  # key for decisions
        mode_input = str(input("Enter Decision: "))  # enter input for mode (encrpyt or decrypt)
        if mode_input == "1": #If the user wishes to encrypt a file
            file_input = input("Enter filename to Encrypt: ") #Asks the user to enter a text file to have its contents encrypted
            f = open(file_input , 'r') #opens the user specified file
            for line in f:  #reads and replaces the code
                line = line.replace("A", "f4").replace("B", "a4").replace("C", "a1").replace("D", "e3").replace("E","b6").replace("F", "d1").replace("G", "c4").replace("H", "b5").replace("I", "c2").replace("J", "d3").replace("K", "f3").replace("L", "e6").replace("M", "a2").replace("N", 'd5').replace("O", "b3").replace("P", "a6").replace("Q","d6").replace("R", "b1").replace("S", "d2").replace("T", "b4").replace("U", "a5").replace("V", "b2").replace("W","a3").replace("X", "f5").replace("Y", "c6").replace("Z", "c1").replace(" ","4!").replace("a", "F4").replace("b", "A4").replace("c", "A1").replace("d", "E3").replace("e","B6").replace("f", "D1").replace("g", "C4").replace("h", "B5").replace("i", "C2").replace("j", "D3").replace("k", "F3").replace("l", "E6").replace("m", "A2").replace("n", 'D5').replace("o", "B3").replace("p", "A6").replace("q","D6").replace("r", "B1").replace("s", "D2").replace("t", "B4").replace("u", "A5").replace("v", "B2").replace("w","A3").replace("x", "F5").replace("y", "C6").replace("z", "C1").replace("\n", "!!")
                x = open(file_input, 'w')
                x.write(line)
            running = 1

        elif mode_input == "2":
            file_input = input("Enter filename to Decrypt ") #Asks the user to enter a text file to have its contents decrypted
            f = open(file_input, 'r')  # opens the user specified file
            for line in f:
                line = line.replace("F4", "a").replace("A4", "b").replace("A1", "c").replace("E3", "d").replace("B6","e").replace("D1", "f").replace("C4", "g").replace("B5", "h").replace("C2", "i").replace("D3", "j").replace("F3", "k").replace("E6", "l").replace("A2", "m").replace("D5", 'n').replace("B3", "o").replace("A6", "p").replace("D6","q").replace("B1", "r").replace("D2", "s").replace("B4", "t").replace("A5", "u").replace("B2", "v").replace("A3","w").replace("F5", "x").replace("C6", "y").replace("C1", "z").replace("4!"," ").replace("f4", "A").replace("a4", "B").replace("a1", "C").replace("e3", "D").replace("b6","E").replace("d1", "F").replace("c4", "G").replace("b5", "H").replace("c2", "I").replace("d3", "J").replace("f3", "K").replace("e6", "L").replace("a2", "M").replace("d5", 'N').replace("b3", "O").replace("a6", "P").replace("d6","Q").replace("b1", "R").replace("d2", "S").replace("b4", "T").replace("a5", "U").replace("b2", "V").replace("a3","W").replace("f5", "X").replace("c6", "Y").replace("c1", "Z").replace("!!", "\n")
                x = open(file_input, 'w')
                x.write(line)
            running = 1
        elif mode_input == "3":
            exit(0)
        else:
            print("Invalid input detected, Try again!")
    if initial_mode == "3":
        exit(0)