### Software created by Lachlan Kent ###
   ### Begin date: Fri 8 jun 2018 ###

print("1. Encode\n2. Decode\n3. Exit") #key for decisions
running = 0

while running == 0:
    mode_input = str(input("Enter Decision: ")) #enter input for mode (encrpyt or decrypt)

    if mode_input == "1": #If the user wishes to encrypt a file
        file_input = input("Enter filename to Encrypt: ") #Asks the user to enter a text file to have its contents encrypted
        f = open(file_input , 'r') #opens the user specified file
        for line in f:
            line = line.replace("A", "f4").replace("B", "a4").replace("C", "a1").replace("D", "e3").replace("E","b6").replace("F", "d1").replace("G", "c4").replace("H", "b5").replace("I", "c2").replace("J", "d3").replace("K", "f3").replace("L", "e6").replace("M", "a2").replace("N", 'd5').replace("O", "b3").replace("P", "a6").replace("Q","d6").replace("R", "b1").replace("S", "d2").replace("T", "b4").replace("U", "a5").replace("V", "b2").replace("W","a3").replace("X", "f5").replace("Y", "c6").replace("Z", "c1").replace(" ","4!")
            x = open(file_input, 'w')
            x.write(line)
        running = 1

    elif mode_input == "2":
        file_input = input("Enter filename to Decrypt ") #Asks the user to enter a text file to have its contents decrypted
        f = open(file_input, 'r+')  # opens the user specified file
        running = 1

    elif mode_input == "3":
        exit(0)

    else:
        print("Invalid input detected, Try again!")