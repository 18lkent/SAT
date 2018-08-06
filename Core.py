### Software created by Lachlan Kent ###
   ### Begin date: fri 8/jun/2018 ###
### Completion date:___ __/___/___ 2018 ###

running = 0
print("1. Plane Text\n2. File\n3. Exit") #key for decisions

while running == 0:
    initial_mode = str(input("Enter Decision: "))
    if initial_mode == "1":
        type = input("Encrypt or Decrypt")
        if type == "Encrypt":
            key = input("Key: ")
            einput = input("Enter String to Encode: ")
            encrypted = []
            for i, c in enumerate(einput):
                key_c = ord(key[i % len(key)])
                input_c = ord(c)
                encrypted.append(chr((input_c + key_c) % 127))
            encrypted = ''.join(encrypted)
            print(encrypted)

        elif type == "Decrypt":
            key = input("Key: ")
            dinput = input("Enter String to Decode: ")
            decrypted = []
            for i, c in enumerate(dinput):
                key_c = ord(key[i % len(key)])
                inputd_c = ord(c)
                decrypted.append(chr((inputd_c - key_c) % 127))
            decrypted = ''.join(decrypted)
            print(decrypted)

    elif initial_mode == "2":
        file = input("Enter file name: ")
        type = input("Encrypt or Decrypt: ")
        type = type.lower()
        if type == "encrypt":
            key = input("Key: ")
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

        elif type == "decrypt":
            key = input("Key: ")
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