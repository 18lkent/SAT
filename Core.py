### Software created by Lachlan Kent ###
   ### Begin date: fri 8/jun/2018 ###
### Completion date:___ __/___/___ 2018 ###

""" *
the encryption and decryption algorythm works by
taking the users input and the key, converting
them to the unicode code point of the character,
offsetting the users input by getting the modulo
of the input and the key added by 127, and converting
it back to english letters
"""

running = 0

while running == 0:
    print("\nLachlan Kent's Cryptography Program\n\nSelect what you would like to use:\n\n1. Plane Text\n2. File\n3. Exit")  # key for decisions
    initial_mode = str(input("\nEnter Decision: ")) # asks user for their decision
    initial_mode.lower() # makes users input lowercase
    if initial_mode == "1":
        print("\n1. Encrypt\n2. Decrypt") # key for decision
        type = input("\nEnter Decision: ") # asks user for their decision

        if type == "encrypt" or type == "1":
            key = input("\nKey: ") # asks user for desired key
            einput = input("\nEnter String to Encode: ") # asks user for a string to use
            encrypted = [] # creates list called encrypted
            for i, c in enumerate(einput):
                key_c = ord(key[i % len(key)]) # *
                input_c = ord(c)
                encrypted.append(chr((input_c + key_c) % 127))
            encrypted = ''.join(encrypted)
            print("\nOutput:",encrypted+"\n")

        elif type == "decrypt" or type == "2":
            key = input("\nKey: ")
            dinput = input("\nEnter String to Decode: ")
            decrypted = []
            for i, c in enumerate(dinput):
                key_c = ord(key[i % len(key)])
                inputd_c = ord(c)
                decrypted.append(chr((inputd_c - key_c) % 127))
            decrypted = ''.join(decrypted)
            print("\nOutput:",decrypted+"\n")

        else:
            print("\nInvalid Input\n")

    elif initial_mode == "2":
        file = input("\nEnter file name: ")
        print("\n1. Encrypt\n2. Decrypt")
        type = input("\nEncrypt or Decrypt: ")
        type = type.lower()
        if type == "encrypt" or type == "1":
            key = input("\nKey: ")
            f = open(file,"r")
            einput = f.read()
            encrypted = []
            for i, c in enumerate(einput):
                key_c = ord(key[i % len(key)])
                input_c = ord(c)
                encrypted.append(chr((input_c + key_c) % 127))
            encrypted = ''.join(encrypted)
            f.close()
            f = open(file, "w")
            f.write(encrypted)
            f.close()

        elif type == "decrypt" or type == "2":
            key = input("\nKey: ")
            f = open(file, "r")
            dinput = f.read()
            decrypted = []
            for i, c in enumerate(dinput):
                key_c = ord(key[i % len(key)])
                input_c = ord(c)
                decrypted.append(chr((input_c - key_c) % 127))
            decrypted = ''.join(decrypted)
            f.close()
            f = open(file, "w")
            f.write(decrypted)
            f.close()

    elif initial_mode == "3":
        exit(0)

    else:
        print("\nInvalid Input\n")